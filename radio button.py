# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTK")
main.config(bg="#060606")
main.geometry("700x400")


style = ttk.Style(main)
style.theme_use("clam")

style.configure("btncambiar.TButton", background="#ffffff", foreground="#000")
style.map("btncambiar.TButton", background=[("active", "#afafaf")], foreground=[("active", "#000")])

btncambiar = ttk.Button(master=main, text="Cambiar", style="btncambiar.TButton", command= lambda: cambiar_color())
btncambiar.place(x=260, y=234, width=80, height=40)

style.configure("btnsalir.TButton", background="#ffffff", foreground="#000")
style.map("btnsalir.TButton", background=[("active", "#a3a0a0")], foreground=[("active", "#000")])

btnsalir = ttk.Button(master=main, text="Salir", style="btnsalir.TButton", command= lambda: salir())
btnsalir.place(x=261, y=294, width=80, height=40)

rdcolor_var = tk.IntVar()
style.configure("rdcolor.TRadiobutton", background="#ffffff", foreground="#000")
style.map("rdcolor.TRadiobutton", background=[("active", "#998f8f")], foreground=[("active", "#000")])


rdcolor_0 = ttk.Radiobutton(master=main, variable=rdcolor_var, text="Rojo", value=0, style="rdcolor.TRadiobutton")
rdcolor_0.place(x=259, y=79)


rdcolor_1 = ttk.Radiobutton(master=main, variable=rdcolor_var, text="Azul", value=1, style="rdcolor.TRadiobutton")
rdcolor_1.place(x=259, y=100)


rdcolor_2 = ttk.Radiobutton(master=main, variable=rdcolor_var, text="Verde", value=2, style="rdcolor.TRadiobutton")
rdcolor_2.place(x=259, y=122)

def cambiar_color():
    valor = rdcolor_var.get()
    if valor == 0:
        main.config(bg="#ff0000")
    elif valor == 1:
        main.config(bg="#0000ff")
    elif valor == 2:
        main.config(bg="#00ff00")

def salir():
    exit()

main.mainloop()