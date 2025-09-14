'''
13. Escribir los números naturales entre 10 y 20
14. Escriba los numeros pares de 0 al 20.
15. Escribir los multiplos de 5 del 1 al 50
16. Escribir los numeros naturales del 100 al 1
17. Escrbir los números pares del 20 al 10
18. Leer numeros hasta que ingrese un 0
19. Validar que la edad de una persona sea > 0 y <105
'''

#13. Escribir los números naturales entre 10 y 20
for i in range(10,21):
    print(i)

#14. Escriba los numeros pares de 0 al 20.
for i in range(2,21,2):
    print(i)

#15. Escribir los multiplos de 5 del 1 al 50
for i in range(5,51,5):
    print(i)

#16. Escribir los numeros naturales del 100 al 1
for i in range(100,0,-1):
    print(i, end="-")

print()


#13Escribir los números naturales entre 10 y 20.
for i in range(10, 21):
    print(i)  

#14 Escriba los numeros pares de 0 al 20.
for n in range(0,21,2):
    print(n)
      
#15. Escribir los multiplos de 5 del 1 al 50
for i in range (1,51):
    if i % 5 == 0:
        print(i)
for i in range(5,51,5):
    print(i, end="-")

#16. Escribir los numeros naturales del 100 al 1
for i in range(100,0,-1):
    print(i, end="-")
print()

for i in range ( 100, 0, -1):
    print(i , end=",")
print()

#17. Escrbir los números pares del 20 al 10
for i in range(20,9, -2):
    print(i)


#18. Leer numeros hasta que ingrese un 0
numero= int(input("Ingrese su edad o 0 para salir: "))

while numero != 0:
    numero= int(input("Ingrese su edad o 0 para salir: "))


#19. Validar que la edad de una persona sea > 0 y <105
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 105:
    print("Su edad es: ", edad)