# 21. Escribir un programa que escriba en pantalla los divisores comunes de dos números dados

numero1=int(input("Ingrese el 1er numero a calcular divisor comun: "))
numero2=int(input("Ingrese el 2do numero: "))
if numero1 < numero2:
    numero_mayor= numero2
elif numero1>numero2:
    numero_mayor=numero1

for i in range (1, numero_mayor+1):
    if numero1 % i == 0 and numero2 % i == 0:
        print("El numero ", i, "es comun divisor de ", numero1, "y de ", numero2)
