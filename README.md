# EDA Titanic - Datasheet y analisis exploratorio

Este directorio concentra todo el trabajo realizado sobre el dataset Titanic: analisis exploratorio, limpieza, generacion de tablas de soporte, visualizaciones, datasheet, reporte final y guia para presentacion.

## Objetivo del proyecto

El objetivo fue entender el comportamiento del dataset Titanic desde una perspectiva exploratoria, identificar patrones asociados a la variable objetivo `Survived` y dejar un conjunto de entregables listos para documentar y exponer el analisis.

## Dataset

- Fuente: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Observaciones: 891
- Variables: 12
- Variable objetivo: `Survived` (`0` = no sobrevivio, `1` = sobrevivio)
- Tasa global de supervivencia: 38.38%

## Que se hizo

Durante el proyecto se trabajo en las siguientes etapas:

1. Carga y tipificacion de datos.
2. Revision de valores faltantes y registros duplicados.
3. Estadistica descriptiva de variables numericas y categoricas.
4. Analisis visual con histogramas, scatter plots, barras, lineas y heatmap.
5. Evaluacion de correlaciones con la variable objetivo.
6. Deteccion de outliers mediante IQR.
7. Imputacion de valores faltantes sin perder filas.
8. Segmentacion por grupos de edad y por sexo.
9. Redaccion de un reporte final y un datasheet del dataset.
10. Preparacion de una guia para la presentacion oral o en diapositivas.

## Hallazgos principales

- Antes del tratamiento habia 866 valores faltantes; despues del proceso, quedaron 0.
- No se encontraron duplicados.
- Las variables mas asociadas con `Survived` fueron `Pclass`, `Fare` y `Parch`.
- La supervivencia fue mayor en mujeres que en hombres.
- La supervivencia disminuyo claramente al pasar de primera a tercera clase.
- El grupo de ninos mostro una tasa de supervivencia superior a la de adultos.

## Entregables generados

- `0.2.AnalisisExploratorio_Titanic.py`: script principal con el flujo de analisis.
- `0.2.AnalisisExploratorio_Titanic.ipynb`: version interactiva del analisis.
- `Informe_Guia_Titanic.md`: guia para redactar el informe final.
- `Presentacion_Guia_Titanic.md`: guia para preparar la exposicion.
- `output/DATASHEET_TITANIC.md`: documentacion resumida del dataset.
- `output/REPORTE_FINAL_TITANIC.md`: reporte final del EDA.
- `output/*.csv` y `output/*.txt`: tablas y resumenes de apoyo.
- `output/plots/*.png`: graficas utilizadas en el analisis y la presentacion.
- `Presentacion_Titanic.pptx`: version preliminar de la presentacion.

## Estructura de salida

La carpeta `output` contiene los resultados producidos por el script:

- `01_exploracion_inicial.txt`
- `02_valores_faltantes.csv`
- `03_duplicados.txt`
- `04_resumen_estadistico.csv`
- `05_frecuencias_categoricas.csv`
- `06_outliers_iqr.csv`
- `07_dataset_tratado.csv`
- `08_correlaciones.csv`
- `09_top3_correlacion_Y.csv`
- `10_segmentacion_age_group.csv`
- `11_segmentacion_sex.csv`
- `DATASHEET_TITANIC.md`
- `GUIA_INTERPRETACION_GRAFICAS_TITANIC.md`
- `REPORTE_FINAL_TITANIC.md`

## Como ejecutar el analisis

Desde la raiz del proyecto:

```powershell
.\.venv\Scripts\python.exe .\2.EDA_Titanic_Datasheet\0.2.AnalisisExploratorio_Titanic.py
```

Si usas otro entorno de Python, reemplaza la ruta anterior por la correspondiente a tu instalacion.

## Recomendacion para revisar el trabajo

1. Abrir `output/REPORTE_FINAL_TITANIC.md` para ver el resumen completo.
2. Revisar `output/DATASHEET_TITANIC.md` para consultar la descripcion tecnica del dataset.
3. Usar `Presentacion_Guia_Titanic.md` si vas a exponer el proyecto.
4. Inspeccionar `output/plots/` para validar la lectura visual de los hallazgos.

## Observaciones

El analisis es exploratorio y asociativo, no causal. Los resultados sirven como base para una siguiente etapa de modelado predictivo y validacion con metricas de clasificacion.
