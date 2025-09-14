# 1. Escribe un programa que pida una frase y escriba cuantas veces aparece la letra a

frase="Mas vale que aprendamos"
contador=0

for letra in frase:
    if letra == "a":
        contador += 1

print(f"La letra 'a' aparece {contador} veces")

# 5. Crea un array con todas las edades de los estudiantes de su clase. Itere la
# lista utilizando un bucle for y luego muestre todas las edades en la consola

edades=[23, 25, 28, 15]

for i in edades:
    print(f"La edad es: {i}")