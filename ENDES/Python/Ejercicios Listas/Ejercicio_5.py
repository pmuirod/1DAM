# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
# Por: Pablo Muiño Rodríguez

random_muiño = int
lista1_muiño = []

import random

for i in range(1,11):
    random_muiño = random.randint(1,10)
    lista1_muiño.append(random_muiño)

print("Valores iniciales de la lista:",lista1_muiño)

lista1_muiño.sort()

print("Valores ordenados:",lista1_muiño)