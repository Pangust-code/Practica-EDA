# Explicación de `euclidean_distances`

## Qué es y para qué sirve

Esta función calcula la **distancia euclídea** entre un punto y varios puntos.

La distancia euclídea es la distancia "en línea recta" en un espacio multidimensional.

**En palabras simples:**
- Si tienes un punto nuevo (el paciente a predecir) y varios puntos antiguos (pacientes de entrenamiento).
- Necesitas saber cuál es el más parecido (más cercano).
- KNN usa distancia euclídea para medir "parecido".

---

## La fórmula

Para dos puntos en el espacio:

$$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2 + ...}$$

**En pocas palabras:**
1. Resta cada coordenada.
2. Eleva al cuadrado cada diferencia.
3. Suma todos los cuadrados.
4. Saca la raíz cuadrada del resultado.

---

## El código

```python
def euclidean_distances(X: np.ndarray, x_new: np.ndarray) -> np.ndarray:
    # ensure numeric numpy arrays (avoid object-dtype issues)
    X_arr = np.asarray(X, dtype=float)
    x_arr = np.asarray(x_new, dtype=float)
    # broadcast subtraction
    diff = X_arr - x_arr
    return np.sqrt(np.sum(diff ** 2, axis=1))
```

### Explicación línea por línea

#### Línea 1: `def euclidean_distances(X: np.ndarray, x_new: np.ndarray) -> np.ndarray:`

- **Parámetro `X`:** Matriz numpy con todos los puntos de entrenamiento.
  - Forma: `(n_pacientes, n_características)` ej: (6, 10)
  - Cada fila es un paciente.
  - Cada columna es una característica (edad_scaled, colesterol_ord, ciudad_*, sexo_*).

- **Parámetro `x_new`:** Un punto nuevo (un solo paciente).
  - Forma: `(n_características,)` ej: (10,)
  - Un array 1D con las características del nuevo paciente.

- **Retorno `-> np.ndarray`:** Array con distancias.
  - Forma: `(n_pacientes,)` ej: (6,)
  - Cada elemento es la distancia del nuevo paciente al correspondiente paciente de entrenamiento.

#### Línea 2-3: `X_arr = np.asarray(X, dtype=float)` y `x_arr = np.asarray(x_new, dtype=float)`

- **Qué hace:** Convierte los arrays a tipo `float` (números decimales).
- **Por qué:** A veces pandas devuelve tipos "object" que causan errores en numpy. Asegurar que son floats evita problemas.
- **Diferencia:**
  ```python
  X = np.array([1, 2, 3], dtype=object)  # Puede causar error
  X_arr = np.asarray(X, dtype=float)     # Garantizado que es float
  ```

#### Línea 4: `diff = X_arr - x_arr`

- **Qué hace:** Resta el nuevo punto de TODOS los puntos de entrenamiento.
- **Operación vectorizada:** Esto es lo poderoso de numpy. No necesitas un loop.

**Ejemplo visual:**

Si tienes:
```
X_arr (3 pacientes, 2 características):
[[1.0, 2.0],
 [3.0, 4.0],
 [5.0, 6.0]]

x_arr (1 nuevo paciente):
[2.0, 3.0]

Después de X_arr - x_arr (broadcast):
[[1.0 - 2.0, 2.0 - 3.0],      → [-1.0, -1.0]
 [3.0 - 2.0, 4.0 - 3.0],      → [1.0, 1.0]
 [5.0 - 2.0, 6.0 - 3.0]]      → [3.0, 3.0]
```

Nota: numpy automáticamente "expande" `x_arr` para que coincida con cada fila de `X_arr`. Esto se llama **broadcasting**.

#### Línea 5: `return np.sqrt(np.sum(diff ** 2, axis=1))`

Esto se ejecuta en tres partes, de adentro hacia afuera:

**Parte 1: `diff ** 2`**
- Eleva al cuadrado cada diferencia.
- Ejemplo (continuando del anterior):
  ```
  [[-1.0, -1.0]     →  [[1.0, 1.0],
   [1.0, 1.0]   →       [1.0, 1.0],
   [3.0, 3.0]]   →      [9.0, 9.0]]
  ```

**Parte 2: `np.sum(diff ** 2, axis=1)`**
- Suma cada fila (por eso `axis=1`).
- `axis=1` significa: suma por columnas (dentro de cada fila).
- Ejemplo:
  ```
  [[1.0, 1.0],   →  [2.0,
   [1.0, 1.0],   →   2.0,
   [9.0, 9.0]]   →   18.0]
  ```

**Parte 3: `np.sqrt(...)`**
- Saca la raíz cuadrada de cada suma.
- Ejemplo:
  ```
  [2.0, 2.0, 18.0]   →   [1.414..., 1.414..., 4.242...]
  ```

