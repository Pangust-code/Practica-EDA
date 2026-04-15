import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")

COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target_raw",
]


def ensure_dirs() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PLOTS_DIR, exist_ok=True)


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_URL, header=None, names=COLUMNS)
    df = df.replace("?", np.nan)

    # Conversion robusta a numerico para facilitar estadistica y correlaciones
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Variable objetivo Y en binario: 0=sin enfermedad, 1=con enfermedad
    df["target"] = (df["target_raw"] > 0).astype(int)
    return df


def initial_exploration(df: pd.DataFrame) -> None:
    with open(os.path.join(OUTPUT_DIR, "01_exploracion_inicial.txt"), "w", encoding="utf-8") as f:
        f.write("Exploracion inicial del dataset Heart Disease (UCI)\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Fuente: {DATA_URL}\n\n")
        f.write(f"Filas (observaciones): {df.shape[0]}\n")
        f.write(f"Columnas (variables): {df.shape[1]}\n")
        f.write("\nTipos de datos:\n")
        f.write(df.dtypes.to_string())
        f.write("\n\nVariable objetivo Y: target (0 sin enfermedad, 1 con enfermedad)\n")

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
    stats = df.describe(include=["number"]).T
    stats.to_csv(os.path.join(OUTPUT_DIR, "04_resumen_estadistico.csv"), encoding="utf-8")


def frequency_analysis(df: pd.DataFrame) -> None:
    # Variables tratadas como categoricas por definicion de dominio
    cat_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal", "target"]
    freq_rows = []

    for col in cat_cols:
        if col not in df.columns:
            continue
        vc = df[col].value_counts(dropna=False).sort_index()
        for k, v in vc.items():
            freq_rows.append({"variable": col, "categoria": k, "frecuencia": int(v)})

    freq_df = pd.DataFrame(freq_rows)
    freq_df.to_csv(os.path.join(OUTPUT_DIR, "05_frecuencias_categoricas.csv"), index=False)


def outlier_analysis_iqr(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]
    rows = []

    for col in numeric_cols:
        series = df[col].dropna()
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        n_out = int(((series < lower) | (series > upper)).sum())
        pct = round((n_out / len(series)) * 100, 2) if len(series) else 0.0
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

    # Imputacion simple y explicable para variables con faltantes notorios en este dataset
    if treated["ca"].isna().any():
        treated["ca"] = treated["ca"].fillna(treated["ca"].median())
    if treated["thal"].isna().any():
        treated["thal"] = treated["thal"].fillna(treated["thal"].mode().iloc[0])

    treated.to_csv(os.path.join(OUTPUT_DIR, "07_dataset_tratado.csv"), index=False)
    return treated


def correlation_analysis(df: pd.DataFrame) -> pd.DataFrame:
    corr = df.corr(numeric_only=True)
    corr.to_csv(os.path.join(OUTPUT_DIR, "08_correlaciones.csv"), encoding="utf-8")

    excluded = ["target", "target_raw"]
    present = [c for c in excluded if c in corr.columns]
    target_corr = corr["target"].drop(labels=present).sort_values(key=lambda s: s.abs(), ascending=False)
    top3 = target_corr.head(3).reset_index()
    top3.columns = ["variable", "corr_with_target"]
    top3.to_csv(os.path.join(OUTPUT_DIR, "09_top3_correlacion_Y.csv"), index=False)
    return top3


def segmentation_analysis(df: pd.DataFrame) -> pd.DataFrame:
    segmented = df.copy()
    segmented["age_group"] = pd.cut(
        segmented["age"],
        bins=[0, 39, 49, 59, 69, 120],
        labels=["<=39", "40-49", "50-59", "60-69", ">=70"],
    )

    by_age = segmented.groupby("age_group", observed=False)["target"].mean().reset_index()
    by_age.columns = ["age_group", "target_rate"]

    by_sex = segmented.groupby("sex", observed=False)["target"].mean().reset_index()
    by_sex.columns = ["sex", "target_rate"]

    by_age.to_csv(os.path.join(OUTPUT_DIR, "10_segmentacion_age_group.csv"), index=False)
    by_sex.to_csv(os.path.join(OUTPUT_DIR, "11_segmentacion_sex.csv"), index=False)

    return by_age


def visualizations(df: pd.DataFrame, corr_df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")

    # Histograma
    plt.figure(figsize=(8, 4))
    sns.histplot(df["age"].dropna(), kde=True, bins=20, color="#1f77b4")
    plt.title("Distribucion de edad")
    plt.xlabel("Edad")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "01_hist_age.png"), dpi=150)
    plt.close()

    # Scatter
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="thalach", y="oldpeak", hue="target", palette="Set2", alpha=0.85)
    plt.title("Relacion entre thalach y oldpeak por clase objetivo")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "02_scatter_thalach_oldpeak.png"), dpi=150)
    plt.close()

    # Barras categoricas
    plt.figure(figsize=(7, 4))
    sns.countplot(data=df, x="cp", hue="target", palette="Set1")
    plt.title("Frecuencia de tipo de dolor de pecho (cp) por target")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "03_bar_cp_target.png"), dpi=150)
    plt.close()

    # Boxplot outliers
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x="target", y="chol", color="#9ecae1")
    plt.title("Outliers de colesterol por target")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "04_boxplot_chol_target.png"), dpi=150)
    plt.close()

    # Matriz correlacion
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, cmap="coolwarm", center=0)
    plt.title("Matriz de correlacion")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "05_heatmap_correlacion.png"), dpi=150)
    plt.close()


