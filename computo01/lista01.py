
print("___________________")
print("_Lista-sumar todos_")
print("___________________")
#Solicitar un numero final de la lista
num1=int(input("ingrese un numero hasta 100: "))
if num1 > 100:
    print("Error escribe un numero menor o igual a 100")
else:
    #crea la lista desde 1 hasta el final
    lista = list(range(1, num1+1))
    #calcular la suma
    resultado=sum(lista)
    #imprimir el resultado
    print(f"La suma de la lista hasta {num1} es {resultado}")
"""
x = 0
numeros = [1, 2, 3, 4, 5, 6]
for i in range(len(numeros)):
    x+= numeros[i]
    print(x)
    #range(star, stop, step)
    #range(stop, step)
    #range(step)
"""