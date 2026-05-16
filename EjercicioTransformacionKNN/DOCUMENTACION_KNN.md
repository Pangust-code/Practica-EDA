# Documentación resumida y amigable — Transformaciones y KNN

Este archivo reúne lo esencial del proyecto en lenguaje sencillo, con pasos para ejecutar y entender el código si no eres experto en Python.

## Propósito
- Implementar K-Nearest Neighbors (KNN) sin usar sklearn para aprender el algoritmo.
- Transformar datos crudos (sexo, ciudad, colesterol, edad) a números para calcular distancias.

## Archivos importantes
- Data: `data.csv` (datos de ejemplo). 
- Script: [EjercicioTransformacionKNN/transformaciones_knn.py](EjercicioTransformacionKNN/transformaciones_knn.py)
- Documentación (esta): [EjercicioTransformacionKNN/DOCUMENTACION_KNN.md](EjercicioTransformacionKNN/DOCUMENTACION_KNN.md)

## Resumen de las transformaciones
- `colesterol`: mapeo ordinal: `bajo->0, medio->1, alto->2, muy alto->3`.
- `sexo`: one-hot (por ejemplo `sexo_1`, `sexo_2`).
- `ciudad`: one-hot (una columna por ciudad presente en entrenamiento).
- `edad`: estandarizada: `(edad - media_entrenamiento) / std_entrenamiento`.

Nota: guardamos la estructura aprendida en `fit()` (qué columnas one-hot existen y media/std de edad) y la aplicamos igual en `transform()`.

## Funciones principales (explicación simple)
- `FeatureTransformer.fit(df)`: mira los datos de entrenamiento y aprende las columnas y estadísticas necesarias.
- `FeatureTransformer.transform(df)`: aplica las mismas transformaciones a un DataFrame (entrenamiento o nuevos casos).
- `euclidean_distances(X, x_new)`: calcula la distancia euclídea entre `x_new` y cada fila de `X`.
- `knn_predict(X_train, y_train, x_new, k=3)`: encuentra los `k` vecinos más cercanos y decide por votación (0/1).

## Cómo ejecutar (rápido)
1. Abrir una terminal en la carpeta `EjercicioTransformacionKNN`.
2. Ejecutar:

```bash
python EjercicioTransformacionKNN/transformaciones_knn.py
```

Salida esperada: lista de vecinos (índices), distancias y la predicción final (0=no, 1=si). El script muestra también los registros originales de los vecinos.

## Ejemplo de uso en el script
- El `main()` del script carga `data.csv`, transforma todo, crea un paciente nuevo de ejemplo y muestra la predicción con `k=3`.

## Sugerencias para principiantes
- Para cambiar el paciente a predecir, edita el diccionario en `main()` o crea tu propio DataFrame con el mismo formato de columnas: `sexo, ciudad, colesterol, edad`.
- Para cambiar `k`, modifica el argumento `k` en la llamada a `knn_predict(...)`.

## Qué hice en este repo
- Consolidé la documentación en este único archivo legible.
- Simplifiqué y aclaré el script principal para que sea fácil de leer.
- Eliminé documentos MD explicativos redundantes para evitar confusión.

---
Si quieres que deje copias de los MD detallados en otra carpeta (por ejemplo `docs/`), o que ejecute el script y te pegue la salida aquí, dímelo y lo hago.
