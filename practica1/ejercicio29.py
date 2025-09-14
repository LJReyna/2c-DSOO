'''
29. Un script que escriba los números del 1 al 500, que indique cuáles son múltiplos de 4 y de 9 y que cada 5 líneas
muestre una línea horizontal.
Por ejemplo : 1 2 3 4 (Múltiplo de 4) 5 ——————————————
6 7 8 (Múltiplo de 4) 9 (Múltiplo de 9) 10—----------------------------------------
'''
contador = 0
for i in range(1, 501):
    if i % 4 == 0 and i % 5 == 0:
        print(f'{i} (Multiplo de 4 y de 5)', end=" ")
        contador+=1
    elif i % 4 == 0:
        print(f'{i} (Multiplo de 4)', end=" ")
        contador+=1
    elif i % 5 == 0:
        print(f'{i} (Multimplo de 5)', end=" ")
        contador+=1
    else:
        print(i, end=" ")
        contador+=1

    if contador % 5 == 0:
        print('————————————————————'*2)