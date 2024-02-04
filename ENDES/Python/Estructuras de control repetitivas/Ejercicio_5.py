# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
# Por: Pablo Muiño Rodríguez

print("Escriba una serie de letras (espacio para terminar)")
letra_muiño = str(input())

while letra_muiño!=" ":
    if letra_muiño == "a" or letra_muiño == "e" or letra_muiño == "i" or letra_muiño == "o" or letra_muiño == "u":
        print("VOCAL")
    else:
        print("NO VOCAL")
    letra_muiño = str(input())