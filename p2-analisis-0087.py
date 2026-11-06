# Alonso Lopez Garcia NC = 0087 | Fecha 06/11/2026
# Importar librerias 
import pandas as pd
import numpy as np
print("Analisis de datos Vehiculos | Alonso López García NC = 0087")
vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Gasolina", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}
df = pd.DataFrame(vehiculos)
print(df)
print("----- Agrupar por una sola columna ----- 0087")
Motorcito = df.groupby("Tipo_Motor")
print(Motorcito)
print("----- Autonomia por KM ----- 0087")
# Autonomia promedio por KM
print(Motorcito["Autonomia_Km"].mean())
# Precio Maximo por departamento
print("----- Precio USD -----")
print(Motorcito["Precio_USD"].max())
