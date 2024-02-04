# Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.

from Funciones.Funcion8 import factorial
num_muino = int

print("Escriba un número")
num_muino = int(input())

print("El factorial de",num_muino,"es",factorial(num_muino))