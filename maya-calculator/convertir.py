def convertir(num):
    num = int(num)
    resultado = []
    numero_maya = []
    while True:
        if num >= 20:
            resto = int(num%20)
            num/=20
            resultado.append(resto)
        if num < 20:
            resultado.append(int(num))
            break
        if num < 20 and len(resultado) == 0:
            resultado.append(num)
            break
   
    for i in range(len(resultado)-1,-1,-1):
        if resultado[i] == 0:
            maya = {
                'circulos':0,
                'lineas':0,
                'conchas':1
            }
            numero_maya.append(maya)
        elif resultado[i] == 1:
            maya = {
                'circulos':1,
                'lineas':0,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 2:
            maya = {
                'circulos':2,
                'lineas':0,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 3:
            maya = {
                'circulos':3,
                'lineas':0,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 4:
            maya = {
                'circulos':4,
                'lineas':0,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 5:
            maya = {
                'circulos':0,
                'lineas':1,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 6:
            maya = {
                'circulos':1,
                'lineas':1,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 7:
            maya = {
                'circulos':2,
                'lineas':1,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 8:
            maya = {
                'circulos':3,
                'lineas':1,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 9:
            maya = {
                'circulos':4,
                'lineas':1,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 10:
            maya = {
                'circulos':0,
                'lineas':2,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 11:
            maya = {
                'circulos':1,
                'lineas':2,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 12:
            maya = {
                'circulos':2,
                'lineas':2,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 13:
            maya = {
                'circulos':3,
                'lineas':2,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 14:
            maya = {
                'circulos':4,
                'lineas':2,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 15:
            maya = {
                'circulos':0,
                'lineas':3,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 16:
            maya = {
                'circulos':1,
                'lineas':3,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 17:
            maya = {
                'circulos':2,
                'lineas':3,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 18:
            maya = {
                'circulos':3,
                'lineas':3,
                'conchas':0
            }
            numero_maya.append(maya)
        elif resultado[i] == 19:
            maya = {
                'circulos':4,
                'lineas':3,
                'conchas':0
            }
            numero_maya.append(maya)
    return numero_maya
