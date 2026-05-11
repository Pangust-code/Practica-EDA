# Explicación de `knn_predict`

## Qué es y para qué sirve

Esta función implementa el **algoritmo K-Nearest Neighbors manualmente** (sin usar sklearn).

**Su objetivo:** Dada una distancia a cada paciente de entrenamiento, encuentra los `k` vecinos más cercanos y decide si el nuevo paciente tiene diabetes o no mediante votación mayoritaria.

**En palabras simples:**
1. Ordena los pacientes por distancia (del más cercano al más lejano).
2. Toma los `k=3` más cercanos.
3. Mira si esos 3 tienen o no diabetes.
4. Si 2 o más dicen "sí", predice "sí". Si 2 o más dicen "no", predice "no".

---

## El código

```python
def knn_predict(X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int = 3) -> Tuple[List[int], List[float], int]:
    dists = euclidean_distances(X_train, x_new)
    idx_sorted = np.argsort(dists)
    neighbors_idx = idx_sorted[:k].tolist()
    neighbors_dists = dists[neighbors_idx].tolist()
    y_arr = np.asarray(y_train)
    votes = y_arr[neighbors_idx]
    # majority vote (ties -> choose 1 if tie and more 1s? here simple sum)
    pred = int(np.round(np.mean(votes)))
    return neighbors_idx, neighbors_dists, pred
```

### Explicación línea por línea

#### Línea 1: `def knn_predict(X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int = 3) -> Tuple[List[int], List[float], int]:`

**Parámetros:**
- `X_train`: matriz de características del entrenamiento. Forma: `(n_pacientes, n_características)`.
- `y_train`: etiquetas (0 o 1) del entrenamiento. Forma: `(n_pacientes,)`.
  - 0 = no diabetes
  - 1 = sí diabetes
- `x_new`: características del nuevo paciente. Forma: `(n_características,)`.
- `k`: número de vecinos a considerar. Por defecto 3.

**Retorno:**
- `Tuple[List[int], List[float], int]` significa una tupla con 3 elementos:
  - `List[int]`: índices de los vecinos.
  - `List[float]`: distancias a esos vecinos.
  - `int`: predicción (0 o 1).

#### Línea 2: `dists = euclidean_distances(X_train, x_new)`

- **Qué hace:** Calcula la distancia del nuevo paciente a TODOS los pacientes de entrenamiento.
- **Resultado:** Array de distancias. Ejemplo: `[3.28, 1.42, 1.98, 2.05, 1.55, 2.30]`.
- **Tamaño:** `(n_pacientes,)` ej: (6,).

#### Línea 3: `idx_sorted = np.argsort(dists)`

- **Qué hace:** Ordena las distancias de menor a mayor y devuelve los índices.
- **`np.argsort`:** "argsort" = "argument sort". Devuelve los índices que ordenarían el array.

**Ejemplo:**
```python
dists = [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]
         # 0    1    2    3    4    5

Después de np.argsort:
idx_sorted = [1, 4, 2, 3, 5, 0]

Por qué:
- Índice 1 tiene distancia 1.42 (más pequeño)
- Índice 4 tiene distancia 1.55 (segundo más pequeño)
- Índice 2 tiene distancia 1.98
- Índice 3 tiene distancia 2.05
- Índice 5 tiene distancia 2.30
- Índice 0 tiene distancia 3.28 (más grande)
```

#### Línea 4: `neighbors_idx = idx_sorted[:k].tolist()`

- **`idx_sorted[:k]`:** Toma los primeros `k` elementos del array ordenado.
  - Si `k=3`, toma los primeros 3 (los más cercanos).
- **`.tolist()`:** Convierte el array numpy a una lista de Python.

**Ejemplo (con k=3):**
```python
idx_sorted = [1, 4, 2, 3, 5, 0]
neighbors_idx = [1, 4, 2]
```

**Significado:** Los 3 vecinos más cercanos son los pacientes en posiciones 1, 4 y 2 del conjunto de entrenamiento.

