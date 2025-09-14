'''
25. Realiza un script que pida números hasta que escriba “fin” Si no es un número
deberá indicarse con un «alert» y seguir pidiendo. Al salir con “cancelar” deberá
indicarse la suma total de los números introducidos.
'''

ingreso=input('Ingrese el 1er numero, para terminar ingrese "fin" para salir o "cancelar" para saber la suma total:')
total=0
flag=True


while flag:
    if ingreso=="fin":
        print("Finalizo de forma manual la suma.")
        flag=False
    if ingreso =="cancelar":
        print("La suma total es de:", total)
        flag=False 
    
    if ingreso.isdigit():
        numero=int(ingreso)
        total += numero
        ingreso=input('Ingrese el siguiente numero, para terminar ingrese "fin" para salir o "cancelar" para saber la suma total:')
    else:
        ingreso=input('Error. Ingrese un numero valido, para terminar ingrese "fin" para saliro "cancelar" para saber la suma total:')


