# Guia para Presentacion (PDF o PPTX)

Usa estas diapositivas para cumplir exactamente la seccion de presentacion del Word.

## Diapositiva 1 - Descripcion del dataset

- Dataset: Heart Disease (UCI)
- Observaciones: 303
- Variables: 15 (incluyendo Y)
- Variable objetivo Y: target (0 sin enfermedad, 1 con enfermedad)

## Diapositiva 2 - Conclusiones del resumen estadistico

- Rango y dispersion de edad, colesterol, presion y frecuencia cardiaca.
- oldpeak presenta variabilidad y valores altos en subconjuntos de pacientes.
- Se evidencia heterogeneidad clinica util para clasificacion.

## Diapositiva 3 - Conclusiones de visualizaciones

- Histograma de edad: concentracion en adultos medios y mayores.
- Scatter thalach vs oldpeak: separacion parcial por clase objetivo.
- Boxplot colesterol por target: presencia de outliers relevantes.

## Diapositiva 4 - Frecuencias categoricas

- Diferencias por sex, cp y exang entre clases.
- Variables categoricas aportan señal para discriminar riesgo.

## Diapositiva 5 - Top 3 correlaciones con Y

- thal
- ca
- exang

Conclusiones:
- Son variables candidatas de mayor peso para modelado posterior.

## Diapositiva 6 - Outliers y decision

- Outliers detectados por IQR en variables continuas.
- Decision sugerida: no eliminar automaticamente; validar contexto clinico antes de filtrar.

## Diapositiva 7 - Hipotesis iniciales

1. Menor thalach y mayor oldpeak incrementan probabilidad de Y=1.
2. Ciertas categorias de cp y exang tienen mayor tasa de enfermedad.
3. Segmentos de mayor edad muestran mayor prevalencia de Y=1.

## Diapositiva 8 - Cierre

- El EDA permite definir variables clave y estrategia de preprocesamiento.
- Proximo paso: entrenamiento y comparacion de modelos de clasificacion.
