# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
# Por: Pablo Muiño Rodríguez

print("Escriba un número")
num_muiño = int(input())

import math
contador_muiño=2
primo_muiño=True

while contador_muiño<(math.sqrt(num_muiño)):
    if (num_muiño%contador_muiño == 0):
        primo = False
    contador_muiño = contador_muiño+1

if primo_muiño==True:
    print("Es primo")
if primo_muiño==False:
    print("No es primo")