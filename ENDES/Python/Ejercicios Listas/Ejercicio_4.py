# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
num_muiño = int

print("Escriba una serie de números")
num_muiño = int(input())

while num_muiño>0:
    lista1_muiño.append(num_muiño)
    num_muiño = int(input())

print("Se han introducido los datos:",lista1_muiño)