# 20. Escribir un programa que escriba en pantalla los divisores de un número dado

numero = int(input("Ingrese el numero a calcular: "))

for i in range (1, numero+1):
    if numero % i == 0:
        print("El numero ", numero, "es divisible por: ", i)

