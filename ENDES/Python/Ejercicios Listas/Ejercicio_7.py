# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
lista2_muiño = []
lista3_muiño = []
valor1 = int
valor2 = int
valor3 = int
contador = int

print("Escriba cinco valores para la primera lista:")

for i in range(1,6):
    valor1 = int(input())
    lista1_muiño.append(valor1)

print("Escriba cinco valores para la segunda lista:")

for i in range(1,6):
    valor2 = int(input())
    lista2_muiño.append(valor2)

contador = 0

for i in range(1,6):
    valor3 = (lista1_muiño[contador])+(lista2_muiño[contador])
    lista3_muiño.append(valor3)
    contador = contador+1

print("Los valores de la primera lista son:",lista1_muiño)
print("Los valores de la segunda lista son:",lista2_muiño)
print("Los valores de la tercera lista son:",lista3_muiño)