# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
# Por: Pablo Muiño Rodríguez

print("Escriba una cadena")
cadena_muiño = input()
print("Elija un caracter")
caracter_muiño = input()

contador_muiño=0

for caracter in cadena_muiño:
    if caracter == caracter_muiño:
        contador_muiño = contador_muiño

print("El caracter",caracter_muiño,"se repite",contador_muiño,"veces")