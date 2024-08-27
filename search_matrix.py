def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j
    return None

# Definir una matriz 3x3 con valores numéricos diferentes
matriz = [
    [12, 25, 7],
    [34, 50, 18],
    [45, 23, 33]
]

# Definir el valor a buscar
valor_buscado = 50

# Buscar el valor en la matriz
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"Valor {valor_buscado} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_buscado} no se encontró en la matriz.")