#### Línea 5: `neighbors_dists = dists[neighbors_idx].tolist()`

- **`dists[neighbors_idx]`:** Obtiene las distancias correspondientes a esos índices.
- **`.tolist()`:** Convierte a lista.

**Ejemplo:**
```python
dists = [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]
neighbors_idx = [1, 4, 2]

neighbors_dists = [dists[1], dists[4], dists[2]]
                = [1.42, 1.55, 1.98]
```

#### Línea 6: `y_arr = np.asarray(y_train)`

- **Qué hace:** Convierte `y_train` a array numpy si no lo es ya.
- **Por qué:** Para poder indexar con `neighbors_idx`.

#### Línea 7: `votes = y_arr[neighbors_idx]`

- **Qué hace:** Obtiene las etiquetas (0 o 1) de los 3 vecinos más cercanos.
- **Indexing:** Usa los índices guardados en `neighbors_idx`.

**Ejemplo:**
```python
y_train = [0, 1, 0, 1, 0, 1]
           # 0  1  2  3  4  5

neighbors_idx = [1, 4, 2]

votes = [y_train[1], y_train[4], y_train[2]]
      = [1, 0, 0]
```

**Significado:** El vecino 1 tiene diabetes (1), el vecino 4 no (0), el vecino 2 no (0).

#### Línea 8: `pred = int(np.round(np.mean(votes)))`

Esto funciona en tres partes:

**Parte 1: `np.mean(votes)`**
- Calcula el promedio de las etiquetas.
- Ejemplo: `np.mean([1, 0, 0]) = 1/3 ≈ 0.333`.

**Parte 2: `np.round(...)`**
- Redondea al entero más cercano.
- Ejemplo: `np.round(0.333) = 0`, `np.round(0.666) = 1`.

**Parte 3: `int(...)`**
- Convierte el resultado a un entero de Python.

**Lógica:**
- Si el promedio es ≤ 0.5, redondea a 0 (no diabetes).
- Si el promedio es > 0.5, redondea a 1 (sí diabetes).

**Ejemplos:**
```python
votes = [0, 0, 0]  → mean = 0.0    → round = 0  (no diabetes)
votes = [0, 0, 1]  → mean = 0.333  → round = 0  (no diabetes)
votes = [1, 0, 1]  → mean = 0.666  → round = 1  (sí diabetes)
votes = [1, 1, 1]  → mean = 1.0    → round = 1  (sí diabetes)
```

#### Línea 9: `return neighbors_idx, neighbors_dists, pred`

- **Retorna:** Una tupla con 3 elementos (por eso el tipo de retorno es `Tuple[...]`).
  - Índices de los vecinos.
  - Distancias a esos vecinos.
  - Predicción final.

---

## Ejemplo completo paso a paso

Supongamos que tienes 6 pacientes de entrenamiento y quieres predecir un nuevo:

**Datos de entrenamiento (después de calcular distancias):**
```
Paciente 0: etiqueta=0, distancia=3.28
Paciente 1: etiqueta=1, distancia=1.42
Paciente 2: etiqueta=0, distancia=1.98
Paciente 3: etiqueta=1, distancia=2.05
Paciente 4: etiqueta=0, distancia=1.55
Paciente 5: etiqueta=1, distancia=2.30

Nuevo paciente: distancia a cada uno = [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]
```

**Paso 1: Calcular distancias**
```python
dists = [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]
```

**Paso 2: Ordenar por distancia**
```python
idx_sorted = np.argsort(dists)  # [1, 4, 2, 3, 5, 0]
```

**Paso 3: Tomar los 3 más cercanos**
```python
neighbors_idx = [1, 4, 2]
neighbors_dists = [1.42, 1.55, 1.98]
```

**Paso 4: Obtener etiquetas de esos vecinos**
```python
y_train = [0, 1, 0, 1, 0, 1]
votes = y_train[[1, 4, 2]] = [1, 0, 0]
```

**Paso 5: Votar mayoritariamente**
```python
mean(votes) = mean([1, 0, 0]) = 1/3 = 0.333
round(0.333) = 0
pred = 0  # No diabetes
```

