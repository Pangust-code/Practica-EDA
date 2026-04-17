# Guia para Presentacion (PDF o PPTX) - Titanic

## Diapositiva 1 - Titulo
### Contenido visual
- Titulo grande: "Analisis Exploratorio del Titanic"
- Subtitulo: "Supervivencia por clase, genero y edad"
- Datos academicos: materia, estudiantes, docente y fecha

### Que decir (guion)
En esta presentacion mostraremos los hallazgos principales del datasheet del Titanic, enfocandonos en las graficas y en los patrones de supervivencia mas relevantes.

## Diapositiva 2 - Datasheet: contexto y objetivo
### Contenido visual
- Nombre del dataset: Titanic
- Uso: EDA y clasificacion binaria
- Pregunta central: que factores se asocian a la supervivencia

### Que decir (guion)
Esta presentacion resume el datasheet del Titanic. El objetivo fue identificar patrones de supervivencia y dejar una base limpia para modelado, sin asumir causalidad directa.

## Diapositiva 3 - Datasheet: composicion del dataset
### Contenido visual
- Fuente: repositorio publico de Titanic
- Observaciones: 891
- Variables: 12
- Variable objetivo Y: Survived (0 no sobrevivio, 1 sobrevivio)
- Tasa global de supervivencia: 38.38%
- Link: https://www.kaggle.com/c/titanic/data

### Que decir (guion)
El dataset contiene 891 pasajeros y 12 variables. La variable objetivo es Survived. Solo el 38.38% sobrevivio, por lo que existe una diferencia clara entre clases objetivo.

## Diapositiva 4 - Datasheet: calidad de datos y tratamiento
### Contenido visual
- Faltantes antes: 866
- Faltantes despues: 0
- Duplicados: 0
- Imputacion aplicada: Age mediana, Embarked moda, Fare mediana, Cabin='Unknown'

### Que decir (guion)
Antes de analizar patrones, se aseguro calidad del dato. Se resolvieron faltantes sin perder filas, para mantener la mayor cantidad de informacion posible.

## Diapositiva 5 - Grafica 1: histograma de edad
### Contenido visual
- Imagen: output/plots/01_hist_age.png
- Puntos clave: concentracion de edades y dispersion

### Que decir (guion)
Esta grafica muestra como se distribuyen las edades. Se observa concentracion en adultos jovenes y adultos, lo que da contexto demografico para interpretar supervivencia.

## Diapositiva 6 - Grafica 2: scatter edad vs tarifa
### Contenido visual
- Imagen: output/plots/02_scatter_age_fare.png
- Ejes: Age y Fare
- Color: Survived

### Que decir (guion)
El scatter permite ver mezcla y separacion parcial entre sobrevivientes y no sobrevivientes segun edad y tarifa. No separa totalmente las clases, pero aporta patron visual.

## Diapositiva 7 - Grafica 3: barras por clase y supervivencia
### Contenido visual
- Imagen: output/plots/03_bar_pclass_survived.png
- Comparacion de Survived dentro de cada Pclass

### Que decir (guion)
Aqui se observa el efecto de clase social. La supervivencia es mayor en primera clase y cae hacia tercera, lo cual respalda una brecha socioeconomica en el evento.

## Diapositiva 8 - Grafica 4: lineas por genero y clase
### Contenido visual
- Imagen: output/plots/04_line_survival_sex_class.png
- Linea azul: male
- Linea naranja: female

### Que decir (guion)
Esta es la grafica clave del analisis. Las mujeres tienen mayor supervivencia que los hombres en las tres clases. Ademas, la supervivencia cae de clase 1 a 3 en ambos generos. Tambien se aprecia que hombres de segunda y tercera clase tienen probabilidades muy bajas.

## Diapositiva 9 - Grafica 5: heatmap de correlacion
### Contenido visual
- Imagen: output/plots/05_heatmap_correlacion.png
- Top correlaciones con Y: Pclass, Fare, Parch

### Que decir (guion)
El heatmap resume relaciones lineales. Pclass muestra asociacion negativa con supervivencia y Fare asociacion positiva. Esto ayuda a priorizar variables para modelado.

## Diapositiva 10 - Conclusiones
### Contenido visual
1. Se aseguro calidad del dato y se eliminaron faltantes.
2. Se confirmo fuerte brecha por genero en supervivencia.
3. Se evidencio efecto de clase social en la probabilidad de sobrevivir.
4. Pclass y Fare son variables prioritarias para modelado.
5. El analisis es asociativo, no causal.

### Que decir (guion)
En conclusion, el EDA del Titanic permitio comprender patrones robustos de supervivencia y dejar una base metodologica clara para entrenar y evaluar modelos predictivos.

