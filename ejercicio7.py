def clasificar_jubilacion(edad, antiguedad):
    if edad >= 60 and antiguedad < 25:
        tipo = "jubilación por edad"
    elif edad < 60 and antiguedad >= 25:
        tipo = "jubilación por antigüedad joven"
    elif edad >= 60 and antiguedad >= 25:
        tipo = "jubilación por antigüedad adulta"
    return tipo
