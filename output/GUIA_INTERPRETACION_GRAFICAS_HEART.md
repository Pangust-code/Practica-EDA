# Guia de interpretacion de graficas - Heart Disease

Este documento explica como leer las graficas generadas en la carpeta `output/plots` del analisis de Heart Disease.

## 1. Histograma de edad
Grafica: `01_hist_age.png`

Que muestra:
- Distribucion de pacientes por edad.
- La linea KDE resume la densidad (donde hay mas concentracion de casos).

Como interpretarla:
- Picos altos indican rangos de edad mas frecuentes en el dataset.
- Si la curva se concentra en edades medias/altas, el dataset tiene mayor presencia de adultos y adultos mayores.
- Si hay cola hacia edades altas, existen menos casos pero en edades avanzadas.

Evita este error:
- No concluir riesgo de enfermedad solo por frecuencia. Esta grafica muestra distribucion de edades, no causalidad.

## 2. Scatter thalach vs oldpeak por target
Grafica: `02_scatter_thalach_oldpeak.png`

Que muestra:
- Eje X: `thalach` (frecuencia cardiaca maxima).
- Eje Y: `oldpeak` (depresion ST inducida por ejercicio).
- Color: `target` (0 sin enfermedad, 1 con enfermedad).

Como interpretarla:
- Si los colores se separan en zonas distintas, hay señal util para clasificacion.
- Zonas con `oldpeak` alto y `thalach` bajo suelen asociarse con mayor probabilidad de `target=1`.
- Si hay mezcla fuerte de colores, una sola pareja de variables no separa bien las clases.

Evita este error:
- No interpretar la nube como relacion lineal perfecta. El scatter permite ver patrones, no prueba causa.

## 3. Barras de cp por target
Grafica: `03_bar_cp_target.png`

Que muestra:
- Conteo de cada categoria de `cp` (tipo de dolor de pecho).
- Barras separadas por clase `target`.

Como interpretarla:
- Compara alturas de barras dentro de cada categoria de `cp`.
- Si una categoria concentra mas `target=1`, puede ser una señal discriminativa.
- Diferencias consistentes entre categorias sugieren relevancia de esta variable categorica.

Evita este error:
- No comparar solo conteos absolutos cuando las clases son desbalanceadas; complementa con porcentajes.

## 4. Boxplot de chol por target
Grafica: `04_boxplot_chol_target.png`

Que muestra:
- Distribucion de colesterol (`chol`) para cada clase de `target`.
- Mediana (linea central), IQR (caja) y outliers (puntos fuera de bigotes).

Como interpretarla:
- Si la mediana de un grupo es mayor, ese grupo tiende a valores mas altos de colesterol.
- Cajas mas altas o mas anchas indican mayor dispersion.
- Muchos outliers no implican error automatico; en datos clinicos pueden ser casos reales.

Evita este error:
- No eliminar outliers solo por verse extremos. Primero valida su contexto clinico.

## 5. Heatmap de correlacion
Grafica: `05_heatmap_correlacion.png`

Que muestra:
- Correlaciones lineales entre variables numericas.
- Valores cercanos a 1 o -1 indican relacion lineal fuerte; cercanos a 0, relacion debil.

Como interpretarla:
- Revisa especialmente la fila/columna de `target` para detectar variables candidatas.
- Correlacion positiva: al subir una variable, tiende a subir `target`.
- Correlacion negativa: al subir una variable, tiende a bajar `target`.

Evita este error:
- Correlacion no implica causalidad.
- Una correlacion baja no significa inutilidad total; modelos no lineales pueden captar relacion.

## Lectura integrada recomendada
1. Usa histograma y boxplot para entender distribucion y dispersion.
2. Usa barras y scatter para identificar separacion por clase.
3. Usa heatmap para priorizar variables candidatas.
4. Cruza hallazgos con contexto clinico antes de concluir.
