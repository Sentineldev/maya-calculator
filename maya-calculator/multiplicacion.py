from suma_numeros import suma_numeros

def multiplicar(num1,num2):
    resultado = []
    for i in range(len(num1)):
        resultado.append(num1[i])
    for i in range(1,num2):
        resultado = suma_numeros(resultado,num1)
    for i in range(len(resultado)):
        if resultado[i]['circulos'] == 0 and resultado[i]['lineas'] == 0:
            resultado[i]['conchas'] = 1
        else:
            resultado[i]['conchas'] = 0
    return resultado


