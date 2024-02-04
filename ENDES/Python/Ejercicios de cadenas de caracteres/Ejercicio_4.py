# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
# Por: Pablo Muiño Rodríguez

print("Escriba una cadena")
cadena_muiño = input()

contador_muiño=1

for caracter in cadena_muiño:
    if caracter == " ":
        contador_muiño = contador_muiño+1

print("Hay",contador_muiño,"palabras")