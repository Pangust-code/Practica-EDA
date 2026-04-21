import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MultipleLocator, PercentFormatter

DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")


def ensure_dirs() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PLOTS_DIR, exist_ok=True)


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_URL)
    for col in ["Age", "Fare", "Pclass", "SibSp", "Parch", "Survived"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def initial_exploration(df: pd.DataFrame) -> None:
    with open(os.path.join(OUTPUT_DIR, "01_exploracion_inicial.txt"), "w", encoding="utf-8") as f:
        f.write("Exploracion inicial del dataset Titanic\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Fuente: {DATA_URL}\n\n")
        f.write(f"Filas (observaciones): {df.shape[0]}\n")
        f.write(f"Columnas (variables): {df.shape[1]}\n")
        f.write("\nTipos de datos:\n")
        f.write(df.dtypes.to_string())
        f.write("\n\nVariable objetivo Y: Survived (0 no sobrevivio, 1 sobrevivio)\n")

    missing = pd.DataFrame(
        {
            "missing_count": df.isna().sum(),
            "missing_pct": (df.isna().mean() * 100).round(2),
        }
    ).sort_values("missing_pct", ascending=False)
    missing.to_csv(os.path.join(OUTPUT_DIR, "02_valores_faltantes.csv"), encoding="utf-8")

    duplicates = int(df.duplicated().sum())
    with open(os.path.join(OUTPUT_DIR, "03_duplicados.txt"), "w", encoding="utf-8") as f:
        f.write(f"Filas duplicadas: {duplicates}\n")


def statistical_summary(df: pd.DataFrame) -> None:
    stats = df.describe(include="all").T
    stats.to_csv(os.path.join(OUTPUT_DIR, "04_resumen_estadistico.csv"), encoding="utf-8")


def frequency_analysis(df: pd.DataFrame) -> None:
    cat_cols = ["Sex", "Embarked", "Pclass", "Survived"]
    freq_rows = []

    for col in cat_cols:
        if col not in df.columns:
            continue
        vc = df[col].value_counts(dropna=False)
        for k, v in vc.items():
            freq_rows.append({"variable": col, "categoria": k, "frecuencia": int(v)})

    freq_df = pd.DataFrame(freq_rows)
    freq_df.to_csv(os.path.join(OUTPUT_DIR, "05_frecuencias_categoricas.csv"), index=False)


def outlier_analysis_iqr(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ["Age", "Fare", "SibSp", "Parch"]
    rows = []

    for col in numeric_cols:
        if col not in df.columns:
            continue
        series = df[col].dropna()
        if len(series) == 0:
            continue
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        n_out = int(((series < lower) | (series > upper)).sum())
        pct = round((n_out / len(series)) * 100, 2)
        rows.append(
            {
                "variable": col,
                "Q1": q1,
                "Q3": q3,
                "IQR": iqr,
                "lower": lower,
                "upper": upper,
                "n_outliers": n_out,
                "outlier_pct": pct,
            }
        )

    out_df = pd.DataFrame(rows).sort_values("outlier_pct", ascending=False)
    out_df.to_csv(os.path.join(OUTPUT_DIR, "06_outliers_iqr.csv"), index=False)
    return out_df


def missing_data_treatment(df: pd.DataFrame) -> pd.DataFrame:
    treated = df.copy()

    if "Age" in treated.columns and treated["Age"].isna().any():
        treated["Age"] = treated["Age"].fillna(treated["Age"].median())

    if "Embarked" in treated.columns and treated["Embarked"].isna().any():
        treated["Embarked"] = treated["Embarked"].fillna(treated["Embarked"].mode().iloc[0])

    if "Fare" in treated.columns and treated["Fare"].isna().any():
        treated["Fare"] = treated["Fare"].fillna(treated["Fare"].median())

    if "Cabin" in treated.columns and treated["Cabin"].isna().any():
        treated["Cabin"] = treated["Cabin"].fillna("Unknown")

    treated.to_csv(os.path.join(OUTPUT_DIR, "07_dataset_tratado.csv"), index=False)
    return treated


def correlation_analysis(df: pd.DataFrame) -> pd.DataFrame:
    corr = df.corr(numeric_only=True)
    corr.to_csv(os.path.join(OUTPUT_DIR, "08_correlaciones.csv"), encoding="utf-8")

    if "Survived" not in corr.columns:
        top3 = pd.DataFrame(columns=["variable", "corr_with_survived"])
    else:
        target_corr = corr["Survived"].drop(labels=["Survived"], errors="ignore")
        target_corr = target_corr.sort_values(key=lambda s: s.abs(), ascending=False)
        top3 = target_corr.head(3).reset_index()
        top3.columns = ["variable", "corr_with_survived"]

    top3.to_csv(os.path.join(OUTPUT_DIR, "09_top3_correlacion_Y.csv"), index=False)
    return top3


def segmentation_analysis(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    segmented = df.copy()

    if "Age" in segmented.columns:
        segmented["age_group"] = pd.cut(
            segmented["Age"],
            bins=[0, 12, 18, 35, 50, 80],
            labels=["nino", "adolescente", "adulto_joven", "adulto", "mayor"],
            include_lowest=True,
        )
    else:
        segmented["age_group"] = "desconocido"

    by_age = segmented.groupby("age_group", observed=False)["Survived"].mean().reset_index()
    by_age.columns = ["age_group", "survival_rate"]

    by_sex = segmented.groupby("Sex", observed=False)["Survived"].mean().reset_index()
    by_sex.columns = ["sex", "survival_rate"]

    by_age.to_csv(os.path.join(OUTPUT_DIR, "10_segmentacion_age_group.csv"), index=False)
    by_sex.to_csv(os.path.join(OUTPUT_DIR, "11_segmentacion_sex.csv"), index=False)

    return by_age, by_sex


def visualizations(df: pd.DataFrame, corr_df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 4))
    sns.histplot(df["Age"].dropna(), kde=True, bins=20, color="#1f77b4")
    plt.title("Distribucion de edad - Titanic")
    plt.xlabel("Edad")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "01_hist_age.png"), dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived", palette="Set2", alpha=0.85)
    plt.title("Relacion entre Edad y Tarifa por Supervivencia")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "02_scatter_age_fare.png"), dpi=150)
    plt.close()

    plt.figure(figsize=(7, 4))
    sns.countplot(data=df, x="Pclass", hue="Survived", palette="Set1")
    plt.title("Frecuencia de clase de boleto por supervivencia")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "03_bar_pclass_survived.png"), dpi=150)
    plt.close()

    plt.figure(figsize=(8, 4.8))
    sns.pointplot(
        data=df,
        x="Pclass",
        y="Survived",
        hue="Sex",
        estimator=np.mean,
        errorbar=None,
        markers=["o", "o"],
        linestyles=["-", "-"],
        palette={"male": "#1f77b4", "female": "#ff7f0e"},
        order=[1, 2, 3],
    )
    plt.title("Supervivencia por clase y genero")
    plt.xlabel("Clase de boleto (1 = alta, 3 = baja)")
    plt.ylabel("Probabilidad de supervivencia (%)")
    plt.ylim(0, 1)
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    plt.legend(title="Sexo")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "04_line_survival_sex_class.png"), dpi=150)
    plt.close()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, cmap="coolwarm", center=0)
    plt.title("Matriz de correlacion")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "05_heatmap_correlacion.png"), dpi=150)
    plt.close()


