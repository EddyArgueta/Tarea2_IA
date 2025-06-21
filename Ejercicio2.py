#✏️Ejercicio 2: Análisis del Clima
#Utilice el archivo clima.csv para analizar los datos climáticos:
#1. Cargue el dataset y conviértelo en un DataFrame.
#2. Calcule la temperatura promedio de cada ciudad.
#3. Determine el registro con la temperatura más alta y el más bajo en el dataset.
#4. Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.
#5. Encuentre cuántos registros tienen una temperatura mayor a 30°C.
#6. Cuenta cuántos días en total hay registrados por cada ciudad.

# Empezaremos, como siempre, cargando los datos
import pandas as pd

clima = pd.read_csv("clima.csv")

# Metodo para definir la temperatura promedio por ciudad
temp_promedio = clima.groupby("Ciudad")["Temperatura"].mean()

# Metodos para el registro  con la temperatura más alta y más baja
registro_max = clima.loc[clima["Temperatura"].idxmax()]
registro_min = clima.loc[clima["Temperatura"].idxmin()]

# Metodos para definir la ciudad con la temperatura más alta y más baja
ciudad_max = registro_max["Ciudad"]
ciudad_min = registro_min["Ciudad"]

# Metodo para ver cuántos registros hay con temperatura > 30 °C
mayor_30 = clima[clima["Temperatura"] > 30].shape[0]

# Metodo para definir el total de días registrados por ciudad
dias_por_ciudad = clima["Ciudad"].value_counts()

# Resultados
print(temp_promedio)
print("Temp más alta:", registro_max)
print("Temp más baja:", registro_min)
print("Ciudad más calurosa:", ciudad_max)
print("Ciudad más fría:", ciudad_min)
print("Registros > 30°C:", mayor_30)
print("Días por ciudad:\n", dias_por_ciudad)