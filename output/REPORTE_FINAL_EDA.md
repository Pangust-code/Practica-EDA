# Analisis Exploratorio de Datos - Heart Disease (UCI)

## 1. Descripcion del dataset
- Fuente oficial: https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data
- Numero de observaciones: 303
- Numero de variables (incluyendo Y): 15
- Variable objetivo Y: target (0 sin enfermedad, 1 con enfermedad)
- Proporcion de Y=1 (enfermedad): 45.87%

## 2. Conclusiones del resumen estadistico
- La edad se concentra en adultos medios y mayores, con dispersion moderada.
- oldpeak muestra asimetria y presencia de valores extremos en algunos pacientes.
- thalach presenta variabilidad alta, util para discriminacion de riesgo.

## 3. Conclusiones de visualizacion
- El scatter thalach vs oldpeak evidencia separacion parcial por target.
- El boxplot de colesterol muestra outliers que deben evaluarse, no eliminarse automaticamente.
- La grafica de cp por target sugiere diferencias de distribucion entre clases.

## 4. Conclusiones del analisis de frecuencias
- Existen diferencias en la frecuencia de categorias clinicas entre pacientes con y sin enfermedad.
- sex, cp y exang muestran variaciones importantes por clase objetivo.

## 5. Variables mas correlacionadas con Y
| variable   |   corr_with_target |
|:-----------|-------------------:|
| thal       |           0.522057 |
| ca         |           0.460033 |
| exang      |           0.431894 |

- Estas variables son candidatas principales para modelos de clasificacion posteriores.

## 6. Analisis de outliers
| variable   |    Q1 |    Q3 |   IQR |   lower |   upper |   n_outliers |   outlier_pct |
|:-----------|------:|------:|------:|--------:|--------:|-------------:|--------------:|
| trestbps   | 120   | 140   |  20   |   90    |  170    |            9 |          2.97 |
| oldpeak    |   0   |   1.6 |   1.6 |   -2.4  |    4    |            5 |          1.65 |
| chol       | 211   | 275   |  64   |  115    |  371    |            5 |          1.65 |
| thalach    | 133.5 | 166   |  32.5 |   84.75 |  214.75 |            1 |          0.33 |
| age        |  48   |  61   |  13   |   28.5  |   80.5  |            0 |          0    |

- Decision sugerida: no eliminar todos los outliers clinicos; primero validar si representan casos reales de alto riesgo.

## 7. Manejo de datos faltantes
- Faltantes antes del tratamiento: 6
- Faltantes despues del tratamiento: 0
- Estrategia aplicada: imputacion en ca (mediana) y thal (moda).

## 8. Segmentacion de datos
- Se segmenta por grupos de edad y por sexo para comparar la tasa de enfermedad.
- Los archivos de salida incluyen tablas listas para presentacion.

## 9. Hipotesis iniciales
1. Pacientes con menor thalach y mayor oldpeak tienen mayor probabilidad de enfermedad cardiaca.
2. Ciertas categorias de cp y exang se asocian con mayor tasa de Y=1.
3. Segmentos de mayor edad presentan mayor prevalencia de Y=1 respecto a segmentos jovenes.

## 10. Pasos siguientes
- Preparar conjunto para modelado (train/test) con validacion cruzada.
- Probar modelos de clasificacion y comparar precision, recall y F1.
- Documentar hallazgos en presentacion PDF/PPTX para entrega.
