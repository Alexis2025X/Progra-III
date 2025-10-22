import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from datetime import datetime
import empleados

class FormularioEmpleados:
    def __init__(self):
        self.empleado1=empleados.Empleados() #Llamamos a la clase Empleados
        self.ventana1=tk.Tk()
        self.ventana1.title("Administración de empleados")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_empleados()
        self.consulta_por_id()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_empleados(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Empleado")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.Nombrecarga=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe1, textvariable=self.Nombrecarga)
        self.entryNombre.grid(column=1, row=0, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe1, text="Apellido Paterno:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.Apellido_Paternocarga=tk.StringVar()
        self.entryApellido_Paterno=ttk.Entry(self.labelframe1, textvariable=self.Apellido_Paternocarga)
        self.entryApellido_Paterno.grid(column=1, row=1, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe1, text="Apellido Materno:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.Apellido_Maternocarga=tk.StringVar()
        self.entryApellido_Materno=ttk.Entry(self.labelframe1, textvariable=self.Apellido_Maternocarga)
        self.entryApellido_Materno.grid(column=1, row=2, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe1, text="Email:")
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.Emailcarga=tk.StringVar()
        self.entryEmail=ttk.Entry(self.labelframe1, textvariable=self.Emailcarga)
        self.entryEmail.grid(column=1, row=3, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe1, text="Fecha de contrato:")
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.Fecha_Contratocarga=tk.StringVar()
        self.entryFecha_Contrato=ttk.Entry(self.labelframe1, textvariable=self.Fecha_Contratocarga)
        self.entryFecha_Contrato.grid(column=1, row=4, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe1, text="Notas:")
        self.label2.grid(column=0, row=5, padx=4, pady=4)
        self.Notascarga=tk.StringVar()
        self.entryNotas=ttk.Entry(self.labelframe1, textvariable=self.Notascarga)
        self.entryNotas.grid(column=1, row=5, padx=4, pady=4)
        #
        self.boton1=ttk.Button(self.labelframe1, text="Guardar", command=self.agregar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)

    def agregar(self):
        if self.formato_valido(self.Fecha_Contratocarga.get()):#False
            return
        else:
            datos=(self.Nombrecarga.get(), self.Apellido_Paternocarga.get(), self.Apellido_Maternocarga.get(), self.Emailcarga.get(), self.Fecha_Contratocarga.get(), self.Notascarga.get())
            self.empleado1.alta(datos)
            mb.showinfo("Información", "Los datos fueron cargados con exito")
            self.Nombrecarga.set("")
            self.Apellido_Paternocarga.set("")
            self.Apellido_Maternocarga.set("")
            self.Emailcarga.set("")
            self.Fecha_Contratocarga.set("")
            self.Notascarga.set("")

    def consulta_por_id(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por ID")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Empleado")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.id_empleado=tk.StringVar()
        self.entryid_empleado=ttk.Entry(self.labelframe2, textvariable=self.id_empleado)
        self.entryid_empleado.grid(column=1, row=0, padx=4, pady=4)

        self.label1=ttk.Label(self.labelframe2, text="Nombre:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.Nombre=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe2, textvariable=self.Nombre, state="readonly")
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe2, text="Apellido Paterno:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.Apellido_Paterno=tk.StringVar()
        self.entryApellido_Paterno=ttk.Entry(self.labelframe2, textvariable=self.Apellido_Paterno, state="readonly")
        self.entryApellido_Paterno.grid(column=1, row=2, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe2, text="Apellido Materno:")
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.Apellido_Materno=tk.StringVar()
        self.entryApellido_Materno=ttk.Entry(self.labelframe2, textvariable=self.Apellido_Materno, state="readonly")
        self.entryApellido_Materno.grid(column=1, row=3, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe2, text="Email:")
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.Email=tk.StringVar()
        self.entryEmail=ttk.Entry(self.labelframe2, textvariable=self.Email, state="readonly")
        self.entryEmail.grid(column=1, row=4, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe2, text="Fecha de contrato:")
        self.label2.grid(column=0, row=5, padx=4, pady=4)
        self.Fecha_Contrato=tk.StringVar()
        self.entryFecha_Contrato=ttk.Entry(self.labelframe2, textvariable=self.Fecha_Contrato, state="readonly")
        self.entryFecha_Contrato.grid(column=1, row=5, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe2, text="Notas:")
        self.label2.grid(column=0, row=6, padx=4, pady=4)
        self.Notas=tk.StringVar()
        self.entryNotas=ttk.Entry(self.labelframe2, textvariable=self.Notas, state="readonly")
        self.entryNotas.grid(column=1, row=6, padx=4, pady=4)
        #
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    def consultar(self):
            datos=(self.id_empleado.get(),)
            respuesta=self.empleado1.consulta(datos)
            if len(respuesta)>0:
                self.Nombre.set(respuesta[0][0])
                self.Apellido_Paterno.set(respuesta[0][1])
                self.Apellido_Materno.set(respuesta[0][2])
                self.Email.set(respuesta[0][3])
                self.Fecha_Contrato.set(respuesta[0][4])
                self.Notas.set(respuesta[0][5])
            else:
                self.Nombrecarga.set("")
                self.Apellido_Paternocarga.set("")
                self.Apellido_Maternocarga.set("")
                self.Emailcarga.set("")
                self.Fecha_Contratocarga.set("")
                self.Notascarga.set("")
                mb.showinfo("Información", "No existe un empleado con dicho ID")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de Empleados")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Empleado")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe4, text="ID de empleado:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idborra = tk.StringVar()
        self.entryborra = ttk.Entry(self.labelframe4, textvariable=self.idborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.idborra.get(),)
        cantidad = self.empleado1.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", f"Se borró el empleado con dicho ID {self.idborra.get()}")
        else:
            mb.showinfo("Información", f"No existe un empleado con ID {self.idborra.get()}")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar Empleado")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Empleado")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe5, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.id_empleadomod=tk.StringVar()
        self.entryid_empleado=ttk.Entry(self.labelframe5, textvariable=self.id_empleadomod)
        self.entryid_empleado.grid(column=1, row=0, padx=4, pady=4)

        self.label1=ttk.Label(self.labelframe5, text="Nombre:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.Nombremod=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe5, textvariable=self.Nombremod)
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe5, text="Apellido Paterno:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.Apellido_Paternomod=tk.StringVar()
        self.entryApellido_Paterno=ttk.Entry(self.labelframe5, textvariable=self.Apellido_Paternomod)
        self.entryApellido_Paterno.grid(column=1, row=2, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe5, text="Apellido Materno:")
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.Apellido_Maternomod=tk.StringVar()
        self.entryApellido_Materno=ttk.Entry(self.labelframe5, textvariable=self.Apellido_Maternomod)
        self.entryApellido_Materno.grid(column=1, row=3, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe5, text="Email:")
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.Emailmod=tk.StringVar()
        self.entryEmail=ttk.Entry(self.labelframe5, textvariable=self.Emailmod)
        self.entryEmail.grid(column=1, row=4, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe5, text="Fecha de contrato:")
        self.label2.grid(column=0, row=5, padx=4, pady=4)
        self.Fecha_Contratomod=tk.StringVar()
        self.entryFecha_Contrato=ttk.Entry(self.labelframe5, textvariable=self.Fecha_Contratomod)
        self.entryFecha_Contrato.grid(column=1, row=5, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe5, text="Notas:")
        self.label2.grid(column=0, row=6, padx=4, pady=4)
        self.Notasmod=tk.StringVar()
        self.entryNotas=ttk.Entry(self.labelframe5, textvariable=self.Notasmod)
        self.entryNotas.grid(column=1, row=6, padx=4, pady=4)
        #

        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=7, padx=4, pady=4)

    def modifica(self):

        if self.formato_valido(self.Fecha_Contratomod.get()):#False
            return
        else:
            datos = (self.Nombremod.get(), self.Apellido_Paternomod.get(), self.Apellido_Maternomod.get(),
                     self.Emailmod.get(), self.Fecha_Contratomod.get(), self.Notasmod.get(), self.id_empleadomod.get())
            cantidad = self.empleado1.modificacion(datos)
            if cantidad == 1:
                mb.showinfo("Información", "Se modificó el empleado")
                self.id_empleadomod.set("")
                self.Nombremod.set("")
                self.Apellido_Paternomod.set("")
                self.Apellido_Maternomod.set("")
                self.Emailmod.set("")
                self.Fecha_Contratomod.set("")
                self.Notasmod.set("")
            else:
                mb.showinfo("Información", "No existe un empleado con dicho ID")
    def formato_valido(self, fecha_str):
        try:
            formato_esperado ="%Y-%m-%d"
            datetime.strptime(fecha_str, formato_esperado)
            return False
        except(ValueError):
            mb.showinfo("Información", "Se espera el siguiente formato YYYY-MM-DD")
            return True

        #self.formato_valido("2008-01-03")


aplicacion1=FormularioEmpleados()