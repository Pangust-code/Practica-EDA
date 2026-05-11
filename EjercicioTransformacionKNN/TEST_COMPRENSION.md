# Test de Comprensión: ¿Entiendes Todo?

Usa este documento para verificar que comprendiste todos los conceptos clave. Si no puedes responder una pregunta, vuelve a leer el archivo markdown correspondiente.

---

## Nivel 1: Conceptos Básicos

### Pregunta 1.1: ¿Qué es KNN?
**Tu respuesta:**

**Respuesta correcta:** (abre EXPLICACION_KNN_PREDICT.md > "Qué es y para qué sirve")

---

### Pregunta 1.2: ¿Por qué el dataset necesita transformación?
**Tu respuesta:**

**Respuesta correcta:** Porque KNN necesita números para calcular distancias, y los datos originales tienen texto (ciudades, niveles de colesterol).

---

### Pregunta 1.3: ¿Cuál es la diferencia entre `fit()` y `transform()`?
**Tu respuesta:**

**Respuesta correcta:** 
- `fit()` aprende la estructura (qué ciudades, media/std de edad).
- `transform()` aplica esa estructura a nuevos datos.

---

### Pregunta 1.4: ¿Qué es distancia euclídea?
**Tu respuesta:**

**Respuesta correcta:** Es la distancia "en línea recta" entre dos puntos multidimensionales. Fórmula: $d = \sqrt{\sum(x_i - y_i)^2}$

---

## Nivel 2: Transformación de Datos

### Pregunta 2.1: ¿Qué es "one-hot encoding"?
**Tu respuesta:**

**Respuesta correcta:** Convertir una categoría en múltiples columnas 0/1. Ej: ciudad "Cuenca" se convierte en [1, 0, 0, 0, 0, 0] para 6 ciudades.

---

### Pregunta 2.2: ¿Cómo se transforma colesterol?
**Tu respuesta:**

**Respuesta correcta:** Se mapea a valores ordinales: bajo → 0, medio → 1, alto → 2, muy alto → 3. Usa un diccionario.

---

### Pregunta 2.3: ¿Cómo se escala edad?
**Tu respuesta:**

**Respuesta correcta:** Se usa estandarización: $edad\_escalada = \frac{edad - media}{desviacion\_estandar}$. Resultado: media 0, desviación 1.

---

### Pregunta 2.4: ¿Por qué NO se escalan las columnas dummy?
**Tu respuesta:**

**Respuesta correcta:** Porque ya están en rango [0, 1]. Escalarlas las pondría fuera de ese rango, lo que no tiene sentido conceptualmente.

---

## Nivel 3: Algoritmo KNN

### Pregunta 3.1: ¿Cuáles son los pasos de `knn_predict()`?
**Tu respuesta:**

**Respuesta correcta:**
1. Calcular distancias a todos los datos de entrenamiento.
2. Ordenar por distancia (menor primero).
3. Tomar los k=3 más cercanos.
4. Obtener sus etiquetas.
5. Votar mayoritariamente.

---

### Pregunta 3.2: ¿Cómo funciona la votación mayoritaria?
**Tu respuesta:**

**Respuesta correcta:** Se toma el promedio de las etiquetas y se redondea. Si promedio ≤ 0.5 → 0, si > 0.5 → 1.

---

### Pregunta 3.3: Si los 3 vecinos tienen etiquetas [1, 0, 0], ¿cuál es la predicción?
**Tu respuesta:**

**Respuesta correcta:** mean([1, 0, 0]) = 0.333, round(0.333) = 0. Predicción = 0.

---

### Pregunta 3.4: ¿Qué significa que un vecino tenga distancia 1.42?
**Tu respuesta:**

**Respuesta correcta:** Que el nuevo paciente es bastante similar a ese vecino (es uno de los más cercanos en el espacio 10-dimensional).

---

## Nivel 4: Código

### Pregunta 4.1: ¿Qué hace `np.argsort(dists)`?
**Tu respuesta:**

**Respuesta correcta:** Devuelve los índices que ordenarían `dists` de menor a mayor. Ej: `dists = [3.28, 1.42, 1.98]` → `argsort = [1, 2, 0]`.

---

### Pregunta 4.2: ¿Qué hace `X_arr - x_arr` en `euclidean_distances()`?
**Tu respuesta:**

**Respuesta correcta:** Resta el nuevo punto de cada fila de X_arr usando broadcasting de numpy. Cada fila se resta independientemente.

---

### Pregunta 4.3: ¿Qué es `axis=1` en `np.sum(..., axis=1)`?
**Tu respuesta:**

**Respuesta correcta:** Suma por filas (no por columnas). Convierte una matriz (6, 10) en un vector (6,).

---

### Pregunta 4.4: ¿Por qué usar `df.copy()` en `transform()`?
**Tu respuesta:**

**Respuesta correcta:** Para no modificar el DataFrame original. Si no copias, los cambios afectan al dataframe de entrada.

---

## Nivel 5: Interpretación de Resultados

### Pregunta 5.1: El programa imprime:
```
Distancias calculadas a cada vecino (k=3):
[1.4194070602392845, 1.7584019781059879, 1.9854092197973214]

Vecinos seleccionados (índices):
[1, 4, 2]

Predicción final: 0
```
**¿Qué significa esto?**

**Tu respuesta:**

**Respuesta correcta:** 
- Los 3 pacientes más cercanos son los índices 1, 4 y 2.
- Están a distancias 1.42, 1.76 y 1.99 respectivamente.
- La votación mayoritaria predice 0 (no diabetes).
- Esto significa que 2 o más de los 3 vecinos no tienen diabetes.

