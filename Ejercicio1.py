#✏️Ejercicio 1: Análisis de Ventas
#Utilice el archivo ventas.csv para responder lo siguiente:
#1. Cargue los datos en un DataFrame.
#2. Calcule la cantidad total de productos vendidos por categoría.
#3. Determine cuál es el producto con el mayor total de ventas.
#4. Encuentre el precio promedio de los productos vendidos.


import pandas as pd

# Lo primero seria cargar los datos
ventas = pd.read_csv("ventas.csv")

# Metodo para obtener el total de ventas por categoria
ventas_por_categoria = ventas.groupby("Producto")["Cantidad"].sum()

# Metodos para obtener el producto mas vendido 
producto_top = ventas_por_categoria.idxmax()
cantidad_top = ventas_por_categoria.max()

# Metodo para obtener el precio promedio
precio_promedio = ventas["Precio_Unitario"].mean()

# Resultados
print(ventas_por_categoria)
print("Producto más vendido:", producto_top, "-", cantidad_top, "unidades")
print("Precio promedio:", precio_promedio)
