'''
EJERCICIO: Leer un número entero y decir si es par
EJERCICIO: Leer un número entero y decir si es par o impar
EJERCICIO: Leer un numero entero y decir si es múltiplo de 2, 3 , 5 o 6
EJERCICIO: Leer la edad de una persona y verificar si puede sacar el registro de conducir
'''

#EJERCICIO: Leer un número entero y decir si es par
numero=int(input("Ingrese un numero entero para saver si es par: "))

if numero % 2 == 0:
    print("es par")

#EJERCICIO: Leer un número entero y decir si es par o impar

numero=int(input("Ingrese un numero entero para saber si es par o impar: "))

if numero % 2 == 0:
    print("es par")
else:
    print("es impar")


#EJERCICIO: Leer un numero entero y decir si es múltiplo de 2, 3 , 5 o 6

numero=int(input("Ingrese un numero entero para saber si es multiplo de 2, 3, 5 y/o 6: "))

if numero % 2 == 0:
    print("es multiplo de 2")
if numero % 3 == 0:
    print("es multiplo de 3")
if numero % 5 == 0:
    print("es multiplo de 5")
if numero % 6 == 0:
    print("es multiplo de 6")

#EJERCICIO: Leer la edad de una persona y verificar si puede sacar el registro de conducir
edad = int(input("ingrese su edad para saber si puede sacar su regitro:"))

if edad <18:
    print("No puede sacar un registro")
elif edad > 70:
    print ("No puede sacar un registro")
else:
    print("puede sacar un registro")