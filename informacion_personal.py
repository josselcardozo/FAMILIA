# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Juana Jaime",
    "edad": 68,
    "ciudad": "Samborondón",
    "profesion": "Diseñadora de modas"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
# Cambiamos la ciudad de "Samborondón" a "Tarifa"
informacion_personal["ciudad"] = "Tarifa"

# Agregar una nueva clave-valor relacionada con la información profesional
# En este caso, añadimos la clave "especialidad"
informacion_personal["especialidad"] = "Diseño Moda"

# Verificar si la clave "telefono" existe en el diccionario
# Si no existe, agregamos un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0910115564"

# Eliminar la clave "edad" porque ya no es necesaria
informacion_personal.pop("edad", None)  # None evita errores si la clave no existe

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)

#Diccionario final:
{'nombre': 'Juana Jaime', 'ciudad': 'Tarifa', 'profesion': 'Diseñadora de modas', 'especialidad': 'Diseño Moda', 'telefono': '0910115564'}