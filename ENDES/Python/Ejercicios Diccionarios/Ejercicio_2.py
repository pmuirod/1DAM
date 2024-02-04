# Por: Pablo Muiño Rodríguez
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

dict1_muiño = {}

print("Escriba una palabra")
cadena_muiño = input()

for caracter in cadena_muiño:
    dict1_muiño[caracter] = cadena_muiño.count(caracter)

print("Las claves y sus valores son:")

for clave,valor in dict1_muiño.items():
    print(clave,"->",valor)