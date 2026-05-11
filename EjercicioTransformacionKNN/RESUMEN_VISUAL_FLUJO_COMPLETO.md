# Resumen Visual: Flujo Completo KNN

Esta hoja es un **resumen ejecutivo** del programa. Úsalo como referencia rápida.

---

## El Proceso en 5 Pasos

```
┌─────────────────────────────────────────────────────────┐
│ PASO 1: CARGAR DATOS                                    │
├─────────────────────────────────────────────────────────┤
│ Función: load_dataset()                                 │
│ Lee: data.csv                                           │
│ Resultado:                                              │
│                                                          │
│   sexo  ciudad     colesterol  edad  diabetes           │
│   1      Cuenca    bajo        18     no                │
│   2      Quito     alto        52     si                │
│   2      Guayaquil medio       34     no                │
│   ...    ...       ...         ...    ...               │
│                                                          │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ PASO 2: PREPARAR Y ESCALAR DATOS                        │
├─────────────────────────────────────────────────────────┤
│ Función: FeatureTransformer.fit() + .transform()        │
│                                                          │
│ Transformaciones:                                       │
│ • "bajo" → 0, "medio" → 1, "alto" → 2, "muy alto" → 3 │
│ • "no" → 0, "sí" → 1                                    │
│ • Cuenca → [1, 0, 0, 0, 0, 0]                          │
│ • Quito  → [0, 0, 0, 0, 0, 1]                          │
│ • sexo 1 → [1, 0]                                       │
│ • sexo 2 → [0, 1]                                       │
│ • edad 50 → (50 - media) / std = 0.233                 │
│                                                          │
│ Resultado: MATRIZ NUMÉRICA (6 pacientes × 10 números)  │
│                                                          │
│   edad_scaled  col_ord  sexo_1  sexo_2  ciudad_Amb ...  │
│   -1.71        0        1       0       0           ...  │
│   0.35         2        0       1       0           ...  │
│   ...          ...      ...     ...     ...         ...  │
│                                                          │
│ Etiquetas: [0, 1, 0, 1, 0, 1]  (no, sí, no, sí, ...)  │
│                                                          │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ PASO 3: NUEVO PACIENTE A PREDECIR                       │
├─────────────────────────────────────────────────────────┤
│ Transformar: sexo=2, ciudad=Cuenca, col=alto, edad=50  │
│                                                          │
│ Resultado:                                              │
│ x_new = [0.233, 2.0, 0, 1, 1, 0, 0, 0, 0, 0]          │
│         ↑      ↑   ↑  ↑  ↑                              │
│        edad  col sexo sexo ciudad                       │
│       escal ord  1   2   Cuenca                         │
│                                                          │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ PASO 4: CALCULAR DISTANCIAS                             │
├─────────────────────────────────────────────────────────┤
│ Función: euclidean_distances()                          │
│                                                          │
│ Fórmula: d = sqrt((x1-a1)² + (x2-a2)² + ... + (xn-an)²)│
│                                                          │
│ Para cada paciente de entrenamiento:                    │
│ • Paciente 0: distancia = 3.28                          │
│ • Paciente 1: distancia = 1.42  ← MÁS CERCANO         │
│ • Paciente 2: distancia = 1.98                          │
│ • Paciente 3: distancia = 2.05                          │
│ • Paciente 4: distancia = 1.55  ← 2ª MÁS CERCANO      │
│ • Paciente 5: distancia = 2.30                          │
│                                                          │
│ Resultado: [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]        │
│                                                          │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ PASO 5: KNN - VOTAR CON K=3 VECINOS MÁS CERCANOS      │
├─────────────────────────────────────────────────────────┤
│ Función: knn_predict()                                  │
│                                                          │
│ Ordenar por distancia (menor primero):                  │
│   1. Paciente 1 (dist 1.42)  → diabetes = 1 (SÍ)       │
│   2. Paciente 4 (dist 1.55)  → diabetes = 0 (NO)       │
│   3. Paciente 2 (dist 1.98)  → diabetes = 0 (NO)       │
│                                                          │
│ Votación: 2 votos NO, 1 voto SÍ                         │
│ Promedio: (1 + 0 + 0) / 3 = 0.333                       │
│ Redondear: round(0.333) = 0                             │
│                                                          │
│ ¿PREDICCIÓN? 0 = NO DIABETES                            │
│                                                          │
│ Salida:                                                 │
│ • Vecinos: [1, 4, 2]                                    │
│ • Distancias: [1.42, 1.55, 1.98]                        │
│ • Predicción: 0                                         │
│                                                          │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
                      FIN
           Predicción: NO DIABETES
```

