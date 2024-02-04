# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
# Por: Pablo Muiño Rodríguez

print("Escriba una cadena")
cadena_muiño = input()

for caracter in cadena_muiño:
    if caracter == caracter.upper():
        print(caracter.lower(),end="")
    else:
        print(caracter.upper(),end="")