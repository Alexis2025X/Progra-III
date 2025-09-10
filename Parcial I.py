import tkinter as tk
from pickle import FRAME

"""
class ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de edad")
        self.ventana.geometry("600x400")

        self.lblText = tk.Label(self.ventana, text="Ingrese su año de nacimiento")
        self.lblText.grid(column=0, row=0)

        self.anio = tk.StringVar()
        self.txtanio = tk.Entry(self.ventana, textvariable=self.anio)
        self.txtanio.grid(column=0, row=1)

        self.lblEdad = tk.Label(self.ventana, text=f"Su edad es: ")
        self.lblEdad.grid(column=0, row=2)

        self.btnCalcular = tk.Button(self.ventana, text="Calcular", command=lambda:self.calcular_edad(self.anio))
        self.btnCalcular.grid(column=0, row=3)

        self.ventana.mainloop()

    def calcular_edad(self, anio):
        anioint = int(self.anio.get())
        anio_actaul = 2025
        edad_actual = anio_actaul - anioint
        return self.lblEdad.config(text=f"Su edad es: {edad_actual}")
ventana()
"""
class ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de edad")
        self.ventana.geometry("600x400")

        self.lblText1 = tk.Label(self.ventana, text="Ingrese la nota del laboratorio I")
        self.lblText1.grid(column=0, row=0)

        self.lab1 = tk.StringVar()
        self.txtlab1 = tk.Entry(self.ventana, textvariable=self.lab1)
        self.txtlab1.grid(column=0, row=1)

        self.lblText2 = tk.Label(self.ventana, text="Ingrese la nota del laboratorio I")
        self.lblText2.grid(column=0, row=2)

        self.lab2 = tk.StringVar()
        self.txtlab2 = tk.Entry(self.ventana, textvariable=self.lab2)
        self.txtlab2.grid(column=0, row=3)


        self.lblText4 = tk.Label(self.ventana, text="Ingrese la nota del parcial")
        self.lblText4.grid(column=0, row=6)

        self.parcial = tk.StringVar()
        self.txtparcial = tk.Entry(self.ventana, textvariable=self.parcial)
        self.txtparcial.grid(column=0, row=7)

        self.lblNota = tk.Label(self.ventana, text=f"Su promedio es: ")
        self.lblNota.grid(column=0, row=8)

        self.btnCalcular = tk.Button(self.ventana, text="Calcular", command=lambda:self.calcular_promedio(self.lab1, self.lab2, self.parcial))
        self.btnCalcular.grid(column=0, row=9)

        self.ventana.mainloop()

    def calcular_promedio(self, lab1, lab2, parcial):
        lab1int = int(self.lab1.get())
        lab2int = int(self.lab2.get())
        parcialint = int(self.parcial.get())

        lab1intlisto = lab1int * 0.30
        lab2intlisto = lab2int * 0.30
        parcialintlisto = parcialint * 0.40
        resul = lab1intlisto + lab2intlisto + parcialintlisto
        resultado = resul

        return self.lblNota.config(text=f"Su promedio es: {resultado}")
ventana()
"""
import wx
aplicacion = wx.App
ventana = wx.Frame(parent=None, title="Con wxPython")
ventana.Show()
aplicacion.MainLoop()
"""