---

## Las 4 Funciones Principales

### 1️⃣ `FeatureTransformer.fit(df)`
**Qué:** Aprende la estructura de los datos.
**Guarda:**
- Columnas dummy de ciudad: `['ciudad_Ambato', 'ciudad_Cuenca', ...]`
- Columnas dummy de sexo: `['sexo_1', 'sexo_2']`
- Media de edad: `46.17`
- Desviación estándar de edad: `16.48`

**Cuándo se usa:** Una sola vez, con los datos de entrenamiento.

---

### 2️⃣ `FeatureTransformer.transform(df)`
**Qué:** Convierte datos crudos en números usando lo aprendido en `fit`.
**Entrada:** DataFrame con texto.
**Salida:** DataFrame numérico.

**Transformaciones:**
```
colesterol: "alto" → 2
ciudad: "Quito" → [0, 0, 0, 0, 0, 1]
sexo: 2 → [0, 1]
edad: 50 → (50 - 46.17) / 16.48 = 0.233
```

**Cuándo se usa:** Múltiples veces (entrenamiento + nuevos pacientes).

---

### 3️⃣ `euclidean_distances(X_train, x_new)`
**Qué:** Calcula distancia del nuevo paciente a cada uno del entrenamiento.
**Fórmula:** $d = \sqrt{\sum(x_i - y_i)^2}$
**Resultado:** Array de distancias.

**Ejemplo:**
```
X_train = matriz de 6 pacientes × 10 características
x_new = 1 paciente × 10 características
dists = [3.28, 1.42, 1.98, 2.05, 1.55, 2.30]
```

---

### 4️⃣ `knn_predict(X_train, y_train, x_new, k=3)`
**Qué:** Predice usando K vecinos más cercanos.
**Pasos:**
1. Calcula distancias (usa `euclidean_distances`).
2. Ordena por distancia.
3. Toma los k=3 primeros.
4. Vota mayoritariamente.

**Resultado:** Predicción 0 o 1.

---

## Datos Reales del Ejemplo

```
ENTRADA (data.csv):
sexo  ciudad     colesterol  edad  diabetes
1     Cuenca     bajo        18    no
2     Quito      alto        52    si
2     Guayaquil  medio       34    no
1     Loja       alto        61    si
2     Ambato     medio       45    no
1     Machala    muy alto    67    si

NUEVO PACIENTE A PREDECIR:
sexo=2, ciudad=Cuenca, colesterol=alto, edad=50

TRANSFORMADO:
X_train (6 × 10):
[[-1.71  0.   1.  0.  1.  0.  0.  0.  0.  0.]
 [ 0.35  2.   0.  1.  0.  0.  0.  0.  0.  1.]
 [-0.74  1.   0.  1.  0.  0.  1.  0.  0.  0.]
 [ 0.90  2.   1.  0.  0.  1.  0.  0.  0.  0.]
 [-0.07  1.   0.  1.  1.  0.  0.  0.  0.  0.]
 [ 1.26  3.   1.  0.  0.  0.  0.  0.  1.  0.]]

y_train = [0, 1, 0, 1, 0, 1]

x_new (1 × 10):
[0.23  2.   0.  1.  1.  0.  0.  0.  0.  0.]

DISTANCIAS:
[3.28, 1.42, 1.98, 2.05, 1.55, 2.30]

K=3 VECINOS MÁS CERCANOS:
Índice 1: dist 1.42, etiqueta 1 (SÍ)
Índice 4: dist 1.55, etiqueta 0 (NO)
Índice 2: dist 1.98, etiqueta 0 (NO)

VOTACIÓN:
mean([1, 0, 0]) = 0.333
round(0.333) = 0
PREDICCIÓN = 0 (NO DIABETES)
```