def create_datasheet(
    df_raw: pd.DataFrame,
    df_treated: pd.DataFrame,
    outliers: pd.DataFrame,
    top3: pd.DataFrame,
    by_age: pd.DataFrame,
    by_sex: pd.DataFrame,
) -> None:
    report = os.path.join(OUTPUT_DIR, "DATASHEET_TITANIC.md")

    y_rate = round(df_treated["Survived"].mean() * 100, 2)
    missing_before = int(df_raw.isna().sum().sum())
    missing_after = int(df_treated.isna().sum().sum())

    with open(report, "w", encoding="utf-8") as f:
        f.write("# Datasheet del Dataset Titanic\n\n")
        f.write("## 1. Motivacion y contexto\n")
        f.write("Este dataset se usa para analizar factores asociados a la supervivencia de pasajeros del Titanic. ")
        f.write("Es un conjunto de referencia en EDA y clasificacion binaria.\n\n")

        f.write("## 2. Composicion del dataset\n")
        f.write(f"- Fuente: {DATA_URL}\n")
        f.write(f"- Numero de observaciones: {df_raw.shape[0]}\n")
        f.write(f"- Numero de variables: {df_raw.shape[1]}\n")
        f.write("- Variable objetivo Y: Survived (0=no sobrevivio, 1=sobrevivio)\n")
        f.write(f"- Tasa global de supervivencia: {y_rate}%\n\n")

        f.write("## 3. Calidad de datos\n")
        f.write(f"- Valores faltantes antes del tratamiento: {missing_before}\n")
        f.write(f"- Valores faltantes despues del tratamiento: {missing_after}\n")
        f.write("- Estrategias de imputacion: Age mediana, Embarked moda, Fare mediana, Cabin='Unknown'.\n\n")

        f.write("## 4. Variables numericas mas relacionadas con Y\n")
        if len(top3) > 0:
            f.write(top3.to_markdown(index=False))
        else:
            f.write("No se pudo calcular correlacion con Y por falta de columnas numericas compatibles.")
        f.write("\n\n")

        f.write("## 5. Outliers (criterio IQR)\n")
        if len(outliers) > 0:
            f.write(outliers.to_markdown(index=False))
        else:
            f.write("No se detectaron columnas numericas para analisis de outliers.")
        f.write("\n\n")

        f.write("## 6. Segmentacion\n")
        f.write("### 6.1 Por grupo de edad\n")
        f.write(by_age.to_markdown(index=False))
        f.write("\n\n")
        f.write("### 6.2 Por sexo\n")
        f.write(by_sex.to_markdown(index=False))
        f.write("\n\n")

        f.write("## 7. Hipotesis iniciales\n")
        f.write("1. Las mujeres presentan mayor tasa de supervivencia que los hombres.\n")
        f.write("2. La primera clase tiene mayor probabilidad de supervivencia que clases inferiores.\n")
        f.write("3. Ninos y adolescentes tienden a mayor supervivencia que adultos mayores.\n\n")

        f.write("## 8. Limitaciones y uso recomendado\n")
        f.write("- El dataset es historico y no representa poblaciones actuales.\n")
        f.write("- Correlacion no implica causalidad.\n")
        f.write("- Recomendado para aprendizaje de EDA, visualizacion y modelado supervisado basico.\n")


def main() -> None:
    ensure_dirs()
    raw_df = load_data()

    initial_exploration(raw_df)
    statistical_summary(raw_df)
    frequency_analysis(raw_df)
    outlier_df = outlier_analysis_iqr(raw_df)

    treated_df = missing_data_treatment(raw_df)
    top3 = correlation_analysis(treated_df)
    by_age, by_sex = segmentation_analysis(treated_df)

    corr_matrix = treated_df.corr(numeric_only=True)
    visualizations(treated_df, corr_matrix)

    create_datasheet(raw_df, treated_df, outlier_df, top3, by_age, by_sex)

    print("EDA Titanic finalizado correctamente.")
    print("Resultados en:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
