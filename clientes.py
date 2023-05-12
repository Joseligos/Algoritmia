import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def inicio_sesion():
    global pantalla1 
    pantalla1 = Tk()
    pantalla1.geometry("400x250")
    pantalla1.title("M&M MOTORS LOGIN")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1, text= "Por Favor Ingrese El Dni Del Cliente",bg="#EB0B0B",fg="white",width="300",height="3", font=("Inter", 15)).pack()
    Label(pantalla1,text="").pack()

    global dni_verificacion

    dni_verificacion = StringVar()

    global dni_usuario_entry 
  
    Label(pantalla1, text="Numero De DNI").pack()
    dni_usuario_entry = Entry(pantalla1,textvariable= dni_verificacion)
    dni_usuario_entry.pack()
    Label(pantalla1).pack()
    Button(pantalla1, text="Validar").pack()
    pantalla1.mainloop()
inicio_sesion()