# Guia para Presentacion (PDF o PPTX)

Usa esta version como guion de exposicion. El objetivo es que puedas hablar con claridad, cubrir la rubrica y defender tus decisiones tecnicas.

## Estructura sugerida

- Duracion total: 7 a 10 minutos
- Tiempo por diapositiva: 45 a 75 segundos
- Cierre: 45 segundos

## Diapositiva 1 - Descripcion del dataset

### Contenido visual
- Dataset: Heart Disease (UCI)
- Observaciones: 303
- Variables: 15 (incluyendo Y)
- Variable objetivo Y: target (0 sin enfermedad, 1 con enfermedad)
- Proporcion de clase positiva: 45.87%

### Que decir (guion)
"En esta practica use un dataset real y publico de UCI sobre enfermedad cardiaca. El conjunto contiene 303 observaciones y 15 variables considerando la variable objetivo Y. Defini Y de forma binaria: 0 indica ausencia de enfermedad y 1 presencia de enfermedad. La clase positiva representa 45.87%, por lo que no hay un desbalance extremo y el analisis es adecuado para estudiar patrones clinicos iniciales." 

## Diapositiva 2 - Conclusiones del resumen estadistico

### Contenido visual
- Estadisticas de edad, trestbps, chol, thalach y oldpeak
- Tabla breve con media, mediana y dispersion

### Que decir (guion)
"A nivel descriptivo, la edad se concentra en adultos medios y mayores. La variable oldpeak presenta asimetria y algunos valores altos, lo que sugiere casos de mayor riesgo fisiologico. thalach muestra una variabilidad considerable, lo cual es valioso porque podria ayudar a separar pacientes con y sin enfermedad en etapas posteriores de modelado." 

## Diapositiva 3 - Conclusiones de visualizaciones

### Contenido visual
- Histograma de edad
- Scatter: thalach vs oldpeak por target
- Boxplot: chol por target

### Que decir (guion)
"En las figuras se observa que la distribucion de edad no es uniforme y se concentra en rangos de mediana edad. En el scatter de thalach contra oldpeak se aprecia una separacion parcial por clase objetivo, lo que respalda que hay senal predictiva en estas variables. En el boxplot de colesterol aparecen valores atipicos, pero por contexto clinico no se recomienda eliminarlos automaticamente sin validacion medica." 

## Diapositiva 4 - Analisis de frecuencias categoricas

### Contenido visual
- Tabla o grafica de frecuencias para sex, cp, exang y target

### Que decir (guion)
"El analisis de frecuencia muestra diferencias claras entre categorias segun la clase objetivo. En particular, variables como sex, cp y exang cambian su distribucion entre pacientes con y sin enfermedad. Estas diferencias refuerzan que las variables categoricas aportan informacion relevante para estimar riesgo." 

## Diapositiva 5 - Top 3 correlaciones con Y

### Contenido visual
- thal: 0.5221
- ca: 0.4600
- exang: 0.4319

### Que decir (guion)
"Las tres variables mas correlacionadas con Y fueron thal, ca y exang. Esto no implica causalidad, pero si una relacion lineal importante con la variable objetivo. Por eso, estas variables son candidatas prioritarias para la siguiente etapa de seleccion de atributos y entrenamiento de modelos de clasificacion." 

## Diapositiva 6 - Outliers y decision tecnica

### Contenido visual
- Tabla IQR por variable
- Variables con mayor porcentaje de outliers: trestbps, oldpeak, chol

### Que decir (guion)
"Detecte outliers usando el criterio IQR. La mayor proporcion aparece en trestbps, oldpeak y chol, pero en niveles moderados. La decision tecnica fue conservarlos en esta fase, porque al tratarse de datos clinicos podrian representar casos reales de alto riesgo. Eliminarlos sin criterio de dominio puede ocultar informacion valiosa." 

## Diapositiva 7 - Hipotesis iniciales

### Contenido visual
1. Menor thalach y mayor oldpeak aumentan probabilidad de Y=1.
2. Ciertas categorias de cp y exang elevan la tasa de enfermedad.
3. Grupos de mayor edad presentan mayor prevalencia de Y=1.

### Que decir (guion)
"Con base en la exploracion, formule tres hipotesis iniciales. La primera relaciona menor frecuencia cardiaca maxima y mayor oldpeak con mayor riesgo. La segunda plantea que ciertas categorias de dolor de pecho y angina inducida por ejercicio se asocian con enfermedad. La tercera sugiere mayor prevalencia en segmentos de mayor edad. Estas hipotesis orientan el modelado posterior." 

## Diapositiva 8 - Cierre y pasos siguientes

### Contenido visual
- EDA completo realizado
- Dataset limpio sin faltantes
- Variables candidatas priorizadas
- Proximo paso: modelado y validacion

### Que decir (guion)
"Como conclusion, el EDA permitio comprender la estructura de los datos, resolver faltantes, identificar variables relevantes y documentar hipotesis de trabajo. El siguiente paso natural es construir modelos de clasificacion, comparar metricas como precision, recall y F1, y validar si las hipotesis planteadas se sostienen con evidencia predictiva." 

## Recomendaciones de defensa oral

- Evita leer todo textual: usa el guion como apoyo.
- Cuando te pregunten por decisiones, responde con criterio: "por contexto clinico" y "evitar perdida de informacion".
- Si preguntan por correlacion vs causalidad, aclara que correlacion no demuestra causa.
- Si preguntan por faltantes, indica exactamente: ca por mediana y thal por moda.
