
from tkinter import *  
from tkinter.font import *
from tkinter.messagebox import *
from convertir import convertir #importar una funcion para convertir el numero decimal a maya mediante una lista con diccionarios
from convertir_decimal import convertir_decimal
import time

from suma_numeros import suma_numeros
from resta_numeros import resta_numeros
from multiplicacion import multiplicar
from division import division_numeros
from resta_numerosv2 import resta_numero2v2

def division():
    if int(entry1.get()) == 0:
        showerror(message='No existe la division entre 0',title='Error')
    else:
        canvas.delete('rectangle3')
        canvas.delete('oval3')
        canvas.delete('line3')
        canvas.delete('concha3')
        resultado_maya = []
        dividendo = convertir(int(entry.get()))
        divisor = convertir(int(entry1.get()))
        resultado_maya = division_numeros(dividendo,divisor)
        if len(resultado_maya) > 6:
            showerror(message='El numero es mayor al tamaño de la ventana. Fuera de rango.',title='Error')
        else:
            mostrar_num3(resultado_maya[0])
            entry2.delete(0,"end")
            entry2.insert(0,abs(resultado_maya[1]))

def multiplicacion():
    canvas.delete('rectangle3')
    canvas.delete('oval3')
    canvas.delete('line3')
    canvas.delete('concha3')
    resultado_maya = []
    multiplicador = int(entry1.get())
    multiplicado = convertir(int(entry.get()))
    resultado_maya = multiplicar(multiplicado,multiplicador)
    if len(resultado_maya) > 6:
        showerror(message='El numero es mayor al tamaño de la ventana. Fuera de rango.',title='Error')
    else:
        mostrar_num3(resultado_maya)
        entry2.delete(0,"end")
        entry2.insert(0,convertir_decimal(resultado_maya))

def restar():
    if int(entry.get()) < int(entry1.get()):
        showinfo(message='El primer numero debe ser mayor al segundo',title='Error')
    else:
        resultado_maya = []
        num1 = convertir(entry.get())
        num2 = convertir(entry1.get())
        resultado_maya = resta_numero2v2(num1,num2)
        if len(resultado_maya) > 6:
            showerror(message='El numero es mayor al tamaño de la ventana. Fuera de rango.',title='Error')
        else:
            mostrar_num3(resultado_maya)
            entry2.delete(0,"end")
            entry2.insert(0,convertir_decimal(resultado_maya))

def sumar():
    canvas.delete('rectangle3')
    canvas.delete('oval3')
    canvas.delete('line3')
    canvas.delete('concha3')
    resultado_maya = []
    num1 = convertir(int(entry.get()))
    num2 = convertir(int(entry1.get()))
    resultado_maya = suma_numeros(num1,num2)
    if len(resultado_maya) > 6:
        showerror(message='El numero es mayor al tamaño de la ventana. Fuera de rango.',title='Error')
    else:
        mostrar_num3(resultado_maya)
        entry2.delete(0,"end")
        entry2.insert(0,convertir_decimal(resultado_maya))


def validate_entry(char):
    return char.isdigit()

def mostrar_num3(resultado_maya):
    canvas.delete('rectangle3')
    canvas.delete('oval3')
    canvas.delete('line3')
    canvas.delete('concha3')
    y1 = 5
    y2 = 100
    x1_oval = 610
    x2_oval = 620
    y1_oval = 15
    y2_oval = 25
    y_line = 0
    y1_concha = 35
    y2_concha = 65
    y_concha_line = 50
    for i in range(len(resultado_maya)):
        if i == 0:
            canvas.create_rectangle(600,y1,700,y2,tags='rectangle3')
            y1+= 95
            y2+= 100
        if i > 0:
            canvas.create_rectangle(600,y1,700,y2,tags='rectangle3')
            y1+=100
            y2+=100
    for i in range(len(resultado_maya)):
        for j in range(resultado_maya[i]['circulos']):
            canvas.create_oval(x1_oval,y1_oval,x2_oval,y2_oval,tags='oval3')
            x1_oval+=20
            x2_oval+=20
        y1_oval+=100
        y2_oval+=100
        x1_oval=610
        x2_oval=620
    for i in range(len(resultado_maya)):
        y_line = (100*i)+40
        for j in range(resultado_maya[i]['lineas']):
            canvas.create_line(610,y_line,690,y_line,tags='line3')
            y_line+=10
    for i in range(len(resultado_maya)):
        for j in range(resultado_maya[i]['conchas']):
            canvas.create_oval(600,y1_concha,700,y2_concha,tags='concha3')
            canvas.create_line(600,y_concha_line,700,y_concha_line,tags='concha3')
        y_concha_line+=100
        y1_concha+=100
        y2_concha+=100