**Resultado:**
```python
neighbors_idx = [1, 4, 2]
neighbors_dists = [1.42, 1.55, 1.98]
pred = 0
```

**Interpretación:** El nuevo paciente se parece más a los pacientes 1, 4 y 2. De esos, 1 tiene diabetes pero 4 y 2 no. Votación: 2 votos contra diabetes, 1 a favor. **Predicción: no diabetes (0)**.

---

## Votación mayoritaria vs media

En este código usamos la **media** para hacer votación:
```python
pred = int(np.round(np.mean(votes)))
```

**Cómo funciona:**
- Etiquetas: 0 = no, 1 = sí.
- Media de [0, 0, 0] = 0.0 → predice 0.
- Media de [0, 0, 1] = 0.333 → redondea a 0 → predice 0.
- Media de [0, 1, 1] = 0.666 → redondea a 1 → predice 1.
- Media de [1, 1, 1] = 1.0 → predice 1.

Es equivalente a contar votos, pero usa una sola línea.

**Forma alternativa (explícita):**
```python
count_ones = np.sum(votes)  # Contar cuántos 1s hay
pred = 1 if count_ones >= k/2 else 0
```

Pero la forma de media es más concisa.

---

## El parámetro k

En este código, `k=3` por defecto. Pero puedes cambiar:

```python
neighbors_idx, neighbors_dists, pred = knn_predict(X_train, y_train, x_new, k=5)
```

**Qué cambia:**
- Con k=3, uses los 3 vecinos más cercanos.
- Con k=5, usas los 5 vecinos más cercanos.
- Con k=7, usas los 7, etc.

**Regla general:**
- k pequeño (1, 3): modelo más flexible, riesgo de overfitting.
- k grande (7, 11): modelo más suave, riesgo de underfitting.
- k = raíz cuadrada del número de datos es una regla común.

---

## Resumen visual

```
Paso 1: Calcular distancias
   Nuevo paciente vs Todos los entrenamiento
   dists = [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]

Paso 2: Ordenar
   idx_sorted = [1, 4, 2, 3, 5, 0]
   (del más cercano al más lejano)

Paso 3: Tomar k=3
   neighbors = pacientes [1, 4, 2]
   distances = [1.42, 1.55, 1.98]

Paso 4: Leer etiquetas
   votes = [1, 0, 0]
   (1 tiene diabetes, 4 y 2 no)

Paso 5: Votación
   mean([1, 0, 0]) = 0.333 → round = 0
   pred = 0 (no diabetes)

Salida:
   neighbors_idx = [1, 4, 2]
   neighbors_dists = [1.42, 1.55, 1.98]
   pred = 0
```

---

## Casos especiales

### ¿Qué pasa si hay empate?

Con k=3, no hay empates posibles (siempre hay mayoría de 2 vs 1).

Pero con k=2:
```python
votes = [0, 1]
mean = 0.5
round(0.5) = 0 en Python (redondea al par más cercano)
```

Con k=4:
```python
votes = [0, 0, 1, 1]
mean = 0.5
round(0.5) = 0
```

El comportamiento exacto depende de `np.round`, que en Python 3 sigue "banker's rounding" (redondea al par más cercano). Pero típicamente con k impar, no hay empates.

### ¿Qué pasa si k es mayor que el número de datos?

Si tienes 6 pacientes de entrenamiento y intentas k=10:
```python
neighbors_idx = idx_sorted[:10]  # Toma los 6 disponibles (con advertencia)
```

Numpy toma cuantos haya disponibles. Es un riesgo de errores, pero el código no falla.

---

## Comparación con sklearn

Este código es una versión manual de:
```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
pred = knn.predict([x_new])
```

La diferencia:
- Sklearn es más eficiente, permite muchos algoritmos de búsqueda, etc.
- Este código manual es pedagógico: aprendes exactamente qué sucede.

Por eso el enunciado pidió NO usar sklearn para esta función.
