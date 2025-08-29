import tkinter as tk

class aplicacion01:
    def __init__(self):
        self.formulario = tk.Tk()
        self.formulario.title("Operaciones")
        self.formulario.geometry("600x400")

        self.label = tk.Label(self.formulario, text="Ingrese el primer numero")
        self.label.grid(column=0, row=0)

        self.dato = tk.StringVar()
        self.entry = tk.Entry(self.formulario, width=10, textvariable = self.dato)
        self.entry.grid(column=0, row=1)

        self.label2 = tk.Label(self.formulario, text="Ingrese el primer numero")
        self.label2.grid(column=0, row=2)

        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.formulario, width=10, textvariable = self.dato2)
        self.entry2.grid(column=0, row=3)
        #self.label = tk.Label(self.formulario, text="Ingrese el segundo numero")

        self.boton = tk.Button(self.formulario, text="Suma", command=self.calcular)
        self.boton.grid(column=0,row=4)
        self.resul = tk.Label(self.formulario, text="resultado: ")
        self.resul.grid(column=0, row=5)

        self.formulario.mainloop()

    def calcular(self):
        valor = int(self.dato.get())
        valor2 = int(self.dato2.get())
        suma = valor+ valor2
        self.resul.config(text=f"resultado: {suma}")

aplicacion01()