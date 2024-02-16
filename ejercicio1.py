def calcular_descuento(cantidad, precio):
    total = cantidad * precio
    if total < 100000:
        descuento = total * 0.08
    else:
        descuento = total * 0.10
    cobro = total - descuento
    return descuento, cobro
