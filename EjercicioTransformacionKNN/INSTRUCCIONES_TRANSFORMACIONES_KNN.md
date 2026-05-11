# Instrucciones y explicación - Transformaciones y KNN

Resumen breve:
- Carga `data.csv` con columnas `sexo, ciudad, colesterol, edad, diabetes`.
- Transformaciones: codificar `ciudad` y `sexo` como dummies, mapear `colesterol` como ordinal, mapear `diabetes` a 0/1.
- Escalado: estandarizar `edad` (media 0, desviación 1) usando la media y std del conjunto de entrenamiento.
- KNN: implementación manual (sin usar sklearn KNeighbors). Distancia euclídea, k=3.

Pasos detallados para reproducir:
1. Coloca `data.csv` en la carpeta `EjercicioTransformacionKNN` (ya está incluido en el repositorio).
2. Ejecuta el script `transformaciones_knn.py` con el intérprete de Python del entorno (recomiendo el `.venv` del proyecto):

```bash
python EjercicioTransformacionKNN/transformaciones_knn.py
```

Qué hace el script (resumen técnico):
- `FeatureTransformer.fit(df)`: calcula las columnas de dummies para `ciudad` y `sexo`, y guarda la media y desviación estándar de `edad`.
- `FeatureTransformer.transform(df)`: aplica las mismas transformaciones a nuevos datos: mapea `colesterol` a ordinal, crea dummies (rellena columnas faltantes con 0), y escala `edad` con la media/std guardadas.
- `knn_predict(...)`: calcula distancias euclídeas entre el nuevo punto y todas las instancias, ordena y selecciona los `k=3` vecinos más cercanos, y decide por votación mayoritaria.

Notas pedagógicas y recomendaciones:
- Es importante usar el mismo transformador (mismas columnas y parámetros) al transformar nuevos ejemplos; por eso `fit` y `transform` están separados.
- No se debe estandarizar variables dummy (one-hot). En este script solo se escala `edad`.
- `colesterol` se transforma como ordinal porque existe un orden natural: `bajo < medio < alto < muy alto`.
- El script instala en tiempo de ejecución dependencias (`pandas`, `numpy`, `scikit-learn`) si faltan, para facilitar ejecución en entornos limpios.

Salida esperada:
- Lista con las distancias a los 3 vecinos más cercanos.
- Índices de los vecinos seleccionados y sus registros originales.
- Predicción final `0` (no) o `1` (si).

Si quieres, puedo:
- Ejecutar el script aquí y mostrar la salida del ejemplo de prueba.
- Guardar el transformador en disco (`pickle`) para uso futuro.
