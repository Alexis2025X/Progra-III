import re
import tkinter as tk
import messagebox

from calculadora import operacion

""""
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
"""
class ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        self.ventana.config(background="#1f1f23")

        self.centrar_form()

        self.num1 = tk.StringVar()
        self.txtNumero1 = tk.Entry(self.ventana, textvariable=self.num1)
        self.txtNumero1.pack(padx=5, pady=5)
        Num1 = 0
        op = ""
        Num2 = ""
        """
        self.num2 = tk.StringVar()
        self.txtNumero2 = tk.Entry(self.ventana, background="blue", textvariable=self.num2)
        self.txtNumero2.grid(column=1, row=1, padx=190)
        self.txtNumero2.destroy()
        """
        self.frame = tk.Frame(self.ventana, width=320, height=300, background="#1f1f23")
        self.frame.pack()
        self.btnSiete = tk.Button(self.frame, text="7", command=lambda: self.siete())
        self.btnSiete.grid(column=2, row=4, padx=5, pady=2)
        self.btnSiete.config(width=6, height=2)

        self.btnOcho = tk.Button(self.frame, text="8", command=lambda: self.ocho())
        self.btnOcho.grid(column=3, row=4, padx=5, pady=2)
        self.btnOcho.config(width=6, height=2)

        self.btnNueve = tk.Button(self.frame, text="9", command=lambda: self.nueve())
        self.btnNueve.grid(column=4, row=4, padx=5, pady=2)
        self.btnNueve.config(width=6, height=2)

        self.btnDivision = tk.Button(self.frame, text="÷", command=lambda: self.divi())
        self.btnDivision.grid(column=5, row=4, padx=5, pady=2)
        self.btnDivision.config(width=6, height=2)

        #Fila 2
        self.btnCuatro = tk.Button(self.frame, text="4", command=lambda: self.cuatro())
        self.btnCuatro.grid(column=2, row=5, padx=5, pady=2)
        self.btnCuatro.config(width=6, height=2)

        self.btnCinco = tk.Button(self.frame, text="5", command=lambda: self.cinco())
        self.btnCinco.grid(column=3, row=5, padx=5, pady=2)
        self.btnCinco.config(width=6, height=2)

        self.btnSeis = tk.Button(self.frame, text="6", command=lambda: self.seis())
        self.btnSeis.grid(column=4, row=5, padx=5, pady=2)
        self.btnSeis.config(width=6, height=2)

        self.btnDivision = tk.Button(self.frame, text="×", command=lambda: self.multi())
        self.btnDivision.grid(column=5, row=5, padx=5, pady=2)
        self.btnDivision.config(width=6, height=2)

        #Fila 3
        self.btnUno = tk.Button(self.frame, text="1", command=lambda: self.uno())
        self.btnUno.grid(column=2, row=6, padx=5, pady=2)
        self.btnUno.config(width=6, height=2)

        self.btnDos = tk.Button(self.frame, text="2", command=lambda: self.dos())
        self.btnDos.grid(column=3, row=6, padx=5, pady=2)
        self.btnDos.config(width=6, height=2)

        self.btnTres = tk.Button(self.frame, text="3", command=lambda: self.tres())
        self.btnTres.grid(column=4, row=6, padx=5, pady=2)
        self.btnTres.config(width=6, height=2)

        self.btnResta = tk.Button(self.frame, text="-", command=lambda: self.rest())
        self.btnResta.grid(column=5, row=6, padx=5, pady=2)
        self.btnResta.config(width=6, height=2)

        #Fila 4
        self.btnIgual = tk.Button(self.frame, text="=", command=lambda: self.operacion())
        self.btnIgual.grid(column=2, row=7, padx=5, pady=2)
        self.btnIgual.config(width=6, height=2)

        self.btnCero = tk.Button(self.frame, text="0", command=lambda: self.cero())
        self.btnCero.grid(column=3, row=7, padx=5, pady=2)
        self.btnCero.config(width=6, height=2)

        self.btnPunto = tk.Button(self.frame, text=".", command=lambda: self.punto())
        self.btnPunto.grid(column=4, row=7, padx=5, pady=2)
        self.btnPunto.config(width=6, height=2)

        self.btnSuma = tk.Button(self.frame, text="+", command=lambda: self.sum())
        self.btnSuma.grid(column=5, row=7, padx=5, pady=2)
        self.btnSuma.config(width=6, height=2)

        self.btnLimpiar = tk.Button(self.frame, text="C", command=lambda: self.limpiar())
        self.btnLimpiar.grid(column=4, row=8, padx=5, pady=2)
        self.btnLimpiar.config(width=6, height=2)





        self.ventana.mainloop()
    def centrar_form(self):
        self.ancho_formulario = 520
        self.alto_formulario = 500
        self.ventana.geometry(f"{self.ancho_formulario}x{self.alto_formulario}")

        self.ancho_pantalla = self.ventana.winfo_screenwidth()
        self.alto_pantalla = self.ventana.winfo_screenheight()
        self.posicion_x = (self.ancho_pantalla // 2) - (self.ancho_formulario // 2)
        self.posicion_y = (self.alto_pantalla // 2) - (self.alto_formulario // 2)
        return self.ventana.geometry(f"{self.ancho_formulario}x{self.alto_formulario}+{self.posicion_x}+{self.posicion_y}")

    def nueve(self):
        self.txtNumero1.insert(tk.END,"9")
    def ocho(self):
        self.txtNumero1.insert(tk.END,"8")
    def siete(self):
        self.txtNumero1.insert(tk.END, "7")
    def seis(self):
        self.txtNumero1.insert(tk.END, "6")
    def cinco(self):
        self.txtNumero1.insert(tk.END, "5")
    def cuatro(self):
        self.txtNumero1.insert(tk.END, "4")
    def tres(self):
        self.txtNumero1.insert(tk.END, "3")
    def dos(self):
        self.txtNumero1.insert(tk.END, "2")
    def uno(self):
        self.txtNumero1.insert(tk.END, "1")
    def cero(self):
        self.txtNumero1.insert(tk.END, "0")
    def rest(self):
        self.txtNumero1.insert(tk.END, "-")
    def sum(self):
        self.txtNumero1.insert(tk.END, "+")
    def multi(self):
        self.txtNumero1.insert(tk.END, "×")
    def divi(self):
        self.txtNumero1.insert(tk.END, "÷")
    def punto(self):
        self.txtNumero1.insert(tk.END, ".")
    def limpiar(self):
        self.txtNumero1.delete(tk.END, tk.END)

    def operacion(self, num1, op, num2):
        match op:
            case "+":
                resul = num1 + num2
                self.txtNumero1.delete(tk.END, tk.END)
                return self.txtNumero1.insert(tk.END, resul)
            case "-":
                resul = num1 - num2
                self.txtNumero1.delete(tk.END, tk.END)
                return self.txtNumero1.insert(tk.END, resul)
            case "×":
                resul = num1 * num2
                self.txtNumero1.delete(tk.END, tk.END)
                return self.txtNumero1.insert(tk.END, resul)
            case "÷":
                resul = num1 / num2
                self.txtNumero1.delete(tk.END, tk.END)
                return self.txtNumero1.insert(tk.END, resul)

ventana()
"""
class form:
    def __init__(self):
        self.formulario_registro = tk.Tk()
        self.formulario_registro.title("Formulario de registro")

        self.formulario_registro.config(background="#1f1f23")

        self.centrar_form()

        self.lblnombre = tk.Label(self.formulario_registro, text="Nombre: ")
        self.lblnombre.config(background="#1f1f23", foreground="#fff")
        self.lblnombre.grid(column=1,row=1)

        self.nombre = tk.StringVar()
        self.txtNombre = tk.Entry(self.formulario_registro, textvariable=self.nombre)
        self.txtNombre.grid(column=2, row=1, pady=10)

        self.lblEmail = tk.Label(self.formulario_registro, text="Email: ")
        self.lblEmail.config(background="#1f1f23", foreground="#fff")
        self.lblEmail.grid(column=1,row=2, pady=10)

        self.email = tk.StringVar()
        self.txtEmail = tk.Entry(self.formulario_registro, textvariable=self.email)
        self.txtEmail.grid(column=2, row=2, pady=10)

        self.lblEdad = tk.Label(self.formulario_registro, text="Edad: ")
        self.lblEdad.config(background="#1f1f23", foreground="#fff")
        self.lblEdad.grid(column=1,row=3, pady=10)

        self.edad = tk.StringVar()
        self.txtEdad = tk.Entry(self.formulario_registro, textvariable=self.edad)
        self.txtEdad.grid(column=2, row=3, pady=10)

        self.btnRegistrar = tk.Button(self.formulario_registro, text="Registrar", command=lambda:self.funciones(self.nombre, self.email, self.edad))
        self.btnRegistrar.grid(column=2, row=7, pady=10)

        self.formulario_registro.mainloop()
    def funciones(self, nombre, email, edad):
        if self.campo_vacio(nombre, email, edad) == True:
           if self.correo_valido(email) == True:
            if self.edad_valido(edad) == True:
                messagebox.showinfo("Exito", "Se ha registrado con exito")


    def correo_valido(self, correo):
        correo = str(correo.get())
        if not "@" in correo:
            messagebox.showerror("Error", "Ingrese un correo valido")
            return False
        elif not "." in correo:
            messagebox.showerror("Error", "Ingrese un correo valido")
            return False
        else:
            return True

    def edad_valido(self, edad):
        edad = int(self.edad.get())
        if edad < 18:
            try:
                messagebox.showerror("Error", "La edad debe ser mayor a 18")
                return False
            except Exception:
                messagebox.showerror("Error", "Solo se aceptan número en el campo EDAD")
                return False
        else:
            return True

    def campo_vacio(self, nombre, email, edad):
        if len(nombre.get()) == 0 and len(email.get()) == 0 and len(edad.get()) == 0:
            messagebox.showerror("Error", "Los campos no pueden estar vacio")
            return False
        elif len(nombre.get()) == 0:
            messagebox.showerror("Error", "El campo NOMBRE no puede estar vacio")
            return False
        elif len(email.get()) == 0:
            messagebox.showerror("Error", "El campo EMAIL no puede estar vacio")
            return False
        elif len(edad.get()) == 0:
            messagebox.showerror("Error", "El campo EDAD no puede estar vacio")
            return False
        else:
            return True
    def centrar_form(self):
        self.ancho_formulario = 220
        self.alto_formulario = 200
        self.formulario_registro.geometry(f"{self.ancho_formulario}x{self.alto_formulario}")

        self.ancho_pantalla = self.formulario_registro.winfo_screenwidth()
        self.alto_pantalla = self.formulario_registro.winfo_screenheight()
        self.posicion_x = (self.ancho_pantalla // 2) - (self.ancho_formulario // 2)
        self.posicion_y = (self.alto_pantalla // 2) - (self.alto_formulario // 2)
        return self.formulario_registro.geometry(f"{self.ancho_formulario}x{self.alto_formulario}+{self.posicion_x}+{self.posicion_y}")


form()
"""