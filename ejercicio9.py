def verificar_temperatura(minimo, maximo, temperatura):
    if minimo <= temperatura <= maximo:
        mensaje = "La temperatura está dentro del rango."
    else:
        mensaje = "La temperatura está fuera del rango."
    return mensaje
