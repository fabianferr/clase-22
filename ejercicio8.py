def calcular_descuento_bolilla(color, total):
    descuentos = {"blanco": 0, "verde": 0.10, "amarillo": 0.25, "azul": 0.50, "rojo": 1}
    descuento = total * descuentos[color]
    total_final = total - descuento
    return total_final
