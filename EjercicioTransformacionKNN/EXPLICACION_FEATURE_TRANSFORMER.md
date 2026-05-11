# Explicación detallada de la clase FeatureTransformer

## Índice
1. [Qué es y para qué sirve](#qué-es-y-para-qué-sirve)
2. [El método `__init__`](#el-método-__init__)
3. [El método `fit`](#el-método-fit)
4. [El método `transform`](#el-método-transform)
5. [Flujo completo con ejemplo](#flujo-completo-con-ejemplo)

---

## Qué es y para qué sirve

La clase `FeatureTransformer` es un **traductor de datos**.

**Problema que resuelve:**
- KNN (K-Nearest Neighbors) solo entiende números.
- Tu dataset tiene texto: ciudades como "Cuenca", niveles de colesterol como "alto".
- KNN no puede calcular distancia euclídea entre "Quito" y "Cuenca".

**Solución:**
- `FeatureTransformer` convierte texto en números.
- Convierte categorías en columnas dummy (0 y 1).
- Estandariza números como edad.
- Todo se guarda de forma consistente para que entrenar y predecir usen la misma estructura.

---

## El método `__init__`

```python
def __init__(self):
    self.city_cols = None
    self.sex_cols = None
    self.edad_mean = None
    self.edad_std = None
    self.chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}
```

### Explicación línea por línea

#### Línea 1: `def __init__(self):`
- **Qué es:** Constructor de la clase.
- **Cuándo se ejecuta:** Cuando haces `transformer = FeatureTransformer()`.
- **Qué hace:** Inicializa los atributos (variables internas) del objeto.

#### Línea 2: `self.city_cols = None`
- **Qué es:** Un atributo llamado `city_cols` (columnas de ciudad).
- **Por qué None:** Aún no sabemos qué ciudades habrá en los datos, así que dejamos esto vacío.
- **Se usará para:** Guardar los nombres de columnas dummy después de hacer `fit`.
- **Ejemplo:** Si tus datos tienen ciudades Cuenca, Quito, Loja, esto contendrá:
  ```
  ['ciudad_Ambato', 'ciudad_Cuenca', 'ciudad_Guayaquil', 'ciudad_Loja', 'ciudad_Machala', 'ciudad_Quito']
  ```

#### Línea 3: `self.sex_cols = None`
- **Qué es:** Un atributo llamado `sex_cols` (columnas de sexo).
- **Por qué None:** Aún no sabemos si hay sexo 1, 2, o ambos.
- **Se usará para:** Guardar los nombres de columnas dummy de sexo.
- **Ejemplo:** Si los datos tienen sexo 1 y 2, esto será:
  ```
  ['sexo_1', 'sexo_2']
  ```

#### Línea 4: `self.edad_mean = None`
- **Qué es:** Un atributo para guardar la media de la edad.
- **Por qué None:** Aún no hemos visto los datos.
- **Se usará para:** Guardar la media de edad del entrenamiento.
- **Ejemplo:** Si las edades son [18, 52, 34, 61, 45, 67], la media es aproximadamente 46.17.

#### Línea 5: `self.edad_std = None`
- **Qué es:** Un atributo para guardar la desviación estándar de la edad.
- **Por qué None:** Aún no hemos visto los datos.
- **Se usará para:** Guardar la desviación estándar de la edad del entrenamiento.
- **Fórmula:** `std = sqrt( suma((x - media)^2) / n )`
- **Importancia:** Sin esto, no podemos estandarizar (escalar) la edad.

#### Línea 6: `self.chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}`
- **Qué es:** Un diccionario que mapea texto a números.
- **Por qué un diccionario:** Es la forma más rápida de convertir "bajo" en 0, "medio" en 1, etc.
- **Se usará para:** En `transform`, reemplazar texto de colesterol por números ordinales.
- **Ejemplo de uso:**
  ```python
  self.chol_map['alto']  # devuelve 2
  self.chol_map['bajo']  # devuelve 0
  ```
- **Nota importante:** Este es el único atributo que NO es None. Lo creamos aquí porque es un diccionario fijo que no cambia según los datos.

---

## El método `fit`

```python
def fit(self, df: pd.DataFrame):
    city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
    sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')
    self.city_cols = list(city_dummies.columns)
    self.sex_cols = list(sex_dummies.columns)
    self.edad_mean = df['edad'].mean()
    self.edad_std = df['edad'].std(ddof=0) if df['edad'].std(ddof=0) != 0 else 1.0
```

**Propósito general:** "Aprender" la estructura de los datos de entrenamiento.

### Explicación línea por línea

#### Línea 1: `def fit(self, df: pd.DataFrame):`
- **Qué es:** Definición del método `fit`.
- **Parámetro `df`:** Es el DataFrame completo con todos los datos de entrenamiento.
- **Cuándo se llama:** Una sola vez, al principio:
  ```python
  transformer = FeatureTransformer()
  transformer.fit(df_entrenamiento)  # <-- aquí
  ```

#### Línea 2: `city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')`
- **Qué es:** `pd.get_dummies` convierte columnas categóricas en dummy variables (0 y 1).
- **Parámetro `df['ciudad']`:** Toma solo la columna "ciudad".
- **Parámetro `prefix='ciudad'`:** Cada columna nueva tendrá el prefijo "ciudad_".

**Ejemplo visual:**
```
Datos originales:
      ciudad
0    Cuenca
1     Quito
2 Guayaquil
3      Loja
4    Ambato
5   Machala

Después de get_dummies:
   ciudad_Ambato  ciudad_Cuenca  ciudad_Guayaquil  ciudad_Loja  ciudad_Machala  ciudad_Quito
0              0              1                0            0               0             0
1              0              0                0            0               0             1
2              0              0                1            0               0             0
3              0              0                0            1               0             0
4              1              0                0            0               0             0
5              0              0                0            0               1             0
```

- **Por qué funciona:** Cada fila tiene exactamente un 1 (la ciudad donde vive) y el resto ceros.
- **Variable local vs atributo:** `city_dummies` es una variable local (solo existe en este método). Luego guardaremos sus nombres en `self.city_cols`.

#### Línea 3: `sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')`
- **Qué es:** Lo mismo que arriba, pero para sexo.
- **`.astype(str)`:** Convierte los números 1 y 2 a texto ("1", "2") porque `get_dummies` funciona mejor con strings.

**Ejemplo visual:**
```
Datos originales:
   sexo
0     1
1     2
2     2
3     1
4     2
5     1

Después de get_dummies:
   sexo_1  sexo_2
0       1       0
1       0       1
2       0       1
3       1       0
4       0       1
5       1       0
```

#### Línea 4: `self.city_cols = list(city_dummies.columns)`
- **Qué es:** Guarda los nombres de las columnas dummy de ciudad.
- **`.columns`:** Obtiene los nombres de las columnas (que son strings).
- **`list(...)`:** Convierte esos nombres a una lista de Python.
- **Por qué lo guardamos:** Cuando llegue un paciente nuevo, debemos usar las MISMAS columnas. Si en entrenamiento vimos Cuenca pero el nuevo paciente es de una ciudad desconocida, necesitamos saber qué columnas esperar.
- **Resultado almacenado:**
  ```python
  self.city_cols = ['ciudad_Ambato', 'ciudad_Cuenca', 'ciudad_Guayaquil', 
                    'ciudad_Loja', 'ciudad_Machala', 'ciudad_Quito']
  ```

#### Línea 5: `self.sex_cols = list(sex_dummies.columns)`
- **Qué es:** Guarda los nombres de las columnas dummy de sexo.
- **Resultado almacenado:**
  ```python
  self.sex_cols = ['sexo_1', 'sexo_2']
  ```

#### Línea 6: `self.edad_mean = df['edad'].mean()`
- **Qué es:** Calcula la media (promedio) de todas las edades.
- **`.mean()`:** Suma todas las edades y divide entre el número de pacientes.
- **Ejemplo:**
  ```
  Edades: [18, 52, 34, 61, 45, 67]
  Media = (18 + 52 + 34 + 61 + 45 + 67) / 6 = 277 / 6 ≈ 46.17
  ```
- **Por qué lo guardamos:** Cuando llegue un nuevo paciente, usaremos esta media para estandarizar su edad exactamente igual.

#### Línea 7: `self.edad_std = df['edad'].std(ddof=0) if df['edad'].std(ddof=0) != 0 else 1.0`
- **Qué es:** Calcula la desviación estándar de las edades.
- **`.std(ddof=0)`:** Parámetro `ddof=0` es importante: calcula la desviación estándar poblacional (divide entre n), no muestral (divide entre n-1). Esto coincide con `StandardScaler` de sklearn.
- **Fórmula:**
  ```
  std = sqrt( suma((edad - media)^2) / n )
  ```
- **Ejemplo:**
  ```
  Edades: [18, 52, 34, 61, 45, 67]
  Media: 46.17
  Diferencias: [-28.17, 5.83, -12.17, 14.83, -1.17, 20.83]
  Cuadrados: [793.5, 34, 148.1, 219.9, 1.4, 433.9]
  Suma: 1630.8
  std = sqrt(1630.8 / 6) ≈ 16.48
  ```
- **`if ... else 1.0`:** Protección: si por alguna razón la desviación es 0 (todas las edades son iguales), usamos 1.0 para evitar división por cero.
- **Por qué lo guardamos:** En `transform`, dividiremos por esta desviación para estandarizar.

---

## El método `transform`

```python
def transform(self, df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['colesterol_ord'] = df['colesterol'].map(self.chol_map).astype(float)
    city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
    sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')
    for c in (self.city_cols or []):
        if c not in city_dummies:
            city_dummies[c] = 0
    for c in (self.sex_cols or []):
        if c not in sex_dummies:
            sex_dummies[c] = 0
    city_dummies = city_dummies.reindex(sorted(self.city_cols), axis=1)
    sex_dummies = sex_dummies.reindex(sorted(self.sex_cols), axis=1)
    df['edad_scaled'] = (df['edad'] - self.edad_mean) / self.edad_std
    features = pd.concat([
        df[['edad_scaled', 'colesterol_ord']].reset_index(drop=True),
        sex_dummies.reset_index(drop=True),
        city_dummies.reset_index(drop=True)
    ], axis=1)
    return features
```

**Propósito general:** Convertir datos crudos (texto, números sin escalar) en una tabla numérica lista para KNN.

### Explicación línea por línea

#### Línea 1: `def transform(self, df: pd.DataFrame) -> pd.DataFrame:`
- **Qué es:** Definición del método.
- **Parámetro `df`:** DataFrame con datos a transformar. Puede ser el conjunto de entrenamiento o un nuevo paciente.
- **`-> pd.DataFrame`:** Indica que devuelve un DataFrame.

#### Línea 2: `df = df.copy()`
- **Qué es:** Hace una copia del DataFrame.
- **Por qué:** Para no modificar el original. Si no hacemos esto, cambios en `df` dentro de la función afectarían al DataFrame original.
- **Ejemplo:**
  ```python
  df_original = pd.DataFrame({'edad': [50]})
  df = df_original  # comparte la misma memoria
  df['edad'] = 100
  print(df_original)  # ¡cambió a 100!
  ```

#### Línea 3: `df['colesterol_ord'] = df['colesterol'].map(self.chol_map).astype(float)`
- **Qué es:** Convierte colesterol de texto a números ordinales.
- **`.map(self.chol_map)`:** Usa el diccionario creado en `__init__` para reemplazar valores.
- **Ejemplo:**
  ```python
  # Entrada:
  df['colesterol'] = ['bajo', 'alto', 'medio', 'muy alto']
  
  # Después de map:
  [0, 2, 1, 3]
  
  # Después de astype(float):
  [0.0, 2.0, 1.0, 3.0]
  ```
- **`.astype(float)`:** Convierte a números decimales (importante para cálculos numéricos).
- **Nueva columna:** Se crea una columna llamada `colesterol_ord` en el DataFrame.

#### Línea 4: `city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')`
- **Qué es:** Lo mismo que en `fit`: convierte ciudad a dummies.
- **Nota importante:** Aquí creamos dummies NUEVAS, no usamos las guardadas en `fit`.
- **Por qué:** Porque el nuevo DataFrame puede tener ciudades diferentes a las del entrenamiento.

#### Línea 5: `sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')`
- **Qué es:** Lo mismo para sexo.

#### Línea 6-7: `for c in (self.city_cols or []):`
- **Qué es:** Bucle que itera sobre cada nombre de columna guardado en `fit`.
- **`(self.city_cols or [])`:** Si `self.city_cols` es None, usa una lista vacía `[]` en su lugar.
- **Propósito:** Asegurar que todas las columnas del entrenamiento estén presentes.

#### Línea 7-8:
```python
if c not in city_dummies:
    city_dummies[c] = 0
```
- **Qué hace:** Si una columna esperada NO está en las dummies nuevas, la agrega con todos ceros.
- **Ejemplo:**
  - En entrenamiento vimos ciudades: Cuenca, Quito, Loja, Guayaquil, Ambato, Machala.
  - Para un nuevo paciente de Quito, solo aparecerá `ciudad_Quito = 1` y el resto = 0.
  - Pero queremos que aparezcan TODAS las columnas, así que agregamos los que falten con 0.

#### Línea 9-10: `for c in (self.sex_cols or []):`
- **Qué hace:** Lo mismo que arriba, pero para las columnas de sexo.

#### Línea 11: `city_dummies = city_dummies.reindex(sorted(self.city_cols), axis=1)`
- **Qué es:** Reorganiza las columnas en orden alfabético.
- **`.reindex(...)`:** Reordena las columnas.
- **`sorted(self.city_cols)`:** Ordena alfabéticamente los nombres de columnas guardadas.
- **`axis=1`:** Eje 1 = columnas (eje 0 = filas).
- **Por qué:** Asegurar que el orden de columnas sea siempre el mismo entre entrenamiento y predicción.
- **Ejemplo:**
  ```python
  # Antes:
  ciudad_Quito, ciudad_Cuenca, ciudad_Loja
  
  # Después de sorted y reindex:
  ciudad_Ambato, ciudad_Cuenca, ciudad_Guayaquil, ciudad_Loja, ciudad_Machala, ciudad_Quito
  ```

#### Línea 12: `sex_dummies = sex_dummies.reindex(sorted(self.sex_cols), axis=1)`
- **Qué hace:** Lo mismo para sexo.

#### Línea 13: `df['edad_scaled'] = (df['edad'] - self.edad_mean) / self.edad_std`
- **Qué es:** Estandarización (scaling) de la edad.
- **Fórmula:** `edad_escalada = (edad - media) / desviación_estándar`
- **Resultado:** Edad transformada a una escala con media 0 y desviación 1.
- **Ejemplo:**
  ```python
  edad_media = 46.17
  edad_std = 16.48
  
  Para edad = 50:
  edad_scaled = (50 - 46.17) / 16.48 = 3.83 / 16.48 ≈ 0.232
  
  Para edad = 18:
  edad_scaled = (18 - 46.17) / 16.48 = -28.17 / 16.48 ≈ -1.710
  ```
- **Por qué es importante:**
  - KNN usa distancia euclídea.
  - Si edad está entre 18 y 67 y colesterol entre 0 y 3, la edad domina el cálculo de distancia.
  - Estandarizar hace que ambas variables contribuyan por igual.

#### Línea 14-18: `features = pd.concat([...])`
- **Qué es:** Une todas las columnas transformadas en un solo DataFrame.
- **`pd.concat`:** Concatena (une) DataFrames.
- **Primera parte:** `df[['edad_scaled', 'colesterol_ord']]` — las dos variables numéricas escaladas.
- **Segunda parte:** `sex_dummies` — dummies de sexo.
- **Tercera parte:** `city_dummies` — dummies de ciudad.
- **`reset_index(drop=True)`:** Reinicia los índices de filas (borra los índices antiguos, crea unos nuevos 0, 1, 2, ...).
- **`axis=1`:** Une por columnas (no por filas).

**Resultado final:**
```
Una tabla como esta:
   edad_scaled  colesterol_ord  sexo_1  sexo_2  ciudad_Ambato  ciudad_Cuenca  ...
0       -1.710            0.0       1       0              0              1  ...
1        0.354            2.0       0       1              0              0  ...
...
```

#### Línea 19: `return features`
- **Qué devuelve:** El DataFrame transformado, listo para KNN.

---

## Flujo completo con ejemplo

Supongamos que tienes el archivo `data.csv`:

```csv
sexo,ciudad,colesterol,edad,diabetes
1,Cuenca,bajo,18,no
2,Quito,alto,52,si
2,Guayaquil,medio,34,no
1,Loja,alto,61,si
2,Ambato,medio,45,no
1,Machala,muy alto,67,si
```

### Paso 1: Crear el transformador
```python
transformer = FeatureTransformer()
```
**Estado interno:**
```
city_cols = None
sex_cols = None
edad_mean = None
edad_std = None
chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}
```

### Paso 2: Ajustar (fit)
```python
transformer.fit(df)
```
**Qué ocurre internamente:**
- Calcula dummies de ciudad y sexo.
- Guarda sus nombres.
- Calcula media y std de edad.

**Estado interno después:**
```
city_cols = ['ciudad_Ambato', 'ciudad_Cuenca', 'ciudad_Guayaquil', 
             'ciudad_Loja', 'ciudad_Machala', 'ciudad_Quito']
sex_cols = ['sexo_1', 'sexo_2']
edad_mean = 46.166...
edad_std = 16.475...
chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}
```

### Paso 3: Transformar el conjunto de entrenamiento
```python
X = transformer.transform(df)
```
**Resultado (primeras 2 filas):**
```
   edad_scaled  colesterol_ord  sexo_1  sexo_2  ciudad_Ambato  ciudad_Cuenca  ciudad_Guayaquil  ciudad_Loja  ciudad_Machala  ciudad_Quito
0     -1.7098            0.0       1       0              0              1                0            0               0             0
1      0.3537            2.0       0       1              0              0                0            0               0             1
2     -0.7408            1.0       0       1              0              0                1            0               0             0
3      0.8968            2.0       1       0              0              0                0            1               0             0
4     -0.0746            1.0       0       1              0              0                0            0               1             0
5      1.2647            3.0       1       0              0              0                0            0               0             1
```

### Paso 4: Transformar un nuevo paciente
```python
nuevo = pd.DataFrame([{
    'sexo': 2,
    'ciudad': 'Cuenca',
    'colesterol': 'alto',
    'edad': 50
}])
x_new = transformer.transform(nuevo)
```
**Resultado:**
```
   edad_scaled  colesterol_ord  sexo_1  sexo_2  ciudad_Ambato  ciudad_Cuenca  ciudad_Guayaquil  ciudad_Loja  ciudad_Machala  ciudad_Quito
0      0.2340            2.0       0       1              0              1                0            0               0             0
```

**Notar:**
- `edad_scaled = (50 - 46.17) / 16.48 ≈ 0.234` ✓
- `colesterol_ord = 2` (alto) ✓
- `sexo_1 = 0, sexo_2 = 1` (es sexo 2) ✓
- `ciudad_Cuenca = 1`, resto = 0 ✓
- Las mismas columnas que en el entrenamiento, en el mismo orden ✓

### Paso 5: Calcular distancias y predecir
```python
neighbors_idx, neighbors_dists, pred = knn_predict(X.to_numpy(), y, x_new.to_numpy()[0], k=3)
```

Ahora KNN puede comparar números y encontrar los 3 vecinos más cercanos.

---

## Resumen visual

```
┌─────────────────┐
│  CSV sin procesar │
│ (texto + números) │
└────────┬─────────┘
         │
         ▼
┌─────────────────────┐
│ FeatureTransformer  │
│      .fit()         │
└────────┬─────────────┘
         │
         ├─► Aprende: qué ciudades, qué sexos, media/std de edad
         │
         ▼
┌─────────────────────┐
│ FeatureTransformer  │
│    .transform()     │
└────────┬─────────────┘
         │
         ├─► Colesterol: texto → números (0, 1, 2, 3)
         ├─► Ciudad: una columna → 6 columnas dummy
         ├─► Sexo: una columna → 2 columnas dummy
         ├─► Edad: números crudos → escalados (media 0, std 1)
         │
         ▼
┌──────────────────────┐
│ Tabla numérica lista │
│    para KNN          │
└──────────────────────┘
         │
         ▼
    Distancia euclídea → K-Nearest Neighbors → Predicción
```

---

## Preguntas frecuentes

### ¿Por qué separar fit y transform?
- **fit** aprende una sola vez de los datos de entrenamiento.
- **transform** aplica esas reglas aprendidas a cualquier dato nuevo.
- Si mezclaras ambas, cada vez que predices tendrías diferentes columnas y escalas.

### ¿Qué pasa si un paciente nuevo tiene una ciudad que no existía en el entrenamiento?
- `transform` crea sus dummies (solo su ciudad = 1, el resto = 0).
- Luego rellena con 0 todas las ciudades del entrenamiento que no estén.
- Resultado: ciudades nuevas se ignoran (todas las columnas del entrenamiento = 0).

### ¿Por qué usar ddof=0 en std?
- `ddof=0` calcula la desviación estándar poblacional (divide entre n).
- `ddof=1` calcula la desviación estándar muestral (divide entre n-1).
- `StandardScaler` de sklearn usa `ddof=0`, así que nosotros también para consistencia.

### ¿Por qué el orden de columnas importa?
- KNN compara índice por índice: primer número con primer número, segundo con segundo, etc.
- Si el orden cambia entre entrenamiento y predicción, comparas edad con colesterol por error.
- Por eso usamos `sorted()` y `reindex()` para forzar un orden consistente.

