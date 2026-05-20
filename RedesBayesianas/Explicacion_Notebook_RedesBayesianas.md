# Resumen Explicativo del Proyecto: Redes Bayesianas y Predicción de Potabilidad

Este documento describe detalladamente el contenido y el propósito del cuaderno interactivo `Informe_RedesBayesianas.ipynb`, así como las características del dataset utilizado en el modelado.

---

## 1. ¿De qué trata el Jupyter Notebook?

El cuaderno es un informe y práctica interactiva centrada en la **evaluación probabilística y predictiva de la calidad del agua**. Está contextualizado en el entorno local (ríos de Cuenca y la gestión de ETAPA EP) y se divide en dos enfoques de la inteligencia artificial:

1. **Enfoque Probabilístico Teórico (Redes Bayesianas):** Se plantea cómo eventos encadenados (Lluvias Fuertes → Alta Turbiedad) afectan la probabilidad final de que el agua sea potable o suponga un riesgo.
2. **Enfoque de Machine Learning (Clasificación):** Implementación de un modelo **Naive Bayes Gaussiano** para predecir matemáticamente si el agua es apta para el consumo basándose en una serie de mediciones químicas reales.

---

## 2. Datasheet: Información del Conjunto de Datos

Para que el modelo aprenda a clasificar el agua, se carga el archivo `mini_water_dataset.csv` (un subconjunto procesado del dataset *Water Quality*). 

### Variables Independientes (Características Químicas - `X`)
El dataset está compuesto por 9 variables predictoras, todas con valores numéricos continuos:
*   **ph:** Nivel de acidez o alcalinidad del agua (rango óptimo aproximado 6.5 - 8.5).
*   **Hardness (Dureza):** Capacidad del agua para precipitar jabón, causada principalmente por calcio y magnesio.
*   **Solids (Sólidos Disueltos Totales):** Cantidad de minerales y sales disueltas en el agua (mg/L).
*   **Chloramines (Cloraminas):** Compuestos de cloro y amoníaco usados como desinfectantes en sistemas públicos de agua.
*   **Sulfate (Sulfatos):** Sustancias de ocurrencia natural presentes en el agua.
*   **Conductivity (Conductividad):** Capacidad del agua para conducir corriente eléctrica (relacionada con la concentración de iones).
*   **Organic_carbon (Carbono Orgánico):** Medición del contenido de carbono de los compuestos orgánicos en el agua.
*   **Trihalomethanes (Trihalometanos):** Químicos que se pueden encontrar en el agua tratada con cloro.
*   **Turbidity (Turbidez):** Medida de la claridad del agua (relacionada con la materia en suspensión).

### Variable Dependiente (Etiqueta Objetivo - `y`)
*   **Potability (Potabilidad):** Indica si el agua es segura para el consumo humano.
    *   `1` = Potable (Apta para consumo).
    *   `0` = No Potable (No apta para consumo).

---

## 3. Estructura y Flujo del Código

El archivo `.ipynb` sigue un flujo clásico de ciencia de datos:

1.  **Exploración de la Red Bayesiana:** Definición de probabilidades condicionales empíricas $P(Riesgo | Turbiedad)$ y $P(Turbiedad | Lluvias)$.
2.  **Carga de Datos:** Lectura del archivo CSV usando la librería `pandas`.
3.  **Separación de Variables:** División de los datos entre características químicas (`X`) y la etiqueta a predecir (`y`).
4.  **Entrenamiento del Modelo:** Se instancia `GaussianNB` (de la librería `scikit-learn`) porque se asume que las variables predictoras siguen una distribución normal o gaussiana, lo cual es ideal para lecturas continuas.
5.  **Predicción / Simulación:** Se generan dos samples o muestras "sintéticas" que representan casos locales:
    *   **Muestra 1 (Río Tomebamba Creciente):** Turbidez alta y aumento crítico de sólidos.
    *   **Muestra 2 (Río Yanuncay Post-Filtro):** Condiciones controladas y turbidez baja.
6.  **Inferencia y Conclusiones:** El algoritmo devuelve la etiqueta final (`0` o `1`) para estas dos nuevas muestras basándose en los patrones estadísticos aprendidos del dataset principal.