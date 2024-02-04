# Programa que lea una cadena por teclado y compruebe si su primera letra tiene una mayúscula.
# Por: Pablo Muiño Rodríguez

print("Escriba una palabra")
cadena = input()

if cadena[0]==cadena[0].upper():
    print("La primera letra de la cadena está en mayúscula")
else:
    print("La primera letra de la cadena no está en mayúscula")