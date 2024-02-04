# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

print("Escriba un número")
num = input()

import math

raíz_cuadrada = num**0.5
raíz_cúbica = math.cbrt(num)

print("La raíz cuadrada de ",num," es ",raíz_cuadrada" y la raíz cúbica es",raíz_cúbica)