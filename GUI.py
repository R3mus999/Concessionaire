from tkinter import *
from tkinter import messagebox

import testConcesionario


class App:
    def __init__(self):
        ventana = Tk()
        ventana.geometry("500x500")
        ventana.title("Concesionario")

        # CREAR CONCESIONARIO

        # Nombre del concesionario
        self.labelNombre = Label(ventana, text="Nombre del concesionario:")
        self.labelNombre.place(x=30, y=30)
        self.nombre = Entry(ventana)
        self.nombre.place(x=250, y=30)

        # Direccion del concesionario
        self.labelDireccion = Label(ventana, text="Dirección:")
        self.labelDireccion.place(x=30, y=50)
        self.direccion = Entry(ventana)
        self.direccion.place(x=250, y=50)

        #Boton de crear concesionario
        self.boton_crear = Button(ventana, text="Crear concesionario", command=self.crear_concesionario)
        self.boton_crear.place(x=250, y=75)

        # AGREGAR VEHICULO AL CONCESIONARIO

        # Marca del vehiculo
        self.labelMarca = Label(ventana, text="Marca:")
        self.labelMarca.place(x=30, y=110)
        self.marca = Entry(ventana)
        self.marca.place(x=250, y=110)

        # Modelo del vehiculo
        self.labelModelo = Label(ventana, text="Modelo:")
        self.labelModelo.place(x=30, y=130)
        self.modelo = Entry(ventana)
        self.modelo.place(x=250, y=130)

        # Año del vehiculo
        self.labelAnio = Label(ventana, text="Año:")
        self.labelAnio.place(x=30, y=150)
        self.anio = Entry(ventana)
        self.anio.place(x=250, y=150)

        # Precio del vehiculo
        self.labelPrecio = Label(ventana, text="Precio:")
        self.labelPrecio.place(x=30, y=170)
        self.precio = Entry(ventana)
        self.precio.place(x=250, y=170)

        # Concesionario a ingresar el vehiculo
        self.labelConcesionario = Label(ventana, text="Concesionario deseado para añadir el vehiculo:")
        self.labelConcesionario.place(x=30, y=190)
        self.concesionario = Entry(ventana)
        self.concesionario.place(x=250, y=190)

        #Boton de añadir vehiculo
        self.boton_crear = Button(ventana, text="Añadir vehiculo", command=self.añadir_vehiculo)
        self.boton_crear.place(x=250, y=215)


        ventana.mainloop()

    def crear_concesionario(self):

        try:
            testConcesionario.Concesionario.crear_nuevo_concesionario(self.nombre.get(), self.direccion.get())
            messagebox.showinfo(message="¡Concesionario creado correctamente!")

            self.nombre.delete(0, END)
            self.direccion.delete(0, END)

        except Exception as e:
            messagebox.showerror(message=str(e))

    def añadir_vehiculo(self):

        try:
            testConcesionario.Concesionario.agregar_modelo_a_concesionario(self.marca.get(), self.modelo.get(),
                                                 self.anio.get(), self.precio.get(), self.concesionario.get())

            messagebox.showinfo(message="¡Vehiculo añadido correctamente!")

            self.marca.delete(0, END)
            self.modelo.delete(0, END)
            self.anio.delete(0, END)
            self.precio.delete(0, END)
            self.concesionario.delete(0, END)

        except Exception as e:
            messagebox.showerror(message= str(e))





App()
