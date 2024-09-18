# Definimos la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=25):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
monto1 = 400.0
monto2 = 800.0
monto3 = 200.0
monto4 = 350.0
porcentaje_descuento2 = 20
porcentaje_descuento4 = 25

# Llamadas a la función
descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
descuento3 = calcular_descuento(monto3, porcentaje_descuento4)

# Mostrar los resultados
print(f"Compra 1: Monto Total = {monto1}, Descuento = {descuento1}, Monto Final = {monto1 - descuento1}")
print(f"Compra 2: Monto Total = {monto2}, Descuento = {descuento2}, Monto Final = {monto2 - descuento2}")
print(f"Compra 3: Monto Total = {monto3}, Descuento = {descuento3}, Monto Final = {monto3 - descuento3}")
