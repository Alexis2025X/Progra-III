# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTK")
main.config(bg="#000000")
main.geometry("600x400")


style = ttk.Style(main)
style.theme_use("clam")
valor = 0
style.configure("lblnumero.TLabel", background="#fffcfc", foreground="#000000", font=("TkMenuFont", 13, ))
lblnumero = ttk.Label(master=main, text=valor, style="lblnumero.TLabel")
lblnumero.place(x=274, y=36, width=80, height=40)

style.configure("btndisminuir.TButton", background="#ffffff", foreground="#000")
style.map("btndisminuir.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

btndisminuir = ttk.Button(master=main, text="Disminuir", style="btndisminuir.TButton", command= lambda: disminuir())
btndisminuir.place(x=273, y=173, width=80, height=40)

style.configure("btnaumentar.TButton", background="#ffffff", foreground="#000")
style.map("btnaumentar.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

btnaumentar = ttk.Button(master=main, text="Aumentar", style="btnaumentar.TButton", command= lambda: aumenta())
btnaumentar.place(x=273, y=104, width=80, height=40)

style.configure("btnsalir.TButton", background="#ffffff", foreground="#000000", relief=tk.FLAT, anchor="center")
btnsalir = ttk.Button(master=main, text="Salir", style="btnsalir.TButton", command= lambda: salir())
btnsalir.place(x=276, y=238, width=80, height=40)

lblnumero.configure(anchor="center")
btnsalir.place(x=276, y=238, width=80, height=40)


def aumenta():
    valor = int(lblnumero.cget("text"))
    valor += 1
    lblnumero.configure(text=valor)

def disminuir():
    valor = int(lblnumero.cget("text"))
    valor -= 1
    lblnumero.configure(text=valor)


def salir():
    exit()
    #main.destroy()


main.mainloop()