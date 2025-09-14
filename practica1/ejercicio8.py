# 8. Escribe un programa que pida un número y diga si es divisible por 2

num=int(input("Ingrese un numero a saber si es divisible por 2: "))

if num % 2 == 0:
    print("El numero", num, "ES divisible por 2.")
else:
    print("El numero", num, "NO ES divisible por 2")