# calculadora

#operacion = input("Ingrese la operacion, suma, resta, multi, divi: ")
print("*** 1 Suma **************\n"
      "*** 2 Resta *************\n"
      "*** 3 Multiplicación ****\n"
      "*** 4 División ***********")
operacion = input("Elija una opción: ")
if operacion == "1":
    print("Selecciono suma")
    x = float(input("ingrese num1: "))
    y = float(input("ingrese num2: "))
    r = x+y
    print("El resulatado es:", r)
elif operacion == "2":
    print("Selecciono resta")
    x = float(input("ingrese num1: "))
    y = float(input("ingrese num2: "))
    r = x-y
    print("El resultado es:", r)
elif operacion == "3":
    print("Selecciono multiplicación")
    x = float(input("ingrese num1: "))
    y = float(input("ingrese num2: "))
    r = x*y
    print("El resultado es:", r)
elif operacion == "4":
    print("Selecciono división")
    x = float(input("ingrese num1: "))
    y = float(input("ingrese num2: "))
    r = x/y
    print("El resultado es:", r)
else:
    print("Esa opción no esta disponible")