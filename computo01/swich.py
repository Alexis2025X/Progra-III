"""
def operaciones(ope, num1, num2):
    if ope == "suma":
       return num1 + num2
    elif ope == "resta":
        return  num1-num2
    elif ope == "division":
        return num1/num2

print("---suma------")
print("---resta-----")
print("---division--")
operacion = input("Elija la operación: ")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print(operaciones(operacion, numero1, numero2))
"""

"""
#Con lambda
def operaciones(ope, num1, num2):
    return {
        "suma": lambda : num1+num2,
        "resta": lambda : num1-num2,
        "multi": lambda : num1*num2,
        "divi": lambda : num1/num2
    }.get(ope, lambda: None)

print("---suma------")
print("---resta-----")
print("---multi-----")
print("---divi------")
operacion = input("Elija la operación: ")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
resultado = operaciones(operacion, numero1, numero2)()
print(resultado)
"""

#match
nota = int(input("Ingrese su nota: "))

match nota:
    case 10 | 9 | 8:
        print("Excelente jovenaso")
    case 7 | 6 | 5:
        print("Mmm necesitas mejorar joven")
    case 4 | 3 | 2 | 0:
        print("Y turismo no te gusta?")
    case _:
        print("Estudia más")
