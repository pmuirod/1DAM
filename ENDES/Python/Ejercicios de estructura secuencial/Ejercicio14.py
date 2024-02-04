# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

print("Escriba un número")
num = input()

num = str(num)[::-1]

print("El número invertido al anterior es", num)