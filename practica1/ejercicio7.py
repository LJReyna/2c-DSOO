# 7. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.

num1=int(input("Ingrese el 1er numero: "))
num2=int(input("Ingrese el 2do numero: "))
num3=int(input("Ingrese el 3er numero: "))

if num1>num2 and num1>num3:
    print("El mayor numero es el 1ro : ", num1)
elif num2>num1 and num2>num3:
    print("El mayor numero es el 2do: ", num2)
else:
    print("El mayor numero es el 3ro: ", num3)