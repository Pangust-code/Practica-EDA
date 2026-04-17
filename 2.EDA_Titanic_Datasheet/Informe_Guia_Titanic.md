# Guia de Redaccion del Informe Final - Titanic

Este archivo te indica que escribir en cada seccion del informe para que quede alineado con la rubrica academica y con los resultados reales del proyecto.

## 1. Portada
Incluye:
- Titulo de la practica: Analisis exploratorio de datos< Extraccion de caracteristicas y presentacion de resultados
- Materia: Inteligencia Artificial
- Nombres de los estudiantes:Est. Valeria Mantilla y Daniel Guanga
- Docente: Ing. Remigio Hurtado

## 2. Introduccion (1 parrafo)
Texto sugerido:
El presente trabajo desarrolla un analisis exploratorio de datos sobre el dataset Titanic. El objetivo es comprender su estructura, evaluar la calidad de los datos, identificar factores asociados a la supervivencia y plantear hipotesis para etapas posteriores de modelado.

## 3. Objetivos
- Reforzar fundamentos de analisis exploratorio de datos.
- Aplicar tecnicas de extraccion de caracteristicas en un dataset real.
- Presentar resultados, conclusiones y pasos siguientes.

## 4. Descripcion del dataset
Escribe:
- Fuente oficial del CSV.
- 891 observaciones.
- 12 variables.
- Definicion de Y: Survived (0 no sobrevivio, 1 sobrevivio).
- Proporcion de Y=1: 38.38%.

## 5. Metodologia aplicada
Describe en orden:
1. Carga y tipificacion de datos.
2. Deteccion de faltantes y duplicados.
3. Estadistica descriptiva.
4. Visualizacion (histograma, scatter, barras de conteo, lineas por sexo/clase y heatmap).
5. Analisis de frecuencias categoricas.
6. Correlacion con Y.
7. Deteccion de outliers por IQR.
8. Imputacion de faltantes.
9. Segmentacion por edad y sexo.
10. Formulacion de hipotesis.

## 6. Resultados principales
### 6.1 Calidad de datos
- Faltantes antes: 866
- Faltantes despues: 0
- Duplicados: 0

### 6.2 Correlaciones con Y
- Pclass (-0.3385)
- Fare (0.2573)
- Parch (0.0816)

Conclusion breve sugerida:
Estas tres variables muestran la mayor asociacion lineal con la variable objetivo y son candidatas prioritarias para modelado.

### 6.3 Outliers
Resume tabla IQR y cierra con:
Se recomienda no eliminar automaticamente los outliers sin evaluar su contexto.

### 6.4 Segmentacion
Comenta diferencias de supervivencia por grupos de edad y por sexo usando los CSV de salida.

## 7. Hipotesis iniciales
1. Las mujeres presentan mayor supervivencia que los hombres.
2. La primera clase presenta mayor supervivencia que clases inferiores.
3. Ninos y adolescentes tienden a mayor supervivencia que adultos mayores.

## 8. Conclusiones (3 a 5 puntos)
- El EDA permitio entender distribucion y calidad de datos.
- La imputacion resolvio faltantes sin perder observaciones.
- Se identificaron variables prioritarias para clasificacion.
- La segmentacion respalda diferencias relevantes entre grupos.
- El proyecto deja base lista para modelado supervisado.

## 9. Recomendaciones
- Ejecutar modelos de clasificacion con validacion cruzada.
- Comparar precision, recall, F1 y AUC.
- Analizar importancia de variables y estabilidad del modelo.

## 10. Evidencias a anexar
Adjuntar o citar:
- output/DATASHEET_TITANIC.md
- output/REPORTE_FINAL_TITANIC.md
- output/04_resumen_estadistico.csv
- output/05_frecuencias_categoricas.csv
- output/09_top3_correlacion_Y.csv
- output/06_outliers_iqr.csv
- output/10_segmentacion_age_group.csv
- output/11_segmentacion_sex.csv
- output/plots/*.png
