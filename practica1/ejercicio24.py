# 24. Leer 30 números y decir cual es el mayor

mayor=0

for i in range(30):
    numero=int(input("Ingrese el numero: "))
    if numero>mayor:
        mayor = numero
    

print("El mayor numero ingresado es el: ",mayor)
