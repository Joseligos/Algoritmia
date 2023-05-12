import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def menu_pantalla():
    global pantalla
    pantalla =Tk()
    pantalla.geometry("400x500")
    pantalla.title("M&M MOTORS BIEVENIDA")

    pantalla.iconbitmap("logo.ico")

    image = PhotoImage(file="logo.png")
    image = image.subsample (2,2)
    label = Label(image=image)
    label.pack()

    Label(text="Acceso Al Sistema",bg="#A8A8A8",fg="white",width="300",height="2", font=("Arial", 15)).pack()

    Label (text="").pack()
    Button(text="Iniciar Sesión", font=("Arial", 12), height="3", width="30",command=inicio_sesion).pack()

    Label (text="").pack()
    Button(text="Registrar", font=("Arial", 12), height="3", width="30", command=Registrar).pack()

    Label (text="").pack()
    Button(text="Continuar", font=("Arial", 12), height="3", width="30", command=pantalla_princ).pack()
    pantalla.mainloop()
#---------------------------------------------------------------------------------
def inicio_sesion():
    global pantalla1 
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("M&M MOTORS LOGIN")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1, text= "Por Favor Ingrese El Dni Del Cliente",bg="#A8A8A8",fg="white",width="300",height="3", font=("Arial", 15)).pack()
    Label(pantalla1,text="").pack()

    global dni_verificacion

    dni_verificacion = StringVar()

    global dni_usuario_entry 
  
    Label(pantalla1, text="Numero De DNI").pack()
    dni_usuario_entry = Entry(pantalla1,textvariable= dni_verificacion)
    dni_usuario_entry.pack()
    Label(pantalla1).pack()
    Button(pantalla1, text="Validar").pack()

    Button(pantalla1, text="Iniciar Sesion",command=lambda:[validacion_datos(),pantalla_princ()]).pack()
#---------------------------------------------------------------------------------
def Registrar():
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("M&M MOTORS Registro De Usuario")
    pantalla2.iconbitmap("logo.ico")

    global nombreusuario_entry
    global clave_entry 

    nombreusuario_entry = StringVar()
    clave_entry = StringVar()

    Label(pantalla2, text="Por Favor Ingrese Un Usuario Y Contraseña \n Para El Registro En El Sisitema",bg="#A8A8A8",fg="white",width="300",height="3", font=("Arial", 15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()  

    Label(pantalla2, text="Contraseña" ).pack()
    clave_entry = Entry(pantalla2, show="*")
    clave_entry.pack()
    Label(pantalla2).pack()  

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()

#---------------------------------------------------------------------------------
def inserta_datos():
    bd=pymysql.connect(
        host = "localhost",
        user = "root",
        passwd="",
        db="bd2"
        )
    
    fcursor=bd.cursor()

    sql="INSERT INTO login (usuario, clave) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(),clave_entry.get())
    try: 
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")
    bd.close()

#---------------------------------------------------------------------------------
def validacion_datos():
    bd=pymysql.connect(
        host = "localhost",
        user = "root",
        passwd="",
        db="bd2"
        )
    fcursor=bd.cursor()
    fcursor.execute("SELECT clave FROM login WHERE usuario='"+nombreusuario_verificacion.get()+"' and clave='"+claveusuario_verificacion.get()+"' ")
    
    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio De Sesión Correcto", message="Usuario Y Contraseña correcta")
        INICIAR = pantalla_princ()
    
        
    else:
        messagebox.showinfo(title="Inicio De Sesión Incorrecto", message="Usuario Y Contraseña Incorrecta")
    bd.close()
    
   #--------------------------------------------------------------------------------- 
def pantalla_princ():
    global pantalla_principal
    pantalla_principal =Toplevel(pantalla)
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

    
#--------------------------------------------------------------------------------------


  #---------------------------------------------------------------------------------  
menu_pantalla()















