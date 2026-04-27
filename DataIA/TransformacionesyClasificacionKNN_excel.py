from __future__ import annotations

import pickle
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import LeaveOneOut, cross_val_predict, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "dataIA.xlsx"
MODEL_PATH = BASE_DIR / "modelo_knn_satisfaccion.pkl"
TRANSFORMED_PATH = BASE_DIR / "dataset_transformado_satisfaccion.csv"

TARGET_MAP = {
    "no me gusta": 0,
    "neutral": 1,
    "neutro": 1,
    "me gusta": 2,
}

TARGET_LABELS = {
    0: "no me gusta",
    1: "neutral",
    2: "me gusta",
}


def clean_text(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value))
    text = text.encode("ascii", "ignore").decode("ascii")
    return text.strip().lower()


def clean_column_name(value: object) -> str:
    text = clean_text(value)
    text = text.replace(" ", "_")
    text = text.replace("-", "_")
    return text


def make_one_hot_encoder() -> OneHotEncoder:
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"No se encontro el archivo Excel: {path}")

    df = pd.read_excel(path)
    df.columns = [clean_column_name(column) for column in df.columns]

    rename_map = {}
    if "pas" in df.columns and "pais" not in df.columns:
        rename_map["pas"] = "pais"
    if "nivelsatisfaccion" in df.columns:
        rename_map["nivelsatisfaccion"] = "nivel_satisfaccion"

    if rename_map:
        df = df.rename(columns=rename_map)

    required_columns = {"sexo", "edad", "pais", "nivel_satisfaccion"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas en el Excel: {sorted(missing)}")

    df = df.copy()
    df["nivel_satisfaccion"] = df["nivel_satisfaccion"].map(lambda value: TARGET_MAP.get(clean_text(value), np.nan))
    df = df.dropna(subset=["nivel_satisfaccion"])
    df["nivel_satisfaccion"] = df["nivel_satisfaccion"].astype(int)
    df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
    df = df.dropna(subset=["edad"])
    df["edad"] = df["edad"].astype(float)
    return df.reset_index(drop=True)


def build_pipeline() -> Pipeline:
    categorical_features = ["sexo", "pais"]
    numeric_features = ["edad"]

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", make_one_hot_encoder()),
        ]
    )

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", categorical_transformer, categorical_features),
            ("num", numeric_transformer, numeric_features),
        ],
        remainder="drop",
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("knn", KNeighborsClassifier(n_neighbors=3, metric="minkowski")),
        ]
    )


def save_model(model: Pipeline, path: Path) -> None:
    with path.open("wb") as handle:
        pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_model(path: Path) -> Pipeline:
    with path.open("rb") as handle:
        return pickle.load(handle)


def encode_dataset(model: Pipeline, X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    transformed = model.named_steps["preprocessor"].transform(X)
    feature_names = model.named_steps["preprocessor"].get_feature_names_out()
    transformed_df = pd.DataFrame(transformed, columns=feature_names)
    transformed_df["nivel_satisfaccion"] = y.to_numpy()
    return transformed_df


def predict_new_sample(model: Pipeline, sexo: str, edad: float, pais: str) -> pd.DataFrame:
    sample = pd.DataFrame(
        [{
            "sexo": sexo,
            "edad": edad,
            "pais": pais,
        }]
    )
    pred_class = int(model.predict(sample)[0])
    proba = model.predict_proba(sample)[0]
    confidence = float(np.max(proba))
    return pd.DataFrame(
        [
            {
                "prediccion_numero": pred_class,
                "prediccion_texto": TARGET_LABELS.get(pred_class, "desconocido"),
                "certeza": round(confidence, 4),
            }
        ]
    )


def main() -> None:
    df = load_data(DATA_PATH)
    print("Dataset cargado")
    print(df)
    print()
    print("Distribucion de la variable objetivo:")
    print(df["nivel_satisfaccion"].value_counts().sort_index())

    X = df[["sexo", "edad", "pais"]]
    y = df["nivel_satisfaccion"]

    model = build_pipeline()

    cv = LeaveOneOut()
    scores = cross_val_score(model, X, y, cv=cv)
    predictions = cross_val_predict(model, X, y, cv=cv)

    print()
    print("Accuracy por validacion leave-one-out:")
    print(round(float(scores.mean()), 4))
    print()
    print("Accuracy global:")
    print(round(float(accuracy_score(y, predictions)), 4))
    print()
    print("Matriz de confusion:")
    print(confusion_matrix(y, predictions))
    print()
    print("Reporte de clasificacion:")
    print(
        classification_report(
            y,
            predictions,
            target_names=[TARGET_LABELS[index] for index in sorted(TARGET_LABELS)],
            zero_division=0,
        )
    )

    model.fit(X, y)
    save_model(model, MODEL_PATH)
    print(f"Modelo guardado en: {MODEL_PATH}")

    transformed_df = encode_dataset(model, X, y)
    transformed_df.to_csv(TRANSFORMED_PATH, index=False, encoding="utf-8-sig")
    print(f"Dataset transformado guardado en: {TRANSFORMED_PATH}")

    example_prediction = predict_new_sample(model, sexo="F", edad=30, pais="Chile")
    print()
    print("Prediccion de ejemplo:")
    print(example_prediction)


if __name__ == "__main__":
    main()