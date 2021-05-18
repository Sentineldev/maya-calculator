def convertir_decimal(numero_maya):
    numero_maya.reverse()
    resultado = 0
    for i in range(len(numero_maya)):
        potencia = 20**i
        circulos = numero_maya[i]['circulos']*1
        lineas = numero_maya[i]['lineas']*5
        resultado += (circulos+lineas)*potencia
    return resultado
