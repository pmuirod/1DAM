# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
# Por: Pablo Muiño Rodríguez

random_muiño = int
contador_muiño = int
lista1_muiño = []
lista2_muiño = []
lista3_muiño = []

contador_muiño = 0

import random

while contador_muiño<10:
    random_muiño = random.randint(1,10)
    cuadrado_muiño = random_muiño**2
    cubo_muiño = random_muiño**3
    lista1_muiño.append(random_muiño)
    lista2_muiño.append(cuadrado_muiño)
    lista3_muiño.append(cubo_muiño)
    contador_muiño = contador_muiño+1

print("Los valores de la lista son:")
print(lista1_muiño)

print("El cuadrado de los valores de la lista es:")
print(lista2_muiño)

print("El cubo de los valores de la lista son:")
print(lista3_muiño)