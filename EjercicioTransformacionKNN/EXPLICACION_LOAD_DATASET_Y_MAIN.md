# Explicación de `load_dataset` y `main`

## Función `load_dataset`

### Qué es y para qué sirve

Esta función simplemente **carga un archivo CSV y lo convierte en un DataFrame de pandas**.

### El código

```python
def load_dataset(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)
```

### Explicación línea por línea

#### Línea 1: `def load_dataset(path: Path) -> pd.DataFrame:`

- **Parámetro `path`:** Una ruta de archivo (tipo `Path` de pathlib).
- **Retorno `-> pd.DataFrame`:** Devuelve un DataFrame.

#### Línea 2: `return pd.read_csv(path)`

- **`pd.read_csv`:** Función de pandas que lee archivos CSV.
- **Qué hace:** Lee el CSV línea por línea y lo convierte en una tabla (DataFrame).
- **Resultado:** Un objeto DataFrame con filas y columnas.

**Ejemplo:**

Si `data.csv` contiene:
```csv
sexo,ciudad,colesterol,edad,diabetes
1,Cuenca,bajo,18,no
2,Quito,alto,52,si
```

Después de `load_dataset`:
```python
df = pd.DataFrame({
    'sexo': [1, 2],
    'ciudad': ['Cuenca', 'Quito'],
    'colesterol': ['bajo', 'alto'],
    'edad': [18, 52],
    'diabetes': ['no', 'si']
})
```

### Por qué una función aparte

Parece simple, pero es buena práctica:
- **Reutilizable:** Si cargas datos en varios lugares, no repites código.
- **Testeable:** Puedes escribir pruebas unitarias.
- **Mantenible:** Si luego necesitas procesar el CSV (ignorar filas, renombrar columnas), cambias en un solo lugar.

---

## Función `main`

### Qué es y para qué sirve

Esta es la función principal que **coordina todo el flujo**: carga datos, transforma, entrena KNN y predice.

### El código

```python
def main():
    base = Path(__file__).parent
    csv_path = base / 'data.csv'
    if not csv_path.exists():
        print(f"No se encuentra {csv_path}. Coloca el CSV en la misma carpeta.")
        return

    df = load_dataset(csv_path)

    # target mapping
    df['diabetes_bin'] = df['diabetes'].map({'no': 0, 'si': 1}).astype(int)

    transformer = FeatureTransformer()
    transformer.fit(df)
    X = transformer.transform(df)
    y = df['diabetes_bin'].to_numpy()

    # ejemplo de paciente nuevo
    nuevo = pd.DataFrame([{
        'sexo': 2,
        'ciudad': 'Cuenca',
        'colesterol': 'alto',
        'edad': 50
    }])

    x_new_feat = transformer.transform(nuevo)

    neighbors_idx, neighbors_dists, pred = knn_predict(X.to_numpy(), y, x_new_feat.to_numpy()[0], k=3)

    print('Distancias calculadas a cada vecino (k=3):')
    print(neighbors_dists)
    print('\nVecinos seleccionados (índices):')
    print(neighbors_idx)
    print('\nRegistros de los vecinos y su etiqueta diabetes:')
    for i in neighbors_idx:
        print(df.iloc[i].to_dict())
    print(f"\nPredicción final (0=no, 1=si): {pred}")
```

### Explicación línea por línea

#### Línea 1: `def main():`

- Función sin parámetros.
- Ejecuta el programa completo.

#### Línea 2: `base = Path(__file__).parent`

- **`__file__`:** Ruta del script actual (`transformaciones_knn.py`).
- **`.parent`:** La carpeta que contiene el script.
- **Resultado:** La carpeta `EjercicioTransformacionKNN`.
- **Por qué:** Para encontrar `data.csv` que está en la misma carpeta.

**Ejemplo:**
```
Si el script está en: c:\Users\wwwda\Documents\Practica-EDA\EjercicioTransformacionKNN\transformaciones_knn.py
Entonces base es:    c:\Users\wwwda\Documents\Practica-EDA\EjercicioTransformacionKNN
```

#### Línea 3: `csv_path = base / 'data.csv'`

- **`/`:** Operador de pathlib para concatenar rutas.
- **Resultado:** Ruta completa a `data.csv`.

**Ejemplo:**
```
csv_path = c:\Users\wwwda\Documents\Practica-EDA\EjercicioTransformacionKNN\data.csv
```

#### Línea 4-5: `if not csv_path.exists():` y siguiente

- **`.exists()`:** Comprueba si el archivo existe.
- **`if not`:** Si NO existe, entra en el bloque.
- **`print(...)`:** Muestra un mensaje de error.
- **`return`:** Sale de la función sin hacer nada más.

**Propósito:** Validación. Si falta el archivo, el programa no falla silenciosamente; te lo dice.

#### Línea 7: `df = load_dataset(csv_path)`

- Carga el CSV en memoria como un DataFrame.
- **Resultado:** `df` tiene 6 filas (6 pacientes) y 5 columnas (sexo, ciudad, colesterol, edad, diabetes).

#### Línea 9-10: `df['diabetes_bin'] = df['diabetes'].map({'no': 0, 'si': 1}).astype(int)`

- **`.map(...)`:** Reemplaza "no" por 0 y "sí" por 1.
- **`.astype(int)`:** Convierte a números enteros.
- **Nueva columna:** Se crea `diabetes_bin` con 0s y 1s.

**Ejemplo:**
```python
Antes:
   diabetes
0       no
1       si
2       no

Después:
   diabetes_bin
0            0
1            1
2            0
```