---

## Ejemplo completo

Supongamos que tienes 3 pacientes de entrenamiento transformados:

```
Paciente 0: edad_scaled=-1.71, colesterol_ord=0, sexo_1=1, sexo_2=0, ciudad_Cuenca=1, ...
Paciente 1: edad_scaled=0.35,  colesterol_ord=2, sexo_1=0, sexo_2=1, ciudad_Quito=0, ...
Paciente 2: edad_scaled=-0.74, colesterol_ord=1, sexo_1=0, sexo_2=1, ciudad_Guayaquil=1, ...

Nuevo paciente: edad_scaled=0.23, colesterol_ord=2, sexo_1=0, sexo_2=1, ciudad_Cuenca=1, ...
```

Ahora agrupamos solo las características numéricas:

```
X_arr (3, 10):
[[-1.71, 0, 1, 0, 1, 0, 0, 0, 0, 0],
 [0.35,  2, 0, 1, 0, 0, 0, 0, 0, 1],
 [-0.74, 1, 0, 1, 0, 0, 1, 0, 0, 0]]

x_arr (10,):
[0.23, 2, 0, 1, 1, 0, 0, 0, 0, 0]
```

**Resta:**
```
diff:
[[-1.71-0.23, 0-2, 1-0, 0-1, 1-1, 0-0, 1-0, 0-0, 0-0, 0-0],
 [0.35-0.23,  2-2, 0-0, 1-1, 0-1, 0-0, 0-0, 0-0, 0-0, 1-0],
 [-0.74-0.23, 1-2, 0-0, 1-1, 0-1, 0-0, 1-0, 0-0, 0-0, 0-0]]

= [[-1.94, -2, 1, -1, 0, 0, 1, 0, 0, 0],
   [0.12,  0,  0,  0, -1, 0, 0, 0, 0, 1],
   [-0.97, -1, 0,  0, -1, 0, 1, 0, 0, 0]]
```

**Cuadrados:**
```
[[-1.94^2, (-2)^2, 1^2, (-1)^2, 0^2, ...],
 [0.12^2, 0^2, 0^2, 0^2, (-1)^2, ...],
 [(-0.97)^2, (-1)^2, 0^2, 0^2, (-1)^2, ...]]

= [[3.76, 4, 1, 1, 0, 0, 1, 0, 0, 0],
   [0.01, 0, 0, 0, 1, 0, 0, 0, 0, 1],
   [0.94, 1, 0, 0, 1, 0, 1, 0, 0, 0]]
```

**Suma (axis=1):**
```
[3.76+4+1+1+0+0+1+0+0+0,
 0.01+0+0+0+1+0+0+0+0+1,
 0.94+1+0+0+1+0+1+0+0+0]

= [10.76, 2.01, 3.94]
```

**Raíz cuadrada:**
```
[sqrt(10.76), sqrt(2.01), sqrt(3.94)]
= [3.28, 1.42, 1.98]
```

**Resultado:**
```
dists = [3.28, 1.42, 1.98]
```

**Interpretación:**
- Paciente 0 está a distancia 3.28 (lejos).
- Paciente 1 está a distancia 1.42 (más cercano).
- Paciente 2 está a distancia 1.98 (medio).

---

## Por qué numpy es eficiente

**Sin numpy (con loops, lento):**
```python
def euclidean_distances_lento(X, x_new):
    dists = []
    for i in range(len(X)):
        dist_sq = 0
        for j in range(len(X[i])):
            dist_sq += (X[i][j] - x_new[j]) ** 2
        dists.append(dist_sq ** 0.5)
    return dists
```

**Con numpy (vectorizado, rápido):**
```python
def euclidean_distances(X, x_new):
    X_arr = np.asarray(X, dtype=float)
    x_arr = np.asarray(x_new, dtype=float)
    diff = X_arr - x_arr
    return np.sqrt(np.sum(diff ** 2, axis=1))
```

Numpy opera sobre arrays completos sin necesidad de loops explícitos. Es muchísimo más rápido.

---

## Resumen

```
Entrada:
  X_arr: matriz de entrenamiento (6, 10)
  x_arr: nuevo punto (10,)

Proceso:
  1. Resta x_arr de cada fila de X_arr → (6, 10)
  2. Eleva al cuadrado → (6, 10)
  3. Suma cada fila → (6,)
  4. Raíz cuadrada → (6,)

Salida:
  dists: array de distancias (6,)
```

Cada elemento de `dists` es la distancia del nuevo paciente al correspondiente paciente de entrenamiento.

Luego, `knn_predict` usa estas distancias para encontrar los `k` vecinos más cercanos.
