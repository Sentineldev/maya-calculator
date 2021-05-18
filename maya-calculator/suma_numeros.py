from convertir import *
def suma_numeros(num1,num2):
    resultado = []
    resultado2 = 0
    if len(num1)==len(num2) or len(num2) == len(num1):
        for i in range(len(num1)):
            aux = {
                "circulos":num1[i]['circulos']+num2[i]['circulos'],
                "lineas":num1[i]['lineas']+num2[i]['lineas'],
                "conchas":num1[i]['conchas']+num2[i]['conchas'],
            }
            resultado.append(aux)
        for i in range(len(resultado)-1,-1,-1):
            if resultado[i]['circulos']>=5:
                resultado[i]['circulos']-=5
                resultado[i]['lineas']+=1
            if i > 0 and resultado[i]['lineas']>=4:
                resultado[i]['lineas']-=4
                resultado[i-1]['circulos']+=1
            if i == 0 and resultado[i]['lineas']>=4:
                aux = {
                    "circulos":0,
                    "lineas":0,
                    "conchas":0
                }
                resultado.insert(0,aux)
                for i in range(len(resultado)-1,-1,-1):
                    if resultado[i]['circulos']>=5:
                        resultado[i]['circulos']-=5
                        resultado[i]['lineas']+=1
                    if resultado[i]['lineas']>=4:
                        resultado[i]['lineas']-=4
                        resultado[i-1]['circulos']+=1
    if len(num1)<len(num2):
        while len(num1)<len(num2):
            aux = {
                "circulos":0,
                "lineas":0,
                "conchas":0
            }
            num1.insert(0,aux)
        for i in range(len(num1)):
            aux = {
                "circulos":num1[i]['circulos']+num2[i]['circulos'],
                "lineas":num1[i]['lineas']+num2[i]['lineas'],
                "conchas":num1[i]['conchas']+num2[i]['conchas'],
            }
            resultado.append(aux)
        for i in range(len(resultado)-1,-1,-1):
            if resultado[i]['circulos']>=5:
                resultado[i]['circulos']-=5
                resultado[i]['lineas']+=1
            if i > 0 and resultado[i]['lineas']>=4:
                resultado[i]['lineas']-=4
                resultado[i-1]['circulos']+=1
            if i == 0 and resultado[i]['lineas']>=4:
                aux = {
                    "circulos":0,
                    "lineas":0,
                    "conchas":0
                }
                resultado.insert(0,aux)
                for i in range(len(resultado)-1,-1,-1):
                    if resultado[i]['circulos']>=5:
                        resultado[i]['circulos']-=5
                        resultado[i]['lineas']+=1
                    if resultado[i]['lineas']>=4:
                        resultado[i]['lineas']-=4
                        resultado[i-1]['circulos']+=1
    if len(num2)<len(num1):
        while len(num2)<len(num1):
            aux = {
                "circulos":0,
                "lineas":0,
                "conchas":0
            }
            num2.insert(0,aux)
        for i in range(len(num2)):
            aux = {
                "circulos":num1[i]['circulos']+num2[i]['circulos'],
                "lineas":num1[i]['lineas']+num2[i]['lineas'],
                "conchas":num1[i]['conchas']+num2[i]['conchas'],
            }
            resultado.append(aux)
        for i in range(len(resultado)-1,-1,-1):
            if resultado[i]['circulos']>=5:
                resultado[i]['circulos']-=5
                resultado[i]['lineas']+=1
            if i > 0 and resultado[i]['lineas']>=4:
                resultado[i]['lineas']-=4
                resultado[i-1]['circulos']+=1
            if i == 0 and resultado[i]['lineas']>=4:
                aux = {
                    "circulos":0,
                    "lineas":0,
                    "conchas":0
                }
                resultado.insert(0,aux)
                for i in range(len(resultado)-1,-1,-1):
                    if resultado[i]['circulos']>=5:
                        resultado[i]['circulos']-=5
                        resultado[i]['lineas']+=1
                    if resultado[i]['lineas']>=4:
                        resultado[i]['lineas']-=4
                        resultado[i-1]['circulos']+=1
    for i in range(len(resultado)):
        if resultado[i]['circulos'] == 0 and resultado[i]['lineas'] == 0:
            resultado[i]['conchas'] = 1
        else:
            resultado[i]['conchas'] = 0
    return resultado
        

