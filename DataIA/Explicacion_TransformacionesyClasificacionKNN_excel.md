# Explicacion del script de transformacion y clasificacion con KNN

## Objetivo

Este material adapta la idea del notebook original a los datos reales del archivo `dataIA.xlsx`. En lugar del dataset bancario amplio del cuaderno, aqui se trabaja con una tabla pequena de 4 columnas:

- `sexo`
- `edad`
- `pais`
- `nivelSatisfaccion`

La variable objetivo es `nivelSatisfaccion`, que representa una clase ordenada. Por eso el ejemplo usa un clasificador KNN y un preprocesamiento sencillo para transformar las variables categoricas y numericas.

## Que hace el script

El archivo [`TransformacionesyClasificacionKNN_excel.py`](TransformacionesyClasificacionKNN_excel.py) realiza este flujo:

1. Carga el Excel con `pandas`.
2. Limpia nombres de columnas y corrige el encabezado del pais si aparece con un caracter mal codificado.
3. Convierte la variable objetivo a valores numericos:
   - `no me gusta` -> 0
   - `neutral` o `neutro` -> 1
   - `me gusta` -> 2
4. Separa variables de entrada y salida.
5. Aplica un `ColumnTransformer`:
   - `OneHotEncoder` para `sexo` y `pais`
   - `StandardScaler` para `edad`
6. Entrena un `KNeighborsClassifier`.
7. Evalua el modelo con `LeaveOneOut`, apropiado para un dataset tan pequeno.
8. Guarda el modelo entrenado en `modelo_knn_satisfaccion.pkl`.
9. Exporta el dataset transformado a `dataset_transformado_satisfaccion.csv`.
10. Genera una prediccion de ejemplo para un nuevo registro.

## Relacion con el notebook original

El notebook original esta orientado a un caso bancario con muchas variables categoricas y numericas. En cambio, el Excel proporcionado es mas pequeno y didactico, por lo que el script se simplifica. Aun asi, conserva la misma idea central:

- transformacion de variables categoricas
- escalado de variables numericas
- uso de un pipeline
- clasificacion con KNN
- prediccion de nuevos datos

La principal diferencia es que aqui la certeza se obtiene con `predict_proba`, que entrega la probabilidad asociada a la clase predicha.

## Estructura del Excel

El archivo de entrada contiene una sola hoja con 6 registros. En la inspeccion del libro se observaron estas columnas:

- `sexo`
- `edad`
- `pa?s` o `pais`
- `nivelSatisfaccion`

El script normaliza el nombre de la columna de pais para que el proceso sea estable aunque el archivo tenga problemas de codificacion.

## Requisitos

El script usa estas librerias:

- `pandas`
- `numpy`
- `scikit-learn`
- `openpyxl` para leer el Excel

## Como ejecutar

Desde la carpeta `DataIA`, ejecuta:

```bash
python TransformacionesyClasificacionKNN_excel.py
```

## Salidas generadas

Al correr el script se obtienen estos archivos:

- `modelo_knn_satisfaccion.pkl`
- `dataset_transformado_satisfaccion.csv`

Tambien se imprime en consola:

- resumen del dataset
- accuracy con validacion leave-one-out
- matriz de confusion
- reporte de clasificacion
- prediccion de ejemplo

## Nota metodologica

Con solo 6 filas, este ejemplo sirve como demostracion de flujo de trabajo, no como modelo listo para produccion. El interes principal es mostrar como organizar la transformacion de datos y la clasificacion con KNN de forma reproducible.