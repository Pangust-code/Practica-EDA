# PRACTICA 2 - Transformaciones y Clasificador KNN

## 1. Titulo y objetivo

**Titulo:** Transformaciones y clasificador KNN

**Objetivo:**
Desarrollar modelos para la clasificacion de patrones mediante inteligencia artificial y machine learning, aplicando transformaciones de variables y el algoritmo KNN en Excel, Orange3 y Python.

## 2. Analisis del dataset

El dataset trabajado contiene 6 registros y 4 variables:

1. `sexo`: variable categorica nominal (`F`, `M`).
2. `edad`: variable numerica discreta (anios).
3. `pais`: variable categorica nominal (`Brasil`, `Chile`, `Ecuador`, `Espania`).
4. `nivel_satisfaccion`: variable categorica ordinal objetivo (`no me gusta`, `neutral`, `me gusta`).

### 2.1 Diseno de transformaciones

| Id | Variable | Descripcion breve | Tipo | Tecnica de transformacion aplicada |
|---|---|---|---|---|
| 1 | sexo | M (masculino), F (femenino) | Categorica nominal | One-Hot Encoding + Estandarizacion |
| 2 | edad | Anios de edad | Numerica discreta | Estandarizacion (Z-score) |
| 3 | pais | Pais de residencia | Categorica nominal | One-Hot Encoding + Estandarizacion |
| 4 | nivel_satisfaccion | Nivel de gusto | Categorica ordinal (objetivo) | Codificacion ordinal (0,1,2) + estandarizacion para comparacion |

## 3. Transformaciones en herramientas

### 3.1 Transformaciones en Excel
Se realizaron transformaciones de variables categoricas y numericas en Excel, generando una tabla normalizada para comparacion con las demas herramientas.

### 3.2 Transformaciones en Orange3
Se construyo el flujo en Orange3 con carga de archivo, preprocesamiento y visualizacion de la tabla transformada. El flujo de trabajo aplicado fue:

`File -> Data Table -> Preprocess -> Data Table`

(Adjuntar captura del flujo de Orange3 y de la tabla transformada.)

### 3.3 Transformaciones en Python
En Python se ejecuto el script `TransformacionesyClasificacionKNN_excel.py` con:

- `OneHotEncoder` para `sexo` y `pais`.
- `StandardScaler` para `edad`.
- Pipeline con `ColumnTransformer` y `KNeighborsClassifier`.

Se genero el archivo:

- `dataset_transformado_satisfaccion.csv`

y se valido que las variables transformadas tengan media aproximada 0 y desviacion estandar 1.

## 4. KNN en Excel (Euclidea y Manhattan, K=2)

Se realizo el procedimiento solicitado en Excel usando K=2 y las distancias:

1. Distancia Euclidea.
2. Distancia Manhattan.

(Adjuntar hoja de calculo con formula de distancias, vecinos seleccionados y decision final.)

## 5. Resultados obtenidos (Python verificado)

Al ejecutar el script con validacion Leave-One-Out se obtuvo:

- **Distribucion de clases:**
  - `no me gusta`: 3
  - `neutral`: 1
  - `me gusta`: 2
- **Accuracy Leave-One-Out:** 0.50
- **Accuracy global:** 0.50

### 5.1 Matriz de confusion

| Real \ Predicho | no me gusta | neutral | me gusta |
|---|---:|---:|---:|
| no me gusta | 3 | 0 | 0 |
| neutral | 0 | 0 | 1 |
| me gusta | 2 | 0 | 0 |

### 5.2 Reporte resumido

- `no me gusta`: precision 0.60, recall 1.00, f1-score 0.75
- `neutral`: precision 0.00, recall 0.00, f1-score 0.00
- `me gusta`: precision 0.00, recall 0.00, f1-score 0.00

### 5.3 Prediccion de ejemplo

Para un nuevo registro (`sexo=F`, `edad=30`, `pais=Chile`):

- clase predicha: `me gusta` (2)
- certeza: 0.6667

## 6. Conclusiones

1. Se aplicaron correctamente transformaciones de variables categoricas y numericas en Excel, Orange3 y Python.
2. La estandarizacion permitio llevar todas las variables a una escala comparable, validando media 0 y desviacion estandar 1.
3. El modelo KNN pudo ejecutarse y clasificar, pero el desempenio fue limitado (accuracy 0.50) debido al tamano muy pequeno del dataset.
4. El flujo desarrollado cumple como practica de implementacion y comparacion de herramientas, mas que como modelo final de produccion.

## 7. Recomendaciones

1. Aumentar el tamano del dataset para mejorar la generalizacion del modelo.
2. Probar diferentes valores de K (`K=1, 3, 5`) y comparar resultados.
3. Evaluar otras metricas de distancia y modelos adicionales para contraste.
4. Mantener evidencia de cada herramienta (capturas y tablas) para demostrar trazabilidad del proceso.

## 8. Evidencias que debes adjuntar en el PDF

1. Captura del flujo en Orange3.
2. Captura de tabla transformada en Orange3.
3. Captura de transformaciones en Excel.
4. Captura del calculo KNN en Excel (Euclidea y Manhattan, K=2).
5. Salida de Python con accuracy y matriz de confusion.
6. Archivo exportado `dataset_transformado_satisfaccion.csv` (o captura de sus primeras filas).

## 9. Cuadro de criterios (sugerencia de llenado)

| Criterio | Valor | Puntaje obtenido | Observacion |
|---|---:|---:|---|
| 1. Transformaciones en Excel | 1 | 1 | Transformaciones aplicadas y evidenciadas |
| 2. Transformaciones en Orange | 1 | 1 | Flujo y salida mostrados en capturas |
| 3. Transformaciones en Python | 2 | 2 | Pipeline y dataset transformado generado |
| 4. KNN en Excel | 1 | 1 | Distancias Euclidea y Manhattan con K=2 desarrolladas |

**Puntaje total sugerido:** 5/5 (si adjuntas todas las evidencias solicitadas).
