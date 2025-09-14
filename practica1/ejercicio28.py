'''
28. Haz un script que escriba una pirámide inversa de los números del 1 al número que
indique el usuario de la siguiente forma : (suponiendo que indica 6).
666666
55555
4444
333
22
1
'''

numero=int(input("ngrese el numero para hacer el calculo: "))

for i in range(numero,0,-1):
    print(f"{i}"*i)