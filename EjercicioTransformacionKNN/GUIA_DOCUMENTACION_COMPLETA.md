# Guía de Documentación Completa

Este folder contiene documentación detallada sobre cada componente del script `transformaciones_knn.py`.

## Archivos de Documentación

### 1. [INSTRUCCIONES_TRANSFORMACIONES_KNN.md](INSTRUCCIONES_TRANSFORMACIONES_KNN.md)
**Para:** Empezar aquí si es tu primera vez.

Contiene:
- Resumen breve del proyecto.
- Instrucciones paso a paso para reproducir.
- Cómo ejecutar el script.
- Notas pedagógicas.

**Lee esto primero si:** Quieres una visión general rápida.

---

### 2. [EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md)
**Para:** Entender la clase `FeatureTransformer`.

Contiene:
- Explicación de cada atributo (`city_cols`, `sex_cols`, `edad_mean`, `edad_std`, `chol_map`).
- Explicación línea por línea del método `__init__`.
- Explicación línea por línea del método `fit`.
- Explicación línea por línea del método `transform`.
- Flujo completo con ejemplo usando tu dataset.
- Preguntas frecuentes.

**Lee esto si:** Necesitas entender cómo se transforman los datos categoriales a números y cómo se escala edad.

**Conceptos clave:**
- One-hot encoding (dummies).
- Estandarización (StandardScaler).
- Fit vs Transform.

---

### 3. [EXPLICACION_EUCLIDEAN_DISTANCES.md](EXPLICACION_EUCLIDEAN_DISTANCES.md)
**Para:** Entender cómo se calcula distancia entre pacientes.

Contiene:
- Fórmula de distancia euclídea.
- Explicación línea por línea del código.
- Ejemplo completo con números.
- Por qué numpy es eficiente.

**Lee esto si:** Necesitas entender qué significa "vecino más cercano" en KNN.

**Conceptos clave:**
- Distancia euclídea en espacios multidimensionales.
- Broadcasting de numpy.

---

### 4. [EXPLICACION_KNN_PREDICT.md](EXPLICACION_KNN_PREDICT.md)
**Para:** Entender el corazón del algoritmo KNN.

Contiene:
- Explicación línea por línea de `knn_predict`.
- `argsort`: cómo ordenar por distancias.
- Votación mayoritaria.
- Ejemplo completo paso a paso.
- Comparación con sklearn.

**Lee esto si:** Quieres entender cómo KNN toma una decisión con votación mayoritaria.

**Conceptos clave:**
- K vecinos más cercanos.
- Votación mayoritaria.
- El parámetro k.

---

### 5. [EXPLICACION_LOAD_DATASET_Y_MAIN.md](EXPLICACION_LOAD_DATASET_Y_MAIN.md)
**Para:** Entender el flujo general y las funciones de infraestructura.

Contiene:
- Explicación de `load_dataset`: carga CSV.
- Explicación de `main`: coordina todo.
- Explicación línea por línea de ambas.
- Diagrama del flujo completo.

**Lee esto si:** Quieres entender cómo todo se conecta.

---

## Flujo de lectura recomendado

### Opción A: Principiante (quiero entender paso a paso)

1. **[INSTRUCCIONES_TRANSFORMACIONES_KNN.md](INSTRUCCIONES_TRANSFORMACIONES_KNN.md)** — Visión general (5 min).
2. **[EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md)** — Transformación de datos (20 min).
3. **[EXPLICACION_EUCLIDEAN_DISTANCES.md](EXPLICACION_EUCLIDEAN_DISTANCES.md)** — Distancias (10 min).
4. **[EXPLICACION_KNN_PREDICT.md](EXPLICACION_KNN_PREDICT.md)** — Predicción (15 min).
5. **[EXPLICACION_LOAD_DATASET_Y_MAIN.md](EXPLICACION_LOAD_DATASET_Y_MAIN.md)** — Conexión total (10 min).

**Total:** ~60 minutos. Resultado: entiendes absolutamente todo.

### Opción B: Tengo prisa (solo lo esencial)

1. **[INSTRUCCIONES_TRANSFORMACIONES_KNN.md](INSTRUCCIONES_TRANSFORMACIONES_KNN.md)** — Visión general (5 min).
2. **[EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md)** (secciones "Qué es y para qué sirve" + "Flujo completo con ejemplo") — (10 min).
3. **[EXPLICACION_KNN_PREDICT.md](EXPLICACION_KNN_PREDICT.md)** (secciones "Qué es y para qué sirve" + "Ejemplo completo") — (10 min).

**Total:** ~25 minutos. Resultado: entiendes el concepto.

### Opción C: Solo quiero ejecutar (sin aprender)

1. [INSTRUCCIONES_TRANSFORMACIONES_KNN.md](INSTRUCCIONES_TRANSFORMACIONES_KNN.md) — Lee "Cómo ejecutarlo".
2. Ejecuta el script.
3. Listo.

---

## Mapa de conceptos

