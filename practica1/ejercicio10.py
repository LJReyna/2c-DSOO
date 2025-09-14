# 10. Añadir al ejercicio anterior que nos diga por cual de los cuatro es divisible (hay que decir todos por los que es divisible)

num=int(input("Ingrese el numero a calcular: "))
if num%2 == 0:
    divisible2=True
else:
    divisible2=False

if num%3 == 0:
    divisible3=True
else:
    divisible3=False

if num%5 == 0:
    divisible5=True
else:
    divisible5=False

if num%7 == 0:
    divisible7=True
else:
    divisible7=False

if divisible2:
    print("El numero", num ,"es divisible por 2")
if divisible3:
    print("El numero", num ,"es divisible por 3")
if divisible5:
    print("El numero", num ,"es divisible por 5")
if divisible7:
    print("El numero", num ,"es divisible por 7")