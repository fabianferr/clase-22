def calcular_sueldo(sueldo_base, ventas):
    comision = sum(ventas) * 0.10
    total = sueldo_base + comision
    return comision, total