```
┌────────────────────────────────────────────────────────┐
│                 FLUJO GENERAL KNN                       │
└────────────────────────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    ┌────────┐    ┌────────────┐   ┌─────────┐
    │  Datos │    │ Transformar│   │  Cargar │
    │ crudos │    │            │   │  CSV    │
    └────────┘    └────────────┘   └─────────┘
         │               │               │
         └───────────────┼───────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────┐
        │  FeatureTransformer.transform()      │
        │  (VER: EXPLICACION_FEATURE_...)     │
        │                                      │
        │  Tareas:                             │
        │  • Dummy encode: ciudad, sexo        │
        │  • Ordinal encode: colesterol        │
        │  • Estandarizar: edad                │
        └─────────────────────────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────┐
        │        X = matriz numérica           │
        │        y = etiquetas (0, 1)          │
        │        x_new = nuevo paciente        │
        └─────────────────────────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────┐
        │  euclidean_distances()               │
        │  (VER: EXPLICACION_EUCLIDEAN_...)   │
        │                                      │
        │  Calcula: distancia nuevo a todos    │
        │  Resultado: array de distancias      │
        └─────────────────────────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────┐
        │  knn_predict()                       │
        │  (VER: EXPLICACION_KNN_PREDICT...)  │
        │                                      │
        │  Tareas:                             │
        │  • Ordena por distancia              │
        │  • Toma k=3 vecinos                  │
        │  • Votación mayoritaria              │
        │  Resultado: predicción (0 o 1)       │
        └─────────────────────────────────────┘
                         │
                         ▼
           ┌─────────────────────────────┐
           │ Predicción final + vecinos  │
           └─────────────────────────────┘
```

---

## Preguntas rápidas

### "¿Dónde explican ONE-HOT ENCODING?"
→ [EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md), sección sobre `pd.get_dummies`.

### "¿Dónde explican ESTANDARIZACIÓN?"
→ [EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md), sección sobre `edad_scaled`.

### "¿Cómo funciona DISTANCIA EUCLÍDEA?"
→ [EXPLICACION_EUCLIDEAN_DISTANCES.md](EXPLICACION_EUCLIDEAN_DISTANCES.md), toda la sección "La fórmula" y "Ejemplo completo".

### "¿Cómo vota KNN?"
→ [EXPLICACION_KNN_PREDICT.md](EXPLICACION_KNN_PREDICT.md), sección sobre `np.mean(votes)`.

### "¿Por qué separar fit y transform?"
→ [EXPLICACION_FEATURE_TRANSFORMER.md](EXPLICACION_FEATURE_TRANSFORMER.md), sección "Preguntas frecuentes".

### "¿Cómo ejecuto el programa?"
→ [INSTRUCCIONES_TRANSFORMACIONES_KNN.md](INSTRUCCIONES_TRANSFORMACIONES_KNN.md) o [EXPLICACION_LOAD_DATASET_Y_MAIN.md](EXPLICACION_LOAD_DATASET_Y_MAIN.md), sección "Cómo ejecutar".

---

## Glosario

| Término | Explicado en | Significado simple |
|---------|--------------|-------------------|
| One-hot encoding | EXPLICACION_FEATURE_TRANSFORMER.md | Convertir categorías en columnas 0/1 |
| Dummy variable | EXPLICACION_FEATURE_TRANSFORMER.md | Columna 0/1 que representa una categoría |
| Estandarización | EXPLICACION_FEATURE_TRANSFORMER.md | Escalar números a media 0, desviación 1 |
| Distancia euclídea | EXPLICACION_EUCLIDEAN_DISTANCES.md | Distancia en línea recta en espacio multidimensional |
| K-Nearest Neighbors | EXPLICACION_KNN_PREDICT.md | Algoritmo que busca los k vecinos más cercanos |
| Votación mayoritaria | EXPLICACION_KNN_PREDICT.md | Decisión por mayoría de votos |
| Broadcasting | EXPLICACION_EUCLIDEAN_DISTANCES.md | Operación de numpy que expande arrays automáticamente |
| Feature | Todo | Una característica o columna de datos |
| Fit | EXPLICACION_FEATURE_TRANSFORMER.md | Aprender la estructura de los datos |
| Transform | EXPLICACION_FEATURE_TRANSFORMER.md | Aplicar transformaciones aprendidas |

---

## Archivos del proyecto

```
EjercicioTransformacionKNN/
├── transformaciones_knn.py              (script principal)
├── data.csv                             (datos de entrada)
├── INSTRUCCIONES_TRANSFORMACIONES_KNN.md
├── EXPLICACION_FEATURE_TRANSFORMER.md   ← Empieza aquí
├── EXPLICACION_EUCLIDEAN_DISTANCES.md
├── EXPLICACION_KNN_PREDICT.md
├── EXPLICACION_LOAD_DATASET_Y_MAIN.md
└── GUIA_DOCUMENTACION_COMPLETA.md       (este archivo)
```

---

## Notas importantes

- **Todo es manual:** No usamos sklearn para KNN (excepto para demostración). Eso significa que aprendes el algoritmo realmente.
- **Paso a paso:** Cada documento explica línea por línea. No se presupone conocimiento previo.
- **Ejemplos numéricos:** Todos los conceptos tienen ejemplos con números reales.
- **Código comentado:** El script tiene comentarios que corresponden a esta documentación.

---

## Siguientes pasos

Una vez que entiendas todo esto, puedes:

1. **Modificar `k`:** Cambiar `k=3` a `k=5` y ver cómo cambian las predicciones.
2. **Agregar pacientes nuevos:** Crear más ejemplos en `main()`.
3. **Usar el transformador en producción:** Guardar el transformador con `pickle` y usarlo después.
4. **Comparar con sklearn:** Implementar lo mismo con `KNeighborsClassifier` y comparar resultados.
5. **Mejorar el código:** Agregar validación de entrada, manejo de errores, etc.

---

**¿Preguntas?** Busca en los archivos md correspondientes o lee los ejemplos específicamente.
