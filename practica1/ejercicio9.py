# 9. Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)

opcion = 0
while opcion != 5:
    print("Elija si quiere saber por que numero es divisible:")
    print("    1 - Divisible por 2")
    print("    2 - Divisible por 3")
    print("    3 - Divisible por 5")
    print("    4 - Divisible por 7")
    print("    5 Salir")

    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        num=int(input("Ingrese el numero a calcular: "))
        if num%2 == 0:
            print("El numero ", num, "es divisible po 2.")
        else:
            print("El numero ", num, "no es divisible por 2.")
    elif opcion == 2:
        num=int(input("Ingrese el numero a calcular: "))
        if num%3 == 0:
            print("El numero ", num, "es divisible po 3.")
        else:
            print("El numero ", num, "no es divisible por 3.")
    elif opcion == 3:
        num=int(input("Ingrese el numero a calcular: "))
        if num%5 == 0:
            print("El numero ", num, "es divisible po 5.")
        else:
            print("El numero ", num, "no es divisible por 5.")
    elif opcion == 4:
        num=int(input("Ingrese el numero a calcular: "))
        if num%7 == 0:
            print("El numero ", num, "es divisible po 7.")
        else:
            print("El numero ", num, "no es divisible por 7.")
    elif opcion == 5:
        print("Adios")
    