# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
# Por: Pablo Muiño Rodríguez

suma_muiño = int
contador_muiño = int
media_muiño = int

print("Introduzca una serie de números")
num_muiño = int(input())

suma_muiño = num_muiño
contador_muiño = 1
media_muiño = 0

while num_muiño!=0:
    num_muiño = int(input())

    suma_muiño = suma_muiño + num_muiño
    contador_muiño = contador_muiño + 1

media_muiño = suma_muiño/contador_muiño

print("La media de los números es",media_muiño)