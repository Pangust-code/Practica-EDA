import pandas as pd
from sklearn.naive_bayes import GaussianNB

# 1. Cargar el dataset original
df_completo = pd.read_csv('mini_water_dataset.csv')

# Mostrar la tabla final resultante
print(df_completo)

# ==========================================
# FASE 3: MODELADO NAIVE BAYES
# ==========================================

# Separar las características (X) y la etiqueta que queremos predecir (y)
X = df_completo.drop('Potability', axis=1) 
y = df_completo['Potability']

# Inicializar y entrenar (fit) el modelo GaussianNB
modelo_nb = GaussianNB()
modelo_nb.fit(X, y)
print("¡Modelo entrenado con éxito!\n")

# ==========================================
# FASE 4: PREDICCIÓN DE NUEVOS SAMPLES
# ==========================================

# Crear 2 muestras de agua completamente nuevas
nuevos_samples = pd.DataFrame({
    'ph': [3.5, 5.6],                       # Muestra 1 es ácida, Muestra 2 es normal
    'Hardness': [300.0, 190.0],
    'Solids': [40000.0, 13800.0],           # Muestra 1 tiene demasiados sólidos
    'Chloramines': [9.0, 6.5],
    'Sulfate': [200.0, 369.0],
    'Conductivity': [600.0, 420.0],
    'Organic_carbon': [25.0, 18.0],
    'Trihalomethanes': [120.0, 80.0],
    'Turbidity': [6.5, 4.5]                 # Muestra 1 está muy turbia
})

# Realizar la predicción
predicciones = modelo_nb.predict(nuevos_samples)

# Imprimir los resultados
print("Resultados de la Predicción:")
for i, prediccion in enumerate(predicciones):
    estado = "POTABLE" if prediccion == 1 else "NO POTABLE"
    print(f"Sample {i+1} ha sido clasificado como: {estado} (Clase {prediccion})")