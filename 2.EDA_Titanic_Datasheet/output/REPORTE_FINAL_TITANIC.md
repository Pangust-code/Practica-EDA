# Informe Final - Analisis Exploratorio de Datos Titanic

## 1. Portada
- Titulo de la practica: Analisis exploratorio de datos, extraccion de caracteristicas y presentacion de resultados
- Materia: Inteligencia Artificial
- Estudiantes: Est. Valeria Mantilla y Daniel Guanga
- Docente: Ing. Remigio Hurtado

## 2. Introduccion
El presente trabajo desarrolla un analisis exploratorio de datos sobre el dataset Titanic. El objetivo es comprender su estructura, evaluar la calidad de los datos, identificar factores asociados a la supervivencia y plantear hipotesis para etapas posteriores de modelado.

## 3. Objetivos
- Reforzar fundamentos de analisis exploratorio de datos.
- Aplicar tecnicas de extraccion de caracteristicas en un dataset real.
- Presentar resultados, conclusiones y pasos siguientes.

## 4. Descripcion del dataset
- Fuente oficial del CSV: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Numero de observaciones: 891
- Numero de variables: 12
- Definicion de Y: Survived (0 no sobrevivio, 1 sobrevivio)
- Proporcion de Y=1: 38.38%

## 5. Metodologia aplicada
1. Carga y tipificacion de datos.
2. Deteccion de faltantes y duplicados.
3. Estadistica descriptiva.
4. Visualizacion (histograma, scatter, barras de conteo, lineas por sexo/clase y heatmap).
5. Analisis de frecuencias categoricas.
6. Correlacion con Y.
7. Deteccion de outliers por IQR.
8. Imputacion de faltantes.
9. Segmentacion por edad y sexo.
10. Formulacion de hipotesis.

## 6. Resultados principales

### 6.1 Calidad de datos
- Faltantes antes: 866
- Faltantes despues: 0
- Duplicados: 0

### 6.2 Correlaciones con Y
| variable | corr_with_survived |
|:--|--:|
| Pclass | -0.338481 |
| Fare | 0.257307 |
| Parch | 0.081629 |

Estas tres variables muestran la mayor asociacion lineal con la variable objetivo y son candidatas prioritarias para modelado.

### 6.3 Outliers
| variable | Q1 | Q3 | IQR | lower | upper | n_outliers | outlier_pct |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Parch | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 213 | 23.91 |
| Fare | 7.9104 | 31.0000 | 23.0896 | -26.7240 | 65.6344 | 116 | 13.02 |
| SibSp | 0.0000 | 1.0000 | 1.0000 | -1.5000 | 2.5000 | 46 | 5.16 |
| Age | 20.1250 | 38.0000 | 17.8750 | -6.6875 | 64.8125 | 11 | 1.54 |

Se recomienda no eliminar automaticamente los outliers sin evaluar su contexto.

### 6.4 Segmentacion
- Por grupo de edad: el grupo nino presenta mayor tasa de supervivencia (57.97%).
- Por sexo: las mujeres muestran mayor supervivencia (74.20%) frente a los hombres (18.89%).

## 7. Hipotesis iniciales
1. Las mujeres presentan mayor supervivencia que los hombres.
2. La primera clase presenta mayor supervivencia que clases inferiores.
3. Ninos y adolescentes tienden a mayor supervivencia que adultos mayores.

## 8. Conclusiones
- El EDA permitio entender distribucion y calidad de datos.
- La imputacion resolvio faltantes sin perder observaciones.
- Se identificaron variables prioritarias para clasificacion.
- La segmentacion respalda diferencias relevantes entre grupos.
- El proyecto deja una base lista para modelado supervisado.

## 9. Recomendaciones
- Ejecutar modelos de clasificacion con validacion cruzada.
- Comparar precision, recall, F1 y AUC.
- Analizar importancia de variables y estabilidad del modelo.

## 10. Evidencias a anexar
- output/DATASHEET_TITANIC.md
- output/REPORTE_FINAL_TITANIC.md
- output/04_resumen_estadistico.csv
- output/05_frecuencias_categoricas.csv
- output/09_top3_correlacion_Y.csv
- output/06_outliers_iqr.csv
- output/10_segmentacion_age_group.csv
- output/11_segmentacion_sex.csv
- output/plots/*.png

## 11. Explicacion del codigo

### 11.1 Estructura general del pipeline
El notebook y el script comparten la misma logica. El flujo principal ejecuta: carga de datos, exploracion inicial, resumen estadistico, analisis de frecuencias, analisis de outliers, tratamiento de faltantes, correlaciones, segmentacion, visualizaciones y generacion del datasheet final.

### 11.2 Funciones clave
- `ensure_dirs()`: crea carpetas de salida (`output` y `output/plots`).
- `load_data()`: descarga el CSV y convierte columnas numericas con control de errores.
- `initial_exploration()`: documenta dimensiones, tipos de dato, faltantes y duplicados.
- `statistical_summary()`: genera estadistica descriptiva global en CSV.
- `frequency_analysis()`: calcula frecuencias de variables categoricas.
- `outlier_analysis_iqr()`: estima limites inferior y superior por IQR para detectar valores atipicos.
- `missing_data_treatment()`: aplica imputacion (mediana/moda/Unknown) y guarda el dataset tratado.
- `correlation_analysis()`: construye matriz de correlacion y extrae el top 3 con mayor asociacion a `Survived`.
- `segmentation_analysis()`: compara supervivencia por grupos de edad y sexo.
- `visualizations()`: crea 5 graficas para soporte interpretativo.
- `create_datasheet()`: integra hallazgos en un documento Markdown trazable.

### 11.3 Criterios tecnicos usados
- Outliers por IQR: se define un dato atipico fuera del rango $[Q1 - 1.5 \times IQR,\ Q3 + 1.5 \times IQR]$.
- Correlacion: se usa correlacion lineal sobre variables numericas para priorizar candidatas a modelado.
- Imputacion: se privilegia no perder observaciones en una etapa exploratoria.

### 11.4 Buenas practicas incluidas
- Exportacion de evidencias por etapa para trazabilidad.
- Separacion en funciones pequenas para facilitar mantenimiento.
- Reproducibilidad mediante ejecucion secuencial del pipeline.
