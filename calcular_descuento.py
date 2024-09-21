# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje sobre el monto total.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento, por defecto es 10%.
    :return: Monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Interacción personalizada con Juana, Isabel y Lia
def main():
    # Interacción con Juana (descuento del 25%)
    monto_juana = 120.0
    descuento_juana = calcular_descuento(monto_juana, 25)
    monto_final_juana = monto_juana - descuento_juana
    print(f"Juana: Monto de la compra: ${monto_juana}, Descuento aplicado: ${descuento_juana}, Monto final: ${monto_final_juana}")

    # Interacción con Isabel (descuento del 50%)
    monto_isabel = 250.0
    descuento_isabel = calcular_descuento(monto_isabel, 50)
    monto_final_isabel = monto_isabel - descuento_isabel
    print(f"Isabel: Monto de la compra: ${monto_isabel}, Descuento aplicado: ${descuento_isabel}, Monto final: ${monto_final_isabel}")

    # Interacción con Lia (descuento del 15%)
    monto_lia = 300.0
    descuento_lia = calcular_descuento(monto_lia, 15)
    monto_final_lia = monto_lia - descuento_lia
    print(f"Lia: Monto de la compra: ${monto_lia}, Descuento aplicado: ${descuento_lia}, Monto final: ${monto_final_lia}")

# Llamada a la función principal
if __name__ == "__main__":
    main()
