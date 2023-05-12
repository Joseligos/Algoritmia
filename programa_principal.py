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

    Label(text="Acceso Al Sistema",bg="#EB0B0B",fg="white",width="300",height="2", font=("Arial", 15)).pack()

    Label (text="").pack()
    Button(text="Iniciar Sesión", font=("Arial", 12), height="3", width="30",command=inicio_sesion).pack()

    Label (text="").pack()
    Button(text="Registrar", font=("Arial", 12), height="3", width="30", command=Registrar).pack()
    pantalla.resizable(width=False,height=False)
    pantalla.mainloop()

def inicio_sesion():
    global pantalla1 
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("M&M MOTORS LOGIN")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1, text= "Por Favor Ingrese Su Usuario Y Contraseña",bg="#EB0B0B",fg="white",width="300",height="3", font=("Arial", 15)).pack()
    Label(pantalla1,text="").pack()

    global nombreusuario_verificacion
    global claveusuario_verificacion

    nombreusuario_verificacion = StringVar()
    claveusuario_verificacion = StringVar()

    global nombre_usuario_entry 
    global clave_usuario_entry
    
    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1,textvariable= nombreusuario_verificacion)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    clave_usuario_entry = Entry(pantalla1,show="*", textvariable= claveusuario_verificacion)
    clave_usuario_entry.pack()
    Label(pantalla1).pack()
    Button(pantalla1, text="Iniciar Sesion",command=validacion_datos).pack()
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

    Label(pantalla2, text="Por Favor Ingrese Un Usuario Y Contraseña \n Para El Registro En El Sisitema",bg="#EB0B0B",fg="white",width="300",height="3", font=("Arial", 15)).pack()
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
        menu_pantalla_principal()
        bd.close()
       
        
    else:
        messagebox.showinfo(title="Inicio De Sesión Incorrecto", message="Usuario Y Contraseña Incorrecta")
        
    bd.close()

    
def menu_pantalla_principal():
    global pantalla_principal
    pantalla_principal =Tk()
    pantalla_principal.geometry("800x600")
    pantalla_principal.title("M&M SERVICIO")

    pantalla_principal.iconbitmap("logo.ico")

    logo_image = Image.open("logo.png")
    logo_image = logo_image.resize((200, 200), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Crear el widget Label con la imagen
    label_logo = Label(pantalla_principal, image=logo_photo)
    label_logo.pack()

    # Asignar la imagen a una variable global para evitar que sea eliminada
    pantalla_principal.logo_photo = logo_photo

    Label(pantalla_principal, text="SELECCIONA EL SERVICIO QUE DESEAS  EMPLEAR:",bg="#A8A8A8",fg="white",width="300",height="2", font=("Arial", 15)).pack()

    Label (pantalla_principal, text="").pack()
    Button(pantalla_principal, text="Registrar Nuevo Usuario", font=("Arial", 12), height="3", width="30", command=registro_usuario).pack()

    Label (pantalla_principal, text="").pack()
    Button(pantalla_principal, text="Buscar Usuario", font=("Arial", 12), height="3", width="30", command=buscar_usuario).pack()
        

    pantalla_principal.mainloop()

def registro_usuario():
    global pantalla_r_u
    pantalla_r_u=Tk()
    pantalla_r_u.geometry("800x600")
    pantalla_r_u.title("M&M REGISTRO USUARIO")
    pantalla_r_u.iconbitmap("logo.ico")
    image=PhotoImage(file="logo.png")
    image=image.subsample(1,1)
    label=Label(image=image)
    label.pack()

    global nombrecliente
    global dnicliente
    global dircliente
    global numcliente
    global correo 
    global marcav
    global modelv
    global año
    global matricula

    Label(pantalla_r_u, text="Datos del cliente:", font=("Arial", 15)).grid(row=0, column=0, sticky='w', pady=20)

    Label(pantalla_r_u, text="Nombre del cliente:", font=("Arial", 10)).grid(row=1, column=0, sticky='w')
    nombrecliente = Entry(pantalla_r_u)
    nombrecliente.grid(row=1, column=1, sticky='w')
    Label(pantalla_r_u, text="Documento del cliente:", font=("Arial", 10)).grid(row=2, column=0, sticky='w')
    dnicliente = Entry(pantalla_r_u)
    dnicliente.grid(row=2, column=1, sticky='w')
    Label(pantalla_r_u, text="Dirección del cliente:", font=("Arial", 10)).grid(row=3, column=0, sticky='w')
    dircliente = Entry(pantalla_r_u)
    dircliente.grid(row=3, column=1, sticky='w')
    Label(pantalla_r_u, text="Número telefónico:", font=("Arial", 10)).grid(row=4, column=0, sticky='w')
    numcliente = Entry(pantalla_r_u)
    numcliente.grid(row=4, column=1, sticky='w')
    Label(pantalla_r_u, text="Correo:", font=("Arial", 10)).grid(row=5, column=0, sticky='w')
    correo = Entry(pantalla_r_u)
    correo.grid(row=5, column=1, sticky='w')

    Label(pantalla_r_u, text="Datos del vehículo:", font=("Arial", 15)).grid(row=6, column=0, sticky='w', pady=20)

    Label(pantalla_r_u, text="Marca del vehículo:", font=("Arial", 10)).grid(row=7, column=0, sticky='w')
    marcav = Entry(pantalla_r_u)
    marcav.grid(row=7, column=1, sticky='w')
    Label(pantalla_r_u, text="Modelo del vehículo:", font=("Arial", 10)).grid(row=8, column=0, sticky='w')
    modelv = Entry(pantalla_r_u)
    modelv.grid(row=8, column=1, sticky='w')
    Label(pantalla_r_u, text="Año:", font=("Arial", 10)).grid(row=9, column=0, sticky='w')
    año = Entry(pantalla_r_u)
    año.grid(row=9, column=1, sticky='w')
    Label(pantalla_r_u, text="Matrícula:", font=("Arial", 10)).grid(row=10, column=0, sticky='w')
    matricula = Entry(pantalla_r_u)
    matricula.grid(row=10, column=1, sticky='w')

    Button(pantalla_r_u, text="Registrar Usuario y Vehiculo", height="3", width="30", command=lambda:[datos_user(), datos_vehiculo()]).grid(row=11, column=0, columnspan=2, pady=10)

    pantalla_r_u.mainloop()

def datos_user():
    bd=pymysql.connect(
        host = "localhost",
        user = "root",
        passwd="",
        db="bd2"
        )
    
    fcursor=bd.cursor() 

    sql="INSERT INTO datos_usuario (Nombre, DNI, Dirección, Teléfono, Correo) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(nombrecliente.get(), dnicliente.get(), dircliente.get(), numcliente.get(), correo.get())
    try: 
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

def datos_vehiculo():
    bd=pymysql.connect(
        host = "localhost",
        user = "root",
        passwd="",
        db="bd2"
        )
    
    fcursor=bd.cursor() 

    sql="INSERT INTO datos_vehiculo (Marca, Modelo, Año, Matricula) VALUES ('{0}', '{1}', '{2}', '{3}')".format(marcav.get(), modelv.get(), año.get(), matricula.get())
    try: 
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

menu_pantalla()