---

## Columnas Después de `transform()`

```
Entrada (original):
  sexo  ciudad  colesterol  edad

Salida (numérica):
  edad_scaled      → edad estandarizada (media 0, std 1)
  colesterol_ord   → 0, 1, 2, 3
  sexo_1           → 1 si sexo==1, 0 si no
  sexo_2           → 1 si sexo==2, 0 si no
  ciudad_Ambato    → 1 si ciudad=="Ambato", 0 si no
  ciudad_Cuenca    → 1 si ciudad=="Cuenca", 0 si no
  ciudad_Guayaquil → 1 si ciudad=="Guayaquil", 0 si no
  ciudad_Loja      → 1 si ciudad=="Loja", 0 si no
  ciudad_Machala   → 1 si ciudad=="Machala", 0 si no
  ciudad_Quito     → 1 si ciudad=="Quito", 0 si no
```

Total: 10 columnas (2 + 2 + 6).

---

## Conceptos Clave

| Concepto | Definición | Por qué importa |
|----------|-----------|-----------------|
| **One-hot encoding** | Convertir categoría a columnas 0/1 | KNN necesita números |
| **Estandarización** | Escalar a media 0, std 1 | Igualar escala de variables |
| **Distancia euclídea** | $\sqrt{\sum(x_i - y_i)^2}$ | Medir "parecido" entre pacientes |
| **K vecinos** | Los k más cercanos | Robusto a ruido |
| **Votación mayoritaria** | Decisión por mayoría | Simple y efectivo |

---

## Ejecución Paso a Paso

```bash
$ python transformaciones_knn.py

Salida esperada:

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

## Hoja de Trucos

| Acción | Código |
|--------|--------|
| **Cambiar k a 5** | `knn_predict(..., k=5)` |
| **Ver datos transformados** | `print(X)` |
| **Ver distancias** | `print(dists)` |
| **Cambiar nuevo paciente** | Editar diccionario en `main()` |
| **Guardar transformador** | `import pickle; pickle.dump(transformer, open('transformer.pkl', 'wb'))` |
| **Cargar transformador** | `transformer = pickle.load(open('transformer.pkl', 'rb'))` |

---

## Preguntas de Debugging

**P: ¿Por qué los vecinos son [1, 4, 2] específicamente?**
R: Son los 3 con menor distancia. Paciente 1 está a 1.42, Paciente 4 a 1.55, Paciente 2 a 1.98.

**P: ¿Por qué la predicción es 0?**
R: 2 de 3 vecinos (4 y 2) tienen etiqueta 0. Votación: 0 gana.

**P: ¿Qué significa edad_scaled = 0.233?**
R: La edad (50) está 0.233 desviaciones estándar por encima de la media (46.17).

**P: ¿Por qué estandarizar?**
R: Porque edad está en rango [18-67] y colesterol en [0-3]. Sin estandarizar, edad domina la distancia.

---

## Recursos

| Recurso | Dónde |
|---------|--------|
| Explicación detallada de FeatureTransformer | `EXPLICACION_FEATURE_TRANSFORMER.md` |
| Explicación detallada de distancias | `EXPLICACION_EUCLIDEAN_DISTANCES.md` |
| Explicación detallada de KNN | `EXPLICACION_KNN_PREDICT.md` |
| Guía completa | `GUIA_DOCUMENTACION_COMPLETA.md` |

---

**Última actualización:** May 11, 2026
