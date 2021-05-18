def resta_numeros(num1,num2):
    resultado = []
    if len(num1) == len(num2):
        for i in range(len(num1)):
            resultado.append(num1[i])
        for i in range(len(resultado)-1,-1,-1):
            if resultado[i]['lineas'] < num2[i]['lineas']:
                resultado[i-1]['circulos']-=1
                resultado[i]['lineas']+=4
                resultado[i]['lineas']-=num2[i]['lineas']
            else:
                resultado[i]['lineas']-=num2[i]['lineas']
            if resultado[i]['circulos'] < num2[i]['circulos']:
                resultado[i]['lineas'] -= 1
                resultado[i]['circulos']+=5
                resultado[i]['circulos']-= num2[i]['circulos']
            else:
                resultado[i]['circulos']-=num2[i]['circulos']
    if len(num1) > len(num2):
        for i in range(len(num1)):
            resultado.append(num1[i])
        while len(num2)!= len(resultado):
            num = {
                'circulos':0,
                'lineas':0,
                'conchas':0
            }
            num2.insert(0,num)
        for i in range(len(num2)-1,-1,-1):
            if resultado[i]['circulos'] < num2[i]['circulos']:
                resultado[i]['lineas']-=1
                resultado[i]['circulos']+=5
                resultado[i]['circulos']-=num2[i]['circulos']
            else:
                resultado[i]['circulos']-=num2[i]['circulos']
            if resultado[i]['lineas'] < num2[i]['lineas']:
                resultado[i-1]['circulos']-=1
                resultado[i]['lineas']+=4
                resultado[i]['lineas']-=num2[i]['lineas']
            else:
                resultado[i]['lineas']-=num2[i]['lineas']
            if resultado[i]['circulos'] == 0 and resultado[i]['lineas'] == 0:
                resultado.remove(resultado[i])
    for i in range(len(resultado)):
        if resultado[i]['circulos'] == 0 and resultado[i]['lineas'] == 0:
            resultado[i]['conchas'] = 1
        else:
            resultado[i]['conchas'] = 0
    return resultado