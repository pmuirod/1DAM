# Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.
# Por: Pablo Muiño Rodríguez

print("Escriba su nombre")
nombre_muiño = input()

nombre_muiño = nombre_muiño.title()
for caracter in nombre_muiño:
    if caracter == caracter.upper():
        print(caracter,end="")