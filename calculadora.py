from tkinter import *
from math import * 

window = Tk()
window.title('CALCULADORA PYTHON')
window.geometry('392x600')

#CREAMOS LAS DIMENSIONES DE LOS BOTONES

width_button = 11
heigth_button = 3

#CREAMOS LOS BOTONES DE LA CALCULADORA

Button = Button(window, text='0', width=width_button, height=heigth_button) .place(x = 17, y = 180) # type: ignore

Salida = Entry(window, font=('arial', 20, 'bold'), width=22, bd=20, insertwidth=4, bg='powder blue', justify='right').place(x = 10, y = 60)

