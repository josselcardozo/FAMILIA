# Crear la matriz 3D (ciudades x días de la semana x semanas)
ciudades = ['Samborondon', 'Guayaquil', 'Quito']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear una matriz 3D que almacene temperaturas aleatorias entre 20 y 35 grados
import random

# Matriz vacía de temperaturas (ciudades x días x semanas)
temperaturas = [[[random.randint(20, 35) for _ in range(semanas)] for _ in dias] for _ in ciudades]

# Iterar sobre cada ciudad y cada semana para calcular el promedio de temperaturas
for ciudad_index, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias)):
            suma_temperaturas += temperaturas[ciudad_index][dia][semana]

        promedio = suma_temperaturas / len(dias)
        print(f"Semana {semana + 1}: {promedio:.2f}°C")