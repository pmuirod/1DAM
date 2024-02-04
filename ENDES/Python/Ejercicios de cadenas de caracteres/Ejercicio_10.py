# Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.
# Por: Pablo Muiño Rodríguez

print("Escribe una cadena")
cadena_muiño = input()

reves_muiño = cadena_muiño[::-1]

if reves_muiño == cadena_muiño:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")