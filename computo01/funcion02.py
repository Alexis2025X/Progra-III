print("-----------------------")
print("-----Kevin Castillo----")
print("--Codigo: ustr007724---")
print("-----------------------")
def probar_numero(num):
    if num > 0:
        print("El numero es positivo")
    elif num < 0:
        print("El numero es negativo")
    else:
        print("El numero es 0")
numero = int(input("Ingrese un numero: "))
probar_numero(numero)