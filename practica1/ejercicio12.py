# 12. Pide una nota (número). Muestra la calificación según la nota: ● 0-3.99: Insuficiente ● 4 -7: Bien ● 7-9: Notable ● 9-10: Sobresaliente

nota=int(input("Ingrese la nota: "))

if nota >=0 and nota <4:
    print("Insuficiente")
elif nota >= 4 and nota <=7:
    print("Bien")
elif nota >7 and nota<9:
    print("Notable")
elif nota>=9 and nota<=10:
    print("Sobresaliente")
else:
    print("Nota invalida")