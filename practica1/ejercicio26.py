'''
26. Realizar una página con un script que calcule el valor de la letra de un número de
DNI (Documento Nacional de Identidad). El algoritmo para calcular la letra del dni es
el siguiente :
● El número debe ser entre 0 y 99999999
● Debemos calcular el resto de la división entera entre el número y el número
● Según el resultado, de 0 a 22, le corresponderá una letra de las siguientes: (T, R,
W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E)
● Si lo introducido no es un número deberá indicarse con un alert y volver a
preguntar.
● Deberá de repetirse el proceso hasta que el usuario pulse «cancelar».
'''
letras=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 
        'K', 'E']
dni=input('Ingrese el numero de DNI o "cacelar" para salir : ')

while dni != "cancelar":
    while not dni.isdigit():
        dni=input("ERROR. Ingrese un numero enrte 0 y 99999999: ")
    nroDni=int(dni)
    print(f'La letra correspondiente al Dni ingresado es: {letras[nroDni%22]}')

    dni=input('Ingrese el numero de DNI o "cacelar" para salir : ')
print("Programa terminado")