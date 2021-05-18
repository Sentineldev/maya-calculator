from convertir_decimal import convertir_decimal
from resta_numeros import resta_numeros
from convertir import convertir

def division_numeros(num1,num2):
    dividendos = []
    divisor = []
    resultado = []
    restos = []
    for i in range(len(num1)):
        dividendos.append(convertir_unidad(num1,i))
    for i in range(len(num2)):
        divisor.append(convertir_unidad(num2,i))
    divisor = sumar_potencia(divisor)
    for i in range(len(dividendos)):
        if i == 0:
            resultado.append(dividendos[i]//divisor)
            restos.append( abs((resultado[i]*divisor)-(dividendos[i])) )
        if i > 0:
            aux = []
            aux.append(restos[i-1])
            aux.append(dividendos[i])
            dividendos[i] = aux
            dividendos[i] = sumar_potencia(dividendos[i])
            resultado.append( dividendos[i]//divisor )
            restos.append(abs((resultado[i]*divisor)-(dividendos[i])))

    resultado = sumar_potencia(resultado)
    resultado = convertir(resultado)
    for i in range(len(resultado)):
        if resultado[i]['circulos'] == 0 and resultado[i]['lineas'] == 0:
            resultado[i]['conchas'] = 1
        else:
            resultado[i]['conchas'] = 0
    return resultado,restos[-1]

def convertir_unidad(numero,pos):
    circulos = (numero[pos]['circulos']*1)
    lineas = (numero[pos]['lineas']*5)
    resultado = (circulos+lineas)*(20**0)
    return resultado 

def sumar_potencia(numero):
    numero.reverse()
    resultado = 0
    for i in range(len(numero)):
        numero[i]*= 20**i
        resultado += numero[i]
    return resultado


