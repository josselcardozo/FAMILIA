def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [12, 45, 23],
    [7,  14, 3],
    [10, 9, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1) usando Bubble Sort
fila_a_ordenar = 1
bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila específica
print("\nMatriz después de ordenar la segunda fila:")
for fila in matriz:
    print(fila)