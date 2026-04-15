# Guia para Presentacion (PDF o PPTX) - Titanic

## Estructura sugerida
- Duracion total: 7 a 10 minutos
- Tiempo por diapositiva: 45 a 75 segundos
- Cierre: 45 segundos

## Diapositiva 1 - Descripcion del dataset
### Contenido visual
- Dataset: Titanic
- Observaciones: 891
- Variables: 12
- Variable objetivo Y: Survived (0 no sobrevivio, 1 sobrevivio)
- Proporcion de clase positiva: 38.38%

### Que decir (guion)
En esta practica use un dataset historico y publico sobre pasajeros del Titanic. El conjunto contiene 891 observaciones y 12 variables. Defini Y como Survived, donde 0 indica no supervivencia y 1 supervivencia. La clase positiva representa 38.38%, por lo que existe una proporcion menor de sobrevivientes respecto al total de pasajeros.

## Diapositiva 2 - Conclusiones del resumen estadistico
### Contenido visual
- Estadisticas de Age, Fare, SibSp y Parch
- Tabla breve con media, mediana y dispersion

### Que decir (guion)
A nivel descriptivo, la edad presenta dispersion moderada y una concentracion principal en adultos jovenes y adultos. La variable Fare tiene alta variabilidad, lo cual sugiere diferencias de clase economica. Estas diferencias son importantes porque pueden relacionarse con la probabilidad de supervivencia.

## Diapositiva 3 - Conclusiones de visualizaciones
### Contenido visual
- Histograma de edad
- Scatter: Age vs Fare por Survived
- Boxplot: Fare por Survived

### Que decir (guion)
En las visualizaciones se observa que la distribucion de edad no es uniforme y que la tarifa tiene valores extremos. En el scatter de edad y tarifa se aprecia un patron parcial por clase objetivo. En el boxplot, la distribucion de tarifa para sobrevivientes tiende a mostrar valores superiores en comparacion con no sobrevivientes.

## Diapositiva 4 - Analisis de frecuencias categoricas
### Contenido visual
- Tabla o grafica de frecuencias para Sex, Embarked, Pclass y Survived

### Que decir (guion)
El analisis de frecuencia muestra diferencias claras por sexo y clase de boleto. Estas variables categoricas aportan informacion relevante para explicar diferencias de supervivencia entre grupos de pasajeros.

## Diapositiva 5 - Top 3 correlaciones con Y
### Contenido visual
- Pclass: -0.3385
- Fare: 0.2573
- Parch: 0.0816

### Que decir (guion)
Las tres variables numericas mas correlacionadas con Y fueron Pclass, Fare y Parch. Pclass tiene relacion negativa, lo que sugiere menor supervivencia en clases numericamente mas altas (segunda y tercera respecto a primera). Fare presenta relacion positiva y Parch una relacion positiva leve.

## Diapositiva 6 - Outliers y decision tecnica
### Contenido visual
- Tabla IQR por variable
- Variables con mayor porcentaje de outliers: Parch y Fare

### Que decir (guion)
Detecte outliers con criterio IQR. La mayor proporcion se observa en Parch y Fare. La decision fue conservarlos para no perder informacion potencialmente relevante del comportamiento real de los pasajeros.

## Diapositiva 7 - Hipotesis iniciales
### Contenido visual
1. Las mujeres presentan mayor supervivencia que los hombres.
2. Primera clase presenta mayor supervivencia.
3. Ninos y adolescentes presentan mayor supervivencia relativa.

### Que decir (guion)
Con base en los resultados del EDA formule tres hipotesis iniciales orientadas a sexo, clase y edad. Estas hipotesis guian la siguiente fase de modelado para verificar si los patrones se sostienen con evidencia predictiva.

## Diapositiva 8 - Cierre y pasos siguientes
### Contenido visual
- EDA completo realizado
- Dataset tratado sin faltantes
- Variables candidatas priorizadas
- Proximo paso: modelado y validacion

### Que decir (guion)
Como cierre, el EDA permitio entender la estructura del dataset, resolver faltantes, identificar variables relevantes y documentar hipotesis. El siguiente paso es entrenar modelos de clasificacion y comparar metricas como precision, recall, F1 y AUC.

## Recomendaciones de defensa oral
- Evita leer todo textual: usa el guion como apoyo.
- Si te preguntan por correlacion y causalidad, aclara que correlacion no prueba causa.
- Si te preguntan por outliers, justifica la conservacion por valor informativo.
- Si te preguntan por faltantes, indica imputacion: Age mediana, Embarked moda, Fare mediana, Cabin='Unknown'.
