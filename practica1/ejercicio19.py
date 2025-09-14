#19. Validar que la edad de una persona sea > 0 y <105
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 105:
    print("Su edad es: ", edad)