**Por qué:** KNN necesita etiquetas numéricas (0 o 1), no texto.

#### Línea 12-13: `transformer = FeatureTransformer()` y `transformer.fit(df)`

- Crea el transformador.
- Lo ajusta con los datos de entrenamiento.
- Aprende: qué ciudades, qué sexos, media/std de edad.

#### Línea 14: `X = transformer.transform(df)`

- Transforma el DataFrame a una tabla numérica.
- **Resultado:** DataFrame con 6 filas y ~10 columnas (edad_scaled, colesterol_ord, sexo_*, ciudad_*).

#### Línea 15: `y = df['diabetes_bin'].to_numpy()`

- Extrae las etiquetas como un array numpy.
- **Resultado:** Array con valores [0, 1, 0, 1, 0, 1].

#### Línea 17-22: Crear un nuevo paciente

```python
nuevo = pd.DataFrame([{
    'sexo': 2,
    'ciudad': 'Cuenca',
    'colesterol': 'alto',
    'edad': 50
}])
```

- **`[{...}]`:** Lista con un diccionario (un paciente).
- Crea un DataFrame con 1 fila y 4 columnas.
- Estos son los valores del paciente a predecir (del ejemplo del enunciado).

#### Línea 24: `x_new_feat = transformer.transform(nuevo)`

- Transforma el nuevo paciente usando el mismo transformador.
- **Resultado:** DataFrame con 1 fila y ~10 columnas (la misma estructura que `X`).

#### Línea 26: `neighbors_idx, neighbors_dists, pred = knn_predict(X.to_numpy(), y, x_new_feat.to_numpy()[0], k=3)`

**Desglose:**
- **`X.to_numpy()`:** Convierte X a array numpy. Forma: (6, 10).
- **`y`:** Ya es array numpy. Forma: (6,).
- **`x_new_feat.to_numpy()[0]`:** Convierte a array y toma la primera (única) fila. Forma: (10,).
- **Llama a `knn_predict`** con estos datos y k=3.

**Resultado:**
- `neighbors_idx`: índices de los 3 vecinos más cercanos.
- `neighbors_dists`: distancias a esos vecinos.
- `pred`: predicción (0 o 1).

#### Línea 28-37: Imprimir resultados

```python
print('Distancias calculadas a cada vecino (k=3):')
print(neighbors_dists)
print('\nVecinos seleccionados (índices):')
print(neighbors_idx)
print('\nRegistros de los vecinos y su etiqueta diabetes:')
for i in neighbors_idx:
    print(df.iloc[i].to_dict())
print(f"\nPredicción final (0=no, 1=si): {pred}")
```

- Imprime cada resultado paso a paso.
- **`df.iloc[i]`:** Obtiene la fila i-ésima del DataFrame original (para mostrar datos brutos, no solo números).
- **`.to_dict()`:** Convierte a diccionario (más legible).

**Ejemplo de salida:**
```
Distancias calculadas a cada vecino (k=3):
[1.4194070602392845, 1.7584019781059879, 1.9854092197973214]

Vecinos seleccionados (índices):
[1, 4, 2]

Registros de los vecinos y su etiqueta diabetes:
{'sexo': 2, 'ciudad': 'Quito', 'colesterol': 'alto', 'edad': 52, 'diabetes': 'si', 'diabetes_bin': 1}
{'sexo': 2, 'ciudad': 'Ambato', 'colesterol': 'medio', 'edad': 45, 'diabetes': 'no', 'diabetes_bin': 0}
{'sexo': 2, 'ciudad': 'Guayaquil', 'colesterol': 'medio', 'edad': 34, 'diabetes': 'no', 'diabetes_bin': 0}

Predicción final (0=no, 1=si): 0
```

---

## Flujo completo

```
main()
  │
  ├─ Validar que existe data.csv
  │
  ├─ Cargar CSV → df (6 filas)
  │
  ├─ Mapear 'no' y 'sí' a 0 y 1 → diabetes_bin
  │
  ├─ Crear transformer
  │
  ├─ transformer.fit(df) → aprende estructura
  │
  ├─ X = transformer.transform(df) → 6 x 10 array
  │
  ├─ y = [0, 1, 0, 1, 0, 1]
  │
  ├─ Crear nuevo paciente (1 fila)
  │
  ├─ x_new = transformer.transform(nuevo) → 1 x 10 array
  │
  ├─ pred = knn_predict(X, y, x_new[0]) → [índices], [dists], predicción
  │
  └─ Imprimir resultados
```

---

## Resumen

| Función | Propósito | Entrada | Salida |
|---------|-----------|---------|--------|
| `load_dataset` | Cargar CSV | Ruta del archivo | DataFrame |
| `main` | Orquestar todo | Nada (usa archivo local) | Prints + programa ejecutado |

Ambas son funciones "de infraestructura": no implementan el algoritmo, sino que lo conectan con archivos y usuarios.

---

## Cómo ejecutar

Desde PowerShell en la carpeta del proyecto:

```bash
python EjercicioTransformacionKNN/transformaciones_knn.py
```

Esto ejecuta:
1. La importación de `main` (al final del archivo).
2. Llama a `main()`.
3. Ejecuta todo el flujo.

---

## Puntos clave

1. **`load_dataset` es simple:** Solo lee el CSV. La lógica verdadera está en `main`.
2. **`main` coordina:** Valida, carga, transforma, predice e imprime.
3. **Separación de responsabilidades:** Cada función hace una cosa bien.
4. **Validación:** Comprueba que exista el archivo antes de usarlo.
5. **Resultar:** Muestra los vecinos y la predicción, no solo el número final.