def create_final_report(df_raw: pd.DataFrame, df_treated: pd.DataFrame, outliers: pd.DataFrame, top3: pd.DataFrame) -> None:
    report = os.path.join(OUTPUT_DIR, "REPORTE_FINAL_EDA.md")

    y_rate = round(df_treated["target"].mean() * 100, 2)
    missing_before = int(df_raw.isna().sum().sum())
    missing_after = int(df_treated.isna().sum().sum())

    with open(report, "w", encoding="utf-8") as f:
        f.write("# Analisis Exploratorio de Datos - Heart Disease (UCI)\n\n")
        f.write("## 1. Descripcion del dataset\n")
        f.write(f"- Fuente oficial: {DATA_URL}\n")
        f.write(f"- Numero de observaciones: {df_raw.shape[0]}\n")
        f.write(f"- Numero de variables (incluyendo Y): {df_raw.shape[1]}\n")
        f.write("- Variable objetivo Y: target (0 sin enfermedad, 1 con enfermedad)\n")
        f.write(f"- Proporcion de Y=1 (enfermedad): {y_rate}%\n\n")

        f.write("## 2. Conclusiones del resumen estadistico\n")
        f.write("- La edad se concentra en adultos medios y mayores, con dispersion moderada.\n")
        f.write("- oldpeak muestra asimetria y presencia de valores extremos en algunos pacientes.\n")
        f.write("- thalach presenta variabilidad alta, util para discriminacion de riesgo.\n\n")

        f.write("## 3. Conclusiones de visualizacion\n")
        f.write("- El scatter thalach vs oldpeak evidencia separacion parcial por target.\n")
        f.write("- El boxplot de colesterol muestra outliers que deben evaluarse, no eliminarse automaticamente.\n")
        f.write("- La grafica de cp por target sugiere diferencias de distribucion entre clases.\n\n")

        f.write("## 4. Conclusiones del analisis de frecuencias\n")
        f.write("- Existen diferencias en la frecuencia de categorias clinicas entre pacientes con y sin enfermedad.\n")
        f.write("- sex, cp y exang muestran variaciones importantes por clase objetivo.\n\n")

        f.write("## 5. Variables mas correlacionadas con Y\n")
        f.write(top3.to_markdown(index=False))
        f.write("\n\n")
        f.write("- Estas variables son candidatas principales para modelos de clasificacion posteriores.\n\n")

        f.write("## 6. Analisis de outliers\n")
        f.write(outliers.to_markdown(index=False))
        f.write("\n\n")
        f.write("- Decision sugerida: no eliminar todos los outliers clinicos; primero validar si representan casos reales de alto riesgo.\n\n")

        f.write("## 7. Manejo de datos faltantes\n")
        f.write(f"- Faltantes antes del tratamiento: {missing_before}\n")
        f.write(f"- Faltantes despues del tratamiento: {missing_after}\n")
        f.write("- Estrategia aplicada: imputacion en ca (mediana) y thal (moda).\n\n")

        f.write("## 8. Segmentacion de datos\n")
        f.write("- Se segmenta por grupos de edad y por sexo para comparar la tasa de enfermedad.\n")
        f.write("- Los archivos de salida incluyen tablas listas para presentacion.\n\n")

        f.write("## 9. Hipotesis iniciales\n")
        f.write("1. Pacientes con menor thalach y mayor oldpeak tienen mayor probabilidad de enfermedad cardiaca.\n")
        f.write("2. Ciertas categorias de cp y exang se asocian con mayor tasa de Y=1.\n")
        f.write("3. Segmentos de mayor edad presentan mayor prevalencia de Y=1 respecto a segmentos jovenes.\n\n")

        f.write("## 10. Pasos siguientes\n")
        f.write("- Preparar conjunto para modelado (train/test) con validacion cruzada.\n")
        f.write("- Probar modelos de clasificacion y comparar precision, recall y F1.\n")
        f.write("- Documentar hallazgos en presentacion PDF/PPTX para entrega.\n")


def main() -> None:
    ensure_dirs()
    raw_df = load_data()

    initial_exploration(raw_df)
    statistical_summary(raw_df)
    frequency_analysis(raw_df)
    outlier_df = outlier_analysis_iqr(raw_df)

    treated_df = missing_data_treatment(raw_df)
    top3 = correlation_analysis(treated_df)
    segmentation_analysis(treated_df)

    corr_matrix = treated_df.corr(numeric_only=True)
    visualizations(treated_df, corr_matrix)

    create_final_report(raw_df, treated_df, outlier_df, top3)

    print("EDA finalizado correctamente.")
    print("Resultados en:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
