import tkinter
from tkinter import *
from tkinter import messagebox

def menu_pantalla():
    global pantalla_principal
    pantalla_principal =Tk()
    pantalla_principal.geometry("800x600")
    pantalla_principal.title("M&M SERVICIO")

    pantalla_principal.iconbitmap("logo.ico")

    image = PhotoImage(file="logo.png")
    image = image.subsample (2,2)
    label = Label(image=image)
    label.pack()

    Label(text="SELECCIONA EL SERVICIO QUE DESEAS  EMPLEAR:",bg="#A8A8A8",fg="white",width="300",height="2", font=("Arial", 15)).pack()

    Label (text="").pack()
    Button(text="Chapa", font=("Arial", 12), height="3", width="30").pack()

    Label (text="").pack()
    Button(text="Pintura", font=("Arial", 12), height="3", width="30").pack()
        
    Label (text="").pack()
    Button(text="Mecanica", font=("Arial", 12), height="3", width="30").pack()
    pantalla_principal.mainloop()
menu_pantalla()