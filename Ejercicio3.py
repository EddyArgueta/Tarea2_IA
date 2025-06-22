#✏️ Ejercicio 3: Estadísticas de Calificaciones
#Utilice el archivo calificaciones.csv para analizar el rendimiento de los estudiantes:
#1. Cargue el dataset y muestre las primeras filas.
#2. Calcule el promedio de calificaciones por materia.
#3. Identifique el estudiante con el promedio más alto.
#4. Agrupa las calificaciones por estudiante y calcule el promedio de cada uno.
#5. Identifique cuántos estudiantes tienen un promedio superior a 85.
#6. Encuentre la materia con la mayor cantidad de calificaciones registradas.
#7. Muestre los 5 estudiantes con el promedio más bajo.
#⚡ Entrega: Suba su código .py o .ipynb, junto con una breve explicación de tus resultados en
#un repositorio de github, envie un txt con el enlace al repositorio

import pandas as pd

# Pra empezar, vamos a cargar el dataset y mostrar las primeras filas
df = pd.read_csv('calificaciones.csv')
print("Primeras filas del dataset:")
print(df.head())

# Metodo para calcular el promedio de calificaciones por materia
promedio_materia = df.groupby('Materia')['Calificación'].mean()
print(f"Promedio por materia: ")
print(promedio_materia)

# Metodo para identificar al estudiante con el promedio más alto
promedio_estudiantes = df.groupby('Estudiante')['Calificación'].mean()
estudiante_top = promedio_estudiantes.idxmax()
print(f"Estudiante con el promedio más alto: {estudiante_top} ({promedio_estudiantes.max():.2f})")

# Agrupamos las calificaciones por estudiante y calculamos el promedio de cada uno
print(f"Promedio por estudiante: ")
print(promedio_estudiantes)

# Metodo para contar cuántos estudiantes tienen un promedio superior a 85
superiores_85 = promedio_estudiantes[promedio_estudiantes > 85]
print(f"Número de estudiantes con promedio superior a 85: {len(superiores_85)}")

# Metodo para identificar la materia con la mayor cantidad de calificaciones registradas
materia_mas_registrada = df['Materia'].value_counts().idxmax()
print(f"Materia con mayor cantidad de calificaciones: {materia_mas_registrada}")

# Metodo para mostrar los 5 estudiantes con el promedio más bajo
peores_5 = promedio_estudiantes.sort_values().head(5)
print("5 estudiantes con el promedio más bajo: ")
print(peores_5)

#En este ejercicio se realizo un analisis de las calificaciones de estudiantes,
#encontrando el promedio de calificaciones por materia, el estudiante con el promedio mas alto,
#el promedio de calificaciones por estudiante, la cantidad de estudiantes con promedio superior a 85,
#la materia con la mayor cantidad de calificaciones registradas y los 5 estudiantes con el promedio mas bajo