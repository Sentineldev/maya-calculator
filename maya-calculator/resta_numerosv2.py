def resta_numero2v2(num1,num2):
    resultado = []
    for numero in num1:
        resultado.append(numero)
    while len(num2)!=len(resultado):
        maya = {
            'circulos':0,
            'lineas':0,
            'conchas':0
        }
        num2.insert(0,maya)
    for i in range(len(resultado)-1,-1,-1):
        if resultado[i]['circulos'] < num2[i]['circulos']:
            resultado[i]['lineas']-=1
            resultado[i]['circulos']+=5
            resultado[i]['circulos']-= num2[i]['circulos']
        else:
            resultado[i]['circulos']-= num2[i]['circulos']
        if i > 0 and resultado[i]['lineas'] < num2[i]['lineas']:
            resultado[i-1]['circulos']-=1
            resultado[i]['lineas']+=4
            resultado[i]['lineas']-=num2[i]['lineas']
        else:
            resultado[i]['lineas']-=num2[i]['lineas']
    for i in range(len(resultado)-1,-1,-1):
        if resultado[i]['lineas'] == 0 and resultado[i]['circulos'] == 0:
            resultado[i]['conchas'] = 1
        else:
            resultado[i]['conchas'] = 0
    return resultado