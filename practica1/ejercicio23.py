# 23. Realiza un script que pida cadenas de texto hasta que escriba “fin”. Al salir deben mostrarse todas las cadenas concatenadas con un guión

linea=input('Ingrese el texto a concatenar o escriba "fin" para salir: ')
oracion=""

while linea != "fin":
    oracion = oracion + linea + "-"
    linea=input('Ingrese el texto a concatenar o escriba "fin" para salir: ')

print(oracion)