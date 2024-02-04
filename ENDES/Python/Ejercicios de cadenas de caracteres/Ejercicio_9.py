# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
# Por: Pablo Muiño Rodríguez

print("Escriba una cadena")
cadena_muiño = input()
print("Escriba una subcadena")
subcadena_muiño = input()

if subcadena_muiño in cadena_muiño:
    print("La subcadena está en la cadena")
else:
    print("La subcadena no está en la cadena")