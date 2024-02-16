def operar_numeros(num1, num2):
    if num1 == num2:
        resultado = num1 * num2
    elif num1 > num2:
        resultado = num1 - num2
    else:
        resultado = num1 + num2
    return resultado
