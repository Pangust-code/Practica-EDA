# Datasheet del Dataset Titanic

## 1. Motivacion y contexto
Este dataset se usa para analizar factores asociados a la supervivencia de pasajeros del Titanic. Es un conjunto de referencia en EDA y clasificacion binaria.

## 2. Composicion del dataset
- Fuente: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Numero de observaciones: 891
- Numero de variables: 12
- Variable objetivo Y: Survived (0=no sobrevivio, 1=sobrevivio)
- Tasa global de supervivencia: 38.38%

## 3. Calidad de datos
- Valores faltantes antes del tratamiento: 866
- Valores faltantes despues del tratamiento: 0
- Estrategias de imputacion: Age mediana, Embarked moda, Fare mediana, Cabin='Unknown'.

## 4. Variables numericas mas relacionadas con Y
| variable   |   corr_with_survived |
|:-----------|---------------------:|
| Pclass     |           -0.338481  |
| Fare       |            0.257307  |
| Parch      |            0.0816294 |

## 5. Outliers (criterio IQR)
| variable   |      Q1 |   Q3 |     IQR |    lower |   upper |   n_outliers |   outlier_pct |
|:-----------|--------:|-----:|--------:|---------:|--------:|-------------:|--------------:|
| Parch      |  0      |    0 |  0      |   0      |  0      |          213 |         23.91 |
| Fare       |  7.9104 |   31 | 23.0896 | -26.724  | 65.6344 |          116 |         13.02 |
| SibSp      |  0      |    1 |  1      |  -1.5    |  2.5    |           46 |          5.16 |
| Age        | 20.125  |   38 | 17.875  |  -6.6875 | 64.8125 |           11 |          1.54 |

## 6. Segmentacion
### 6.1 Por grupo de edad
| age_group    |   survival_rate |
|:-------------|----------------:|
| nino         |        0.57971  |
| adolescente  |        0.428571 |
| adulto_joven |        0.353271 |
| adulto       |        0.398693 |
| mayor        |        0.34375  |

### 6.2 Por sexo
| sex    |   survival_rate |
|:-------|----------------:|
| female |        0.742038 |
| male   |        0.188908 |

## 7. Hipotesis iniciales
1. Las mujeres presentan mayor tasa de supervivencia que los hombres.
2. La primera clase tiene mayor probabilidad de supervivencia que clases inferiores.
3. Ninos y adolescentes tienden a mayor supervivencia que adultos mayores.

## 8. Limitaciones y uso recomendado
- El dataset es historico y no representa poblaciones actuales.
- Correlacion no implica causalidad.
- Recomendado para aprendizaje de EDA, visualizacion y modelado supervisado basico.
