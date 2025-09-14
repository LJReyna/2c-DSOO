'''
# Mostrar por pantalla los numeros del 10 al 20

for i in range(10, 21):
    print(i)

# Mostrar numeros pares del 2 al 14 uno al lado del otro
for i in range(2,15,2):
    print(i, end=", ")

print()

# Mostrar los numeros impares del 100 al 4
for i in range(99,4,-1):
    print(i, end=", ")

print()

# Mostrar todos los numeros del 0 al 20
for i in range(0,21,1):
    print(i, end=", ")

print()

for i in range(21):
    print(i, end="-")
'''


'''#EJERCICIO 38: Ingresar la cantidad de alumnos de un curso, leer nombre y nota de cada uno, mostrar los datos ingresados y al finalizar mostrar 
#              el promedio de notas de los alumnos

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
while cantidad_alumnos<0:
    cantidad_alumnos = int(input("Error - Ingrese la cantidad de alumnos: "))
suma_notas=0

for i in range(cantidad_alumnos):
    nombre= input("Ingrese el nombre del alumno: ")
    nota= float(input("Ingrese la nota del alumno: "))
    while nota <0 or nota >10:
        nota= float(input("Error - Ingrese la nota del alumno: "))

    print("El alumno ", nombre, "tiene una nota de: ", nota)
    suma_notas += nota

print("El promedio de los ", cantidad_alumnos ,"alumnos es de: ",suma_notas/cantidad_alumnos)
'''

'''
EJERCICIO 30: Programar el  menu para una  calculadora: 
Menu
    1 suma
    2 resta
   3 ,multiplicacion
   4 division
   5 Salir    
Ingrese una opcion:
'''
opcion = 0
while opcion != 5:
    print("Menu:")
    print("    1 Suma")
    print("    2 Resta")
    print("    3 Multiplicacion")
    print("    4 Division")
    print("    5 Salir")

    opcion = int(input("Ingrese su opcion: "))


    if opcion == 1:
        numero1=float(input("Ingrese el primer numero a sumar: "))
        numero2=float(input("Ingrese el segundo numero a sumar: "))
        print("La suma es: ", numero1 + numero2)      
    elif opcion == 2:
        numero1=float(input("Ingrese el primer numero a restar: "))
        numero2=float(input("Ingrese el segundo numero a restar: "))
        print("La resta es: ", numero1 - numero2)
    elif opcion == 3:
        numero1=float(input("Ingrese el primer numero a multiplicar: "))
        numero2=float(input("Ingrese el segundo numero a multiplicar: "))
        print("La multiplicacion es: ", numero1*numero2)
    elif opcion == 4:
        numero1=float(input("Ingrese el numero a dividir: "))
        numero2=float(input("Ingrese el  numero divisor: "))
        if numero2==0:
            numero2=float(input("Error - Ingrese un numero distinto de 0: "))
        print("La division es igual a: ", numero1/numero2)
    elif opcion == 5:
        print("Chau")
    

