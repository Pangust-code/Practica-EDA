# Guia de Redaccion del Informe Final

Este archivo te dice que escribir en cada seccion del informe para que quede alineado con la guia del Word y con los resultados reales del proyecto.

## 1. Portada

Incluye:
- Titulo de la practica
- Materia
- Nombre del estudiante
- Docente
- Fecha

## 2. Introduccion (1 parrafo)

Texto sugerido:
"El presente trabajo desarrolla un analisis exploratorio de datos sobre un conjunto real de enfermedad cardiaca de UCI. El objetivo es comprender la estructura del dataset, evaluar su calidad, extraer patrones iniciales y formular hipotesis que orienten etapas posteriores de modelado predictivo."

## 3. Objetivos

- Reforzar fundamentos de analisis exploratorio de datos.
- Aplicar tecnicas de extraccion de caracteristicas a un dataset real.
- Presentar resultados, conclusiones y pasos siguientes.

## 4. Descripcion del dataset

Escribe:
- Fuente oficial de UCI.
- 303 observaciones.
- 15 variables incluyendo Y.
- Definicion de Y: target (0 sin enfermedad, 1 con enfermedad).
- Proporcion de Y=1: 45.87%.

## 5. Metodologia aplicada

Describe en orden:
1. Carga y tipificacion de datos.
2. Deteccion de faltantes y duplicados.
3. Estadistica descriptiva.
4. Visualizacion (histograma, scatter, barras, boxplot, heatmap).
5. Analisis de frecuencias categoricas.
6. Correlacion con Y.
7. Deteccion de outliers por IQR.
8. Imputacion de faltantes (ca mediana, thal moda).
9. Segmentacion por edad y sexo.
10. Formulacion de hipotesis.

## 6. Resultados principales

### 6.1 Calidad de datos
- Faltantes antes: 6
- Faltantes despues: 0
- Duplicados: reportar valor del archivo de salida.

### 6.2 Correlaciones con Y
- thal (0.5221)
- ca (0.4600)
- exang (0.4319)

Conclusion breve:
"Estas tres variables muestran la mayor asociacion lineal con la variable objetivo y son candidatas prioritarias para modelado."

### 6.3 Outliers
Resume tabla IQR y cierra con:
"Se recomienda no eliminar automaticamente los outliers por posible relevancia clinica."

### 6.4 Segmentacion
Comenta diferencias de tasa de target entre grupos de edad y sexo usando los CSV de salida.

## 7. Hipotesis iniciales

1. Menor thalach y mayor oldpeak aumentan la probabilidad de enfermedad.
2. Ciertas categorias de cp y exang se asocian con mayor riesgo.
3. La prevalencia de Y=1 aumenta con la edad.

## 8. Conclusiones (3 a 5 puntos)

- El EDA permitio entender la distribucion y calidad del dataset.
- La imputacion resolvio faltantes sin eliminar registros.
- Se identificaron variables clinicas prioritarias para clasificacion.
- El analisis visual y de frecuencias respalda diferencias entre clases.
- El proyecto deja base lista para modelado supervisado.

## 9. Recomendaciones

- Ejecutar modelos de clasificacion con validacion cruzada.
- Comparar precision, recall, F1 y AUC.
- Evaluar importancia de variables y estabilidad del modelo.
- Validar hallazgos con criterio de dominio clinico.

## 10. Evidencias a anexar

Adjuntar o citar:
- output/REPORTE_FINAL_EDA.md
- output/04_resumen_estadistico.csv
- output/05_frecuencias_categoricas.csv
- output/09_top3_correlacion_Y.csv
- output/06_outliers_iqr.csv
- output/plots/*.png
