# Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: 
# Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
# Por: Pablo Muiño Rodríguez

print("Escriba un número")
num_muiño = int(input())

import math

raiz_muiño = math.sqrt(num_muiño)

if (raiz_muiño*raiz_muiño)!=num_muiño:
    print("Su número es primo")
else:
    print("Su número no es primo")