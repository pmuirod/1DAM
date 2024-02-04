# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
# Por: Pablo Muiño Rodríguez

print("Escriba una cadena")
cadena_muiño = input()
print("Escriba una letra (debe estar dentro de la cadena)")
letra1_muiño = input()
print("Escriba otra letra")
letra2_muiño = input()

for caracter in cadena_muiño:
    if caracter == letra1_muiño:
        print(letra2_muiño,end="")
    else:   
        print(caracter,end="")