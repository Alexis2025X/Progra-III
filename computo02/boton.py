import tkinter as tk
class aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana = tk.Tk()
        self.ventana.title("Botones")
        self.ventana.geometry("600x400")

        self.label = tk.Label(self.ventana, text=self.valor)
        self.label.grid(column=1, row=1)
        self.label.config(foreground="red")
        #self.label.place(relx=10, anchor=tk.CENTER)

        self.boton = tk.Button(self.ventana, text="Sumar", command=self.sumar)
        self.boton.grid(column=3, row=3)

        self.boton = tk.Button(self.ventana, text="Resta", command=self.resta)
        self.boton.grid(column=4, row=3)

        self.ventana.mainloop()

    def sumar(self):
        self.valor = self.valor+1
        self.label.config(text=self.valor)

    def resta(self):
        self.valor = self.valor-1
        self.label.config(text=self.valor)
aplicacion()