def dibujar_cuadros_1(numero_maya):
    y1 = 5
    y2 = 100
    x1_oval = 260
    x2_oval = 270
    y1_oval = 15
    y2_oval = 25
    y_line = 0
    y1_concha = 35
    y2_concha = 65
    y_concha_line = 50
    for i in range(len(numero_maya)):
        if i == 0:
            canvas.create_rectangle(250,y1,350,y2,tags='rectangle1')
            y1+= 95
            y2+= 100
        if i > 0:
            canvas.create_rectangle(250,y1,350,y2,tags='rectangle1')
            y1+=100
            y2+=100
    for i in range(len(numero_maya)):
        for j in range(numero_maya[i]['circulos']):
            canvas.create_oval(x1_oval,y1_oval,x2_oval,y2_oval,tags='oval1')
            x1_oval+=20
            x2_oval+=20

        y1_oval+=100
        y2_oval+=100
        x1_oval=260
        x2_oval=270
    for i in range(len(numero_maya)):
        y_line = (100*i)+40
        for j in range(numero_maya[i]['lineas']):
            canvas.create_line(260,y_line,340,y_line,tags='line1')
            y_line+=10
    for i in range(len(numero_maya)):
        for j in range(numero_maya[i]['conchas']):
            canvas.create_oval(250,y1_concha,350,y2_concha,tags='concha1')
            canvas.create_line(250,y_concha_line,350,y_concha_line,tags='concha1')
        y_concha_line+=100
        y1_concha+=100
        y2_concha+=100
def mostrar_num1():
    if validate_entry(entry.get()) == True:
        numero_maya = 0
        canvas.delete('rectangle1')
        canvas.delete('oval1')
        canvas.delete('line1')
        canvas.delete('concha1')
        numero = int(entry.get())
        numero_maya = convertir(numero)
        if len(numero_maya) > 6:
            showerror(message='El numero es mayor al tamaño de la ventana. Fuera de rango.',title='Error')
        else:
            dibujar_cuadros_1(numero_maya)
    else:
        showerror(message='Introduzca solo numeros',title='Error')

def dibujar_cuadros_2(numero_maya):
    y1 = 5
    y2 = 100
    x1_oval = 410
    x2_oval = 420
    y1_oval = 15
    y2_oval = 25
    y_line = 0
    y1_concha = 35
    y2_concha = 65
    y_concha_line = 50
    for i in range(len(numero_maya)):
        if i == 0:
            canvas.create_rectangle(400,y1,500,y2,tags='rectangle2')
            y1+= 95
            y2+= 100
        if i > 0:
            canvas.create_rectangle(400,y1,500,y2,tags='rectangle2')
            y1+=100
            y2+=100
    for i in range(len(numero_maya)):
        for j in range(numero_maya[i]['circulos']):
            canvas.create_oval(x1_oval,y1_oval,x2_oval,y2_oval,tags='oval2')
            x1_oval+=20
            x2_oval+=20
        y1_oval+=100
        y2_oval+=100
        x1_oval=410
        x2_oval=420
    for i in range(len(numero_maya)):
        y_line = (100*i)+40
        for j in range(numero_maya[i]['lineas']):
            canvas.create_line(410,y_line,490,y_line,tags='line2')
            y_line+=10
    for i in range(len(numero_maya)):
        for j in range(numero_maya[i]['conchas']):
            canvas.create_oval(400,y1_concha,500,y2_concha,tags='concha2')
            canvas.create_line(400,y_concha_line,500,y_concha_line,tags='concha2')
        y_concha_line+=100
        y1_concha+=100
        y2_concha+=100
def mostrar_num2():
    if validate_entry(entry1.get()) == True:
        numero_maya2 = 0
        canvas.delete('rectangle2')
        canvas.delete('oval2')
        canvas.delete('line2')
        canvas.delete('concha2')
        numero = int(entry1.get())
        numero_maya2 = convertir(numero)
        if len(numero_maya2) > 6:
            showerror(message='El numero es mayor al tamaño de la ventana. Fuera de rango.',title='Error')
        else:
            dibujar_cuadros_2(numero_maya2)
    else:
        showerror(message='Introduzca solo numeros',title='Error')


def dibujar_entradas(frame):
    global entry
    global entry1
    global entry2
    entry = Entry(frame,width=10,font=('Arial',25))
    entry1 = Entry(frame,width=10,font=('Arial',25))
    entry2 = Entry(frame,width=10,font=('Arial',25))
    entry.place(x=25,y=100)
    entry1.place(x=25,y=200)
    entry2.place(x=25,y=530)


def dibujar_botones(frame):
    num1 = Button(frame,text='Mostrar',command=mostrar_num1)
    num1.place(x=89,y=150)
    num2 = Button(frame,text='Mostrar',command=mostrar_num2)
    num2.place(x=89,y=250)
    suma = Button(frame,text='Sumar',width=21,height=2,command=sumar)
    suma.place(x=25,y=300)
    resta = Button(frame,text='Restar',width=21,height=2,command=restar)
    resta.place(x=25,y=350)
    multiplicar = Button(frame,text='Multiplicar',width=21,height=2,command=multiplicacion)
    multiplicar.place(x=25,y=400)
    dividir = Button(frame,text='Dividir',width=21,height=2,command=division)
    dividir.place(x=25,y=450)



def main():
    global canvas
    window = Tk()
    window.title('Calculadora Maya')
    canvas = Canvas(window,width=800,height=600)
    canvas.pack()

    frame = Frame(window,bg='#263d42')
    frame.place(relwidth=0.3,relheight=1)

    dibujar_entradas(frame)
    dibujar_botones(frame)

    window.mainloop()

main()
