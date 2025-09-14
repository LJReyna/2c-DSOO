# 22. Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)

numero=int(input("Ingrese el numero a saber si es primo: "))
primo=True

for i in range (2, numero):
    if numero % i == 0:
        primo=False

if primo:
    print("El numero", numero, "es primo.")
else:
    print("El numero", numero, "no es primo.")
