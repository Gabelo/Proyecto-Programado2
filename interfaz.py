from Tkinter import *
from Pylog import *

#Funciones necesarias

#Funcion ocultar
def ocultar(ventana):
    ventana.withdraw()

#Funcion mostrar
def mostrar(ventana):
    ventana.deiconify()

#Funcion ejecutar
def ejecutar(f):
    principal.after(200,f)

def almacenar(e1,e2,e3,e4,e5):
    total = 'restaurante('+e1.lower()+','+e2.lower()+','+e3.lower()+','+e4.lower()+','+e5.lower()+').'
    almacenar_aux(total)

def almacenar_aux(element):
    archivo = open("bc.pl", "a")
    archivo.write(element+'\n');
    archivo.close()

def limpiar(e1,e2,e3,e4,e5):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def cargar(lista,listbox):
    ind,largo=0,len(lista)
    while ind <largo:
        listbox.insert(END,lista[ind])
        ind+=1

#Ventanas
#Creacion de una ventana principal para la interfaz
principal = Tk()
principal.title('Menu Principal')
#Creacion de la ventana mantenimiento
ventana_mantenimiento =Toplevel(principal)
ventana_mantenimiento.title('Mantenimiento')
ventana_mantenimiento.geometry("600x200")
ventana_mantenimiento.withdraw() #Mantiene la ventana oculta
#Creacion de los botones en mantenimiento
boton_restaurante=Button(ventana_mantenimiento,text='Mantenimiento Restaurante',command=lambda: mostrar(restaurante) or ocultar(ventana_mantenimiento))
boton_restaurante.grid(row=1,column=1)
boton_platillo=Button(ventana_mantenimiento,text='Mantenimiento Platillo',command=lambda: mostrar(platillo) or ocultar(ventana_mantenimiento))
boton_platillo.grid(row=1,column=3)
boton_salir_mantenimiento=Button(ventana_mantenimiento,text='Salir',command=lambda: mostrar(principal) or ocultar(ventana_mantenimiento))
boton_salir_mantenimiento.grid(row=3,column=2)
#Creacion de la ventana restaurante
restaurante=Toplevel(ventana_mantenimiento)
restaurante.title=('Mantenimiento Restaurante')
restaurante.geometry("1000x200")
restaurante.withdraw()
#Creacion de la ventana platillo
platillo=Toplevel(ventana_mantenimiento)
platillo.title('Mantenimiento Platillo')
platillo.geometry("1000x200")
platillo.withdraw()
#Creacion de la ventana de consulta
ventana_consulta = Toplevel(principal)
ventana_consulta.title('Consulta')
ventana_consulta.withdraw() #Mantiene la ventana oculta
#Creacion de los botones de la principal
#Creacion del boton de mantenimiento
boton_mantenimiento = Button(principal,text='Mantenimiento',command=lambda: ejecutar(mostrar(ventana_mantenimiento))or ocultar(principal))
boton_mantenimiento.grid(row=3,column=2)
#Creacion del boton de consulta
boton_consulta = Button(principal,text='Consulta',command=lambda: ejecutar(mostrar(ventana_consulta)))
boton_consulta.grid(row=3,column=4)
boton_salir = Button(principal,text='Salir')
boton_salir.grid(row=5,column=3)
#Creacion de las etiquetas y textbox necesarias para recibir la informacion en la ventana mantenimiento de restaurante
#Etiqueta Nombre restaurante
label_nombre = Label(restaurante,text='Digite el nombre del restaurante ')
label_nombre.grid(row=1,column=1)
#variable para almacenar el nombre
nombre=StringVar()
#textbox para capturar el nombre
textbox_nombre = Entry(restaurante,textvariable=nombre)
textbox_nombre.grid(row=1,column=2)
#Etiqueta tipo comida
label_tipo = Label(restaurante,text='Digite el tipo de comida ')
label_tipo.grid(row=1,column=5)
#variable para almacenar el tipo de comida
tipo=StringVar()
#textbox para capturar el tipo de comida
textbox_tipo = Entry(restaurante,textvariable=tipo)
textbox_tipo.grid(row=1,column=6)
#Etiqueta ubicacion
label_ubicacion =Label(restaurante,text='Digite la ubicacion del restaurante')
label_ubicacion.grid(row=3,column=1)
#variable para almacenar la ubicacion
ubicacion=StringVar()
#textbox para capturar la ubicacion
textbox_ubicacion = Entry(restaurante,textvariable=ubicacion)
textbox_ubicacion.grid(row=3,column=2)
#label telefono
label_telefono =Label(restaurante,text='Digite el telefono del restaurante')
label_telefono.grid(row=3,column=5)
#Variable para almacenar el telefono
telefono=StringVar()
#textbox para capturar el telefono
textbox_telefono = Entry(restaurante,textvariable=telefono)
textbox_telefono.grid(row=3,column=6)
#label horario
label_horario = Label(restaurante,text='Digite el horario del restaurante')
label_horario.grid(row=5,column=1)
#variable horario
horario=StringVar()
#Textbox para almacenar el horario
textbox_horario = Entry(restaurante,textvariable=horario)
textbox_horario.grid(row=5,column=2)
#botones
#boton agregar
button_a = Button(restaurante,text='Almacenar',command=lambda: almacenar(nombre.get(),tipo.get(),ubicacion.get(),telefono.get(),horario.get())or limpiar(textbox_nombre,textbox_tipo,textbox_ubicacion,textbox_telefono,textbox_horario))
button_a.grid(row=7,column=3)
button_s = Button(restaurante,text='Salir',command=lambda: ocultar(restaurante) or mostrar(ventana_mantenimiento))
button_s.grid(row=7,column=5)
#Creacion de etiquetas,botones y textbox de mantenimiento platillos
label_nombre_restaurante=Label(platillo,text='Elija el restaurante')
label_nombre_restaurante.grid(row=1,column=1)
#Variable restaurante
rest=StringVar()
#Creacion de textbox para almacenar el restaurante
textbox_rest= Entry(platillo,textvariable=rest)
textbox_rest.grid(row=1,column=2)
#Etiqueta nombre platillo
label_platillo_nombre=Label(platillo,text='Digite el nombre del platillo')
label_platillo_nombre.grid(row=1,column=4)
#Variable nombre platillo
var_nombre_platillo=StringVar()
#Textbox para nombre platillo
textbox_nombre_platillo=Entry(platillo,textvariable=var_nombre_platillo)
textbox_nombre_platillo.grid(row=1,column=5)
#Etiqueta tipo platillo
label_sabor=Label(platillo,text='Seleccione el sabor del platillo')
label_sabor.grid(row=3,column=1)
#Variable tipo platillo
sabor=StringVar()
#ListBox
sabores=Listbox(platillo)
sabores.grid(row=3,column=2)
lista_sabores=['picante','salado','dulce','agridulce','amargo']
prueba=Label(platillo,textvar=sabor)
cargar(lista_sabores,sabores)

def guardar():
    ind=sabores.curselection()
    if sabores.curselection() != ():
        sabor=sabores.get(ind)
        printer(sabor)
guardar()

def printer(var):
    print(var)
principal.mainloop()

