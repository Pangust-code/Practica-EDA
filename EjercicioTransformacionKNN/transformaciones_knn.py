from pathlib import Path
import pandas as pd
import numpy as np
from typing import List, Tuple


class FeatureTransformer:
    """Convierte el DataFrame crudo en la matriz numérica para KNN.

    Uso sencillo:
        tr = FeatureTransformer()
        tr.fit(df_entrenamiento)
        X = tr.transform(df_entrenamiento)
        X_new = tr.transform(df_nuevo)
    """

    def __init__(self):
        self.city_cols: List[str] = []
        self.sex_cols: List[str] = []
        self.edad_mean: float = 0.0
        self.edad_std: float = 1.0
        self.chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}

    def fit(self, df: pd.DataFrame):
        city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
        sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')
        self.city_cols = list(city_dummies.columns)
        self.sex_cols = list(sex_dummies.columns)
        self.edad_mean = float(df['edad'].mean())
        std = float(df['edad'].std(ddof=0))
        self.edad_std = std if std != 0 else 1.0

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['colesterol_ord'] = df['colesterol'].map(self.chol_map).astype(float)
        city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
        sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')
        # asegurar columnas iguales a las del entrenamiento
        for c in self.city_cols:
            if c not in city_dummies:
                city_dummies[c] = 0
        for c in self.sex_cols:
            if c not in sex_dummies:
                sex_dummies[c] = 0
        city_dummies = city_dummies.reindex(sorted(self.city_cols), axis=1)
        sex_dummies = sex_dummies.reindex(sorted(self.sex_cols), axis=1)
        df['edad_scaled'] = (df['edad'] - self.edad_mean) / self.edad_std
        features = pd.concat([
            df[['edad_scaled', 'colesterol_ord']].reset_index(drop=True),
            sex_dummies.reset_index(drop=True),
            city_dummies.reset_index(drop=True)
        ], axis=1)
        return features


def euclidean_distances(X: np.ndarray, x_new: np.ndarray) -> np.ndarray:
    X_arr = np.asarray(X, dtype=float)
    x_arr = np.asarray(x_new, dtype=float)
    diff = X_arr - x_arr
    return np.sqrt(np.sum(diff ** 2, axis=1))


def knn_predict(X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int = 3) -> Tuple[List[int], List[float], int]:
    dists = euclidean_distances(X_train, x_new)
    idx_sorted = np.argsort(dists)
    neighbors_idx = idx_sorted[:k].tolist()
    neighbors_dists = dists[neighbors_idx].tolist()
    y_arr = np.asarray(y_train)
    votes = y_arr[neighbors_idx]
    pred = int(np.round(np.mean(votes)))
    return neighbors_idx, neighbors_dists, pred


def load_dataset(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main():
    base = Path(__file__).parent
    csv_path = base / 'data.csv'
    if not csv_path.exists():
        print(f"No se encuentra {csv_path}. Coloca data.csv en la misma carpeta.")
        return

    df = load_dataset(csv_path)
    df['diabetes_bin'] = df['diabetes'].map({'no': 0, 'si': 1}).astype(int)

    transformer = FeatureTransformer()
    transformer.fit(df)
    X = transformer.transform(df)
    y = df['diabetes_bin'].to_numpy()

    # ejemplo simple: cambiar aquí si quieres probar otros casos
    nuevo = pd.DataFrame([{
        'sexo': 2,
        'ciudad': 'Cuenca',
        'colesterol': 'alto',
        'edad': 50
    }])

    x_new_feat = transformer.transform(nuevo)
    neighbors_idx, neighbors_dists, pred = knn_predict(X.to_numpy(), y, x_new_feat.to_numpy()[0], k=3)

    print('Vecinos (índices):', neighbors_idx)
    print('Distancias:', neighbors_dists)
    print('Predicción (0=no, 1=si):', pred)
    print('\nDetalles de los vecinos:')
    for i in neighbors_idx:
        print(df.iloc[i].to_dict())


if __name__ == '__main__':
    main()
