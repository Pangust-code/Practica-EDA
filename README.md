# Practica EDA (segun Word) - Heart Disease UCI

Este proyecto fue rehecho desde cero y sigue la guia del documento Word:

- Titulo: Analisis exploratorio de datos, extraccion de caracteristicas y presentacion de resultados.
- Base metodologica: estructura y estilo de las guias 0.1 y 0.2 del repositorio de referencia.
- Dataset distinto y real: Heart Disease (UCI).

## Dataset usado (real y verificable)

- URL oficial de datos:
  https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data
- Repositorio UCI del dataset:
  https://archive.ics.uci.edu/dataset/45/heart+disease

## Archivos del proyecto

- 0.1.AprendiendoPythonFundamentos.py
  - Repaso breve de fundamentos Python solicitados en la guia.
- 0.2.AnalisisExploratorio_HeartDisease.py
  - Script principal del analisis exploratorio completo.
- requirements.txt
  - Dependencias.
- output/
  - Evidencias generadas (tablas, reporte final y figuras).

## Actividades del Word cubiertas

1. Carga de datos:
- Se carga el dataset UCI desde URL oficial.

2. Exploracion inicial:
- Tamano, tipos, faltantes, duplicados y variable objetivo Y.

3. Resumen estadistico:
- Estadisticas descriptivas completas y conclusiones en reporte.

4. Visualizacion:
- Histograma, scatter, barras, boxplot y heatmap.

5. Variables categoricas:
- Frecuencias por categorias en archivo dedicado.

6. Correlacion con Y:
- Matriz y top 3 variables mas correlacionadas con target.

7. Manejo de faltantes:
- Imputacion explicita de ca (mediana) y thal (moda).

8. Outliers:
- Deteccion por IQR y recomendacion justificada en reporte.

9. Segmentacion:
- Segmentacion por grupos de edad y por sexo.

10. Hipotesis:
- Se incluyen hipotesis iniciales basadas en hallazgos.

11. Presentacion de resultados:
- REPORTE_FINAL_EDA.md + guia de presentacion en Presentacion_Guia.md.

## Dependencias

Instalar (en tu .venv):

    .\.venv\Scripts\python.exe -m pip install -r .\1.EDA_Heart_Disease_UCI\requirements.txt

## Ejecucion

Desde la carpeta IA:

    .\.venv\Scripts\python.exe .\1.EDA_Heart_Disease_UCI\0.2.AnalisisExploratorio_HeartDisease.py

## Salidas generadas

Dentro de 1.EDA_Heart_Disease_UCI/output:

- 01_exploracion_inicial.txt
- 02_valores_faltantes.csv
- 03_duplicados.txt
- 04_resumen_estadistico.csv
- 05_frecuencias_categoricas.csv
- 06_outliers_iqr.csv
- 07_dataset_tratado.csv
- 08_correlaciones.csv
- 09_top3_correlacion_Y.csv
- 10_segmentacion_age_group.csv
- 11_segmentacion_sex.csv
- REPORTE_FINAL_EDA.md
- plots/01_hist_age.png
- plots/02_scatter_thalach_oldpeak.png
- plots/03_bar_cp_target.png
- plots/04_boxplot_chol_target.png
- plots/05_heatmap_correlacion.png

## Resultado clave para la rubrica

Top 3 variables mas correlacionadas con Y (target):
- thal
- ca
- exang

Estas variables ya estan exportadas en output/09_top3_correlacion_Y.csv.

## Nota sobre la limpieza solicitada

Se elimino todo lo anterior del workspace y se reconstruyo solo esta practica desde cero (manteniendo .venv y el archivo Word original).# Practica-EDA
