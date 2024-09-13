def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante el período de tiempo dado.

    Parámetros:
    datos_temperaturas (list): Una lista 2D que contiene las temperaturas de múltiples ciudades
                               para varias semanas. Cada sublista representa una ciudad,
                               y cada valor dentro de la sublista representa la temperatura de una semana.

    Retorna:
    dict: Un diccionario donde las llaves son los nombres de las ciudades y los valores son sus
          temperaturas promedio. Si los datos no son válidos, el promedio será 'Datos inválidos'.
    """
    nombres_ciudades = ["Salitre", "Samborondón", "Daule"]
    promedios_ciudades = {}

    for i, ciudad in enumerate(datos_temperaturas):
        if ciudad and all(isinstance(temp, (int, float)) for temp in ciudad):
            promedio = sum(ciudad) / len(ciudad)  # Calcula el promedio de la ciudad
            if promedio != 0:  # Verifica que el promedio no sea 0
                promedios_ciudades[nombres_ciudades[i]] = promedio
            else:
                promedios_ciudades[nombres_ciudades[i]] = 'Promedio igual a 0'
        else:
            promedios_ciudades[nombres_ciudades[i]] = 'Datos inválidos'

    return promedios_ciudades


# Datos de ejemplo: temperaturas de Salitre, Samborondón y Daule durante 4 semanas
datos_temperaturas = [
    [27, 29, 28, 30],  # Salitre
    [32, 33, 31, 34],  # Samborondón
    [0, 0, 0, 0]  # Daule (promedio es 0)
]

# Llamada a la función
promedios = calcular_temperatura_promedio(datos_temperaturas)

# Mostrar resultados
for ciudad, promedio in promedios.items():
    if isinstance(promedio, str):  # Verifica si el promedio es un mensaje de error
        print(f"{ciudad}: {promedio}")
    else:
        print(f"{ciudad}: {promedio:.2f}°C")
