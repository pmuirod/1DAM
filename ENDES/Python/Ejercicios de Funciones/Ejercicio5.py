# Pablo Muiño Rodríguez
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

lista1_muino = []
longitud_muino = int
longitud_muino = 0
from Funciones.Funcion5 import calcularMaxMin

print("Escriba una serie de números (introducir un 0 para terminar)")
num_muino = int(input())

while num_muino != 0:
    lista1_muino.append(num_muino)
    longitud_muino += 1
    num_muino = int(input())

calcularMaxMin(lista1_muino,longitud_muino)