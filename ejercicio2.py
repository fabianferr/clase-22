def calcular_pago(monto_compra):
    if monto_compra > 500000:
        inversion = monto_compra * 0.55
        prestamo = monto_compra * 0.30
        credito = monto_compra * 0.15
    else:
        inversion = monto_compra * 0.70
        prestamo = 0
        credito = monto_compra * 0.30
    intereses = credito * 0.20
    return inversion, prestamo, credito, intereses
