# Guia de interpretacion de graficas - Titanic

Este documento explica como leer las graficas generadas en la carpeta `output/plots` del analisis de Titanic.

## 1. Histograma de edad
Grafica: `01_hist_age.png`

Que muestra:
- Distribucion de pasajeros por edad.
- Curva KDE con la densidad estimada.

Como interpretarla:
- Picos indican tramos de edad con mayor cantidad de pasajeros.
- La forma general (asimetria, colas) ayuda a detectar si predominan ciertos grupos etarios.
- Si hay cola hacia edades altas, son menos frecuentes pero presentes.

Evita este error:
- No confundir frecuencia de edades con probabilidad de supervivencia.

## 2. Scatter edad vs tarifa por supervivencia
Grafica: `02_scatter_age_fare.png`

Que muestra:
- Eje X: `Age`.
- Eje Y: `Fare`.
- Color: `Survived` (0 no sobrevivio, 1 sobrevivio).

Como interpretarla:
- Busca zonas donde predomine un color (supervivientes o no supervivientes).
- Si a tarifas altas hay mayor proporcion de `Survived=1`, puede existir asociacion positiva de `Fare` con supervivencia.
- Si los colores se mezclan mucho, estas dos variables por si solas no separan completamente la clase.

Evita este error:
- No concluir causalidad directa (pagar mas no "causa" sobrevivir).

## 3. Barras de clase de boleto por supervivencia
Grafica: `03_bar_pclass_survived.png`

Que muestra:
- Conteo por `Pclass` (1, 2, 3).
- Barras divididas por `Survived`.

Como interpretarla:
- Compara dentro de cada clase si hay mas sobrevivientes o no sobrevivientes.
- Si en primera clase hay mas proporcion de supervivencia, respalda la hipotesis de ventaja por clase socioeconomica.
- Si en tercera clase domina no supervivencia, sugiere mayor vulnerabilidad en ese grupo.

Evita este error:
- No usar solo conteos absolutos; verifica tambien tasas relativas por clase.

## 4. Boxplot de tarifa por supervivencia
Grafica: `04_boxplot_fare_survived.png`

Que muestra:
- Distribucion de `Fare` separada por `Survived`.
- Mediana, rango intercuartil y outliers.

Como interpretarla:
- Mediana mas alta en `Survived=1` sugiere asociacion positiva entre tarifa y supervivencia.
- Cajas anchas indican mayor variabilidad en tarifas.
- Outliers altos representan boletos de tarifa muy superior al resto.

Evita este error:
- No eliminar outliers automaticamente; pueden ser informacion real de pasajeros premium.

## 5. Heatmap de correlacion
Grafica: `05_heatmap_correlacion.png`

Que muestra:
- Correlacion entre variables numericas (`Survived`, `Pclass`, `Fare`, `Age`, etc.).

Como interpretarla:
- Revisa la columna/fila de `Survived` para priorizar variables.
- Correlacion negativa con `Pclass` indica menor supervivencia al aumentar el numero de clase.
- Correlacion positiva con `Fare` sugiere mayor supervivencia en tarifas mas altas.

Evita este error:
- Correlacion no implica causalidad.
- Variables con baja correlacion individual pueden aportar en conjunto dentro de un modelo.

## Lectura integrada recomendada
1. Inicia con histograma para contexto poblacional.
2. Sigue con barras y boxplot para diferencias entre clases de supervivencia.
3. Usa scatter para detectar patrones mixtos entre edad, tarifa y clase objetivo.
4. Finaliza con heatmap para priorizar variables de modelado.
