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
# Sample 1: Tomebamba en lluvia | Sample 2: Yanuncay filtrado
    'ph': [6.0, 5.7],                       
    'Hardness': [250.0, 180.0],
    'Solids': [28000.0, 14000.0],           # Tomebamba tiene muchos sólidos por la lluvia
    'Chloramines': [4.0, 6.5],              # Yanuncay tiene cloro residual del tratamiento
    'Sulfate': [250.0, 369.0],
    'Conductivity': [300.0, 400.0],
    'Organic_carbon': [12.0, 18.0],
    'Trihalomethanes': [50.0, 80.0],
    'Turbidity': [6.0, 4.0]                 # Tomebamba muy turbio (6.0), Yanuncay claro (4.0)
})

# Realizar la predicción
predicciones = modelo_nb.predict(nuevos_samples)

# Imprimir los resultados con nombres personalizados
nombres_muestras = ["Río Tomebamba (Creciente)", "Río Yanuncay (Post-Filtro)"]

print("--- RESULTADOS DE PREDICCIÓN LOCAL (CUENCA) ---")
for i, prediccion in enumerate(predicciones):
    estado = "POTABLE" if prediccion == 1 else "NO POTABLE"
    print(f"La muestra del {nombres_muestras[i]} ha sido clasificada como: {estado} (Clase {prediccion})")