---

### Pregunta 5.2: ¿Cómo verificarías que la predicción es correcta?
**Tu respuesta:**

**Respuesta correcta:** Ver los registros de los vecinos y su etiqueta. Si 2 tienen diabetes=0 y 1 tiene diabetes=1, entonces la votación correcta es 0.

---

### Pregunta 5.3: Si cambiaras k=3 a k=5, ¿qué podría cambiar?
**Tu respuesta:**

**Respuesta correcta:** La predicción podría cambiar porque usarías 5 vecinos en lugar de 3. La votación resultaría diferente.

---

## Nivel 6: Conceptos Avanzados

### Pregunta 6.1: ¿Qué es `ddof=0` en `.std(ddof=0)`?
**Tu respuesta:**

**Respuesta correcta:** Parámetro de pandas que usa desviación estándar poblacional (divide entre n, no n-1). Coincide con StandardScaler de sklearn.

---

### Pregunta 6.2: ¿Por qué no se puede usar `fit()` en el conjunto de prueba?
**Tu respuesta:**

**Respuesta correcta:** Porque causarías data leakage: los parámetros del transformador (media, columnas) se calcularían incluyendo datos de prueba, que NO deberían influir.

---

### Pregunta 6.3: ¿Cómo se comporta el código si un nuevo paciente es de una ciudad que no existía en entrenamiento?
**Tu respuesta:**

**Respuesta correcta:** Se crea una columna para esa ciudad (con 0), luego se rellena con 0 todas las ciudades del entrenamiento. Esa ciudad nueva se ignora efectivamente.

---

### Pregunta 6.4: ¿Qué es broadcasting en numpy?
**Tu respuesta:**

**Respuesta correcta:** Mecanismo donde numpy automáticamente expande arrays de diferentes formas para operaciones. Ej: restar un vector (1, 10) de una matriz (6, 10) resta el vector de cada fila.

---

## Nivel 7: Debugging

### Pregunta 7.1: Código falla con "TypeError: loop of ufunc does not support argument 0 of type float". ¿Por qué?
**Tu respuesta:**

**Respuesta correcta:** Porque numpy está intentando hacer operaciones en tipos de datos incorrectos (object en lugar de float). Solución: convertir con `np.asarray(..., dtype=float)`.

---

### Pregunta 7.2: Obtienes K vecinos pero con índices raros. ¿Qué podrías revisar?
**Tu respuesta:**

**Respuesta correcta:** 
- ¿Están ordenadas correctamente las distancias?
- ¿Se está usando `[:k]` correctamente?
- ¿El transformador está siendo aplicado de la misma forma para entrenamiento y prueba?

---

### Pregunta 7.3: La predicción nunca cambia aunque cambies el nuevo paciente. ¿Por qué?
**Tu respuesta:**

**Respuesta correcta:** Posiblemente:
- El transformador no se re-ajusta entre pacientes (correcto, es lo esperado).
- O hay un error en cómo se transforma el nuevo paciente.

---

## Autotest: Implementación

### Pregunta A.1: ¿Podrías escribir `euclidean_distances()` desde cero?
**Intenta:**

```python
def euclidean_distances(X, x_new):
    # Tu código aquí
    pass
```

**Respuesta correcta:** (compara con el archivo)

---

### Pregunta A.2: ¿Podrías escribir la votación mayoritaria sin ver el código?
**Intenta:**

```python
def votacion_mayoritaria(votes):
    # Tu código aquí
    pass
```

**Respuesta correcta:** `int(np.round(np.mean(votes)))`

---

### Pregunta A.3: ¿Podrías cambiar el script para usar k=7 en lugar de k=3?
**Intenta: ¿Dónde cambiarías qué línea?**

---

## Puntuación

Cuenta cuántas preguntas respondiste correctamente:

- **20-26 correctas:** ¡Excelente! Entiendes profundamente KNN. 🌟
- **14-19 correctas:** Muy bien. Entiende los conceptos clave, pero repasa detalles. ✅
- **8-13 correctas:** Bien. Los conceptos básicos están claros, pero necesitas reforzar detalles. 📖
- **0-7 correctas:** Regresa a la documentación y relee los archivos markdown. No es problema, estos conceptos son complejos. 📚

---

## Pasos Siguientes

### Si puntuaste < 14:
1. Relee [EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md).
2. Relee [EXPLICACION_KNN_PREDICT.md](EXPLICACION_KNN_PREDICT.md).
3. Ejecuta el script paso a paso y ve los valores intermedios con `print()`.

### Si puntuaste 14-19:
1. Repasa [EXPLICACION_EUCLIDEAN_DISTANCES.md](EXPLICACION_EUCLIDEAN_DISTANCES.md).
2. Intenta los ejercicios de implementación (Autotest).
3. Modifica el script (ej: k=5, nuevo paciente).

### Si puntuaste 20-26:
1. Considera:
   - Guardar el transformador con pickle.
   - Comparar con sklearn KNeighborsClassifier.
   - Agregar validación cruzada.
   - Mejorar el manejo de errores.

---

## Recursos para Profundizar

| Tema | Recurso |
|------|---------|
| Machine Learning básico | https://scikit-learn.org/stable/modules/neighbors.html |
| Numpy | https://numpy.org/doc/stable/ |
| Pandas | https://pandas.pydata.org/docs/ |
| One-hot encoding | Busca "one-hot encoding" en Google |
| Estandarización | Busca "standardization machine learning" |

---

**¡Éxito en tu aprendizaje!** 🚀
