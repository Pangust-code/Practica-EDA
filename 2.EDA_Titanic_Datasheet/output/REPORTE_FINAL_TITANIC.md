# Analisis Exploratorio de Datos - Titanic

## 1. Portada
- Titulo: Analisis exploratorio de datos, extraccion de caracteristicas y presentacion de resultados (Titanic)
- Materia: [Completar]
- Estudiante: [Completar]
- Docente: [Completar]
- Fecha: [Completar]

## 2. Introduccion
El presente trabajo desarrolla un analisis exploratorio de datos sobre un conjunto historico de pasajeros del Titanic. El objetivo es comprender la estructura del dataset, evaluar su calidad, identificar patrones iniciales asociados a la supervivencia y formular hipotesis que orienten etapas posteriores de modelado predictivo.

## 3. Objetivos
- Reforzar fundamentos de analisis exploratorio de datos.
- Aplicar tecnicas de extraccion de caracteristicas a un dataset real.
- Presentar resultados, conclusiones y pasos siguientes.

## 4. Descripcion del dataset
- Fuente oficial: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Numero de observaciones: 891
- Numero de variables: 12
- Variable objetivo Y: Survived (0=no sobrevivio, 1=sobrevivio)
- Proporcion de Y=1 (supervivencia): 38.38%

## 5. Metodologia aplicada
1. Carga y tipificacion de datos.
2. Deteccion de faltantes y duplicados.
3. Estadistica descriptiva.
4. Visualizacion (histograma, scatter, barras de conteo, lineas por sexo/clase y heatmap).
5. Analisis de frecuencias categoricas.
6. Correlacion con Y.
7. Deteccion de outliers por IQR.
8. Imputacion de faltantes (Age mediana, Embarked moda, Fare mediana, Cabin='Unknown').
9. Segmentacion por edad y sexo.
10. Formulacion de hipotesis.

## 6. Resultados principales

### 6.1 Calidad de datos
- Faltantes antes: 866
- Faltantes despues: 0
- Duplicados: 0

### 6.2 Variables mas correlacionadas con Y
| variable | corr_with_survived |
|:--|--:|
| Pclass | -0.338481 |
| Fare | 0.257307 |
| Parch | 0.081629 |

Conclusion breve:
Estas tres variables muestran la mayor asociacion lineal con la variable objetivo y son candidatas prioritarias para modelado.

### 6.3 Outliers
| variable | Q1 | Q3 | IQR | lower | upper | n_outliers | outlier_pct |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Parch | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 213 | 23.91 |
| Fare | 7.9104 | 31.0000 | 23.0896 | -26.7240 | 65.6344 | 116 | 13.02 |
| SibSp | 0.0000 | 1.0000 | 1.0000 | -1.5000 | 2.5000 | 46 | 5.16 |
| Age | 20.1250 | 38.0000 | 17.8750 | -6.6875 | 64.8125 | 11 | 1.54 |

Decision tecnica:
Se recomienda no eliminar automaticamente todos los outliers sin evaluar su contexto, ya que algunos pueden representar perfiles reales de pasajeros y condiciones de viaje.

### 6.4 Segmentacion
- Por edad: el grupo "nino" presenta mayor supervivencia (57.97%).
- Por sexo: las mujeres presentan supervivencia notablemente mayor (74.20%) frente a hombres (18.89%).

## 7. Hipotesis iniciales
1. Las mujeres presentan mayor tasa de supervivencia que los hombres.
2. La primera clase tiene mayor probabilidad de supervivencia que clases inferiores.
3. Ninos y adolescentes tienden a mayor supervivencia que adultos mayores.

## 8. Conclusiones
- El EDA permitio comprender la distribucion y calidad del dataset Titanic.
- La estrategia de imputacion resolvio faltantes sin eliminar registros.
- Se identificaron variables prioritarias (Pclass, Fare, Parch) para clasificacion.
- El analisis de segmentacion refuerza diferencias claras por sexo y grupo de edad.
- El proyecto deja una base lista para modelado supervisado y validacion de hipotesis.

## 9. Recomendaciones
- Ejecutar modelos de clasificacion con validacion cruzada.
- Comparar precision, recall, F1 y AUC.
- Evaluar importancia de variables y estabilidad del modelo.
- Complementar el analisis con ingenieria de caracteristicas (por ejemplo: tamano de familia o titulo del pasajero).

## 10. Evidencias anexas
- output/01_exploracion_inicial.txt
- output/04_resumen_estadistico.csv
- output/05_frecuencias_categoricas.csv
- output/09_top3_correlacion_Y.csv
- output/06_outliers_iqr.csv
- output/10_segmentacion_age_group.csv
- output/11_segmentacion_sex.csv
- output/plots/*.png
- output/DATASHEET_TITANIC.md
