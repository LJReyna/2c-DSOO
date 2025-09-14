# 6. Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.

num1=int(input("Ingrese el 1er numero: "))
num2=int(input("Ingrese el 2do numero: "))

if num1<num2:
    print("El mayor numero es el 2do: ", num2)
else:
    print("El mayor numero es el 1ro: ", num1)