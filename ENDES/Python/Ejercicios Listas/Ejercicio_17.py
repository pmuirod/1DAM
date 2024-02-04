# Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación, 
# debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
numero_muiño = int
contador1_muiño = int
contador2_muiño = int

print("Escriba un número")
numero_muiño = int(input())

while numero_muiño>=0:
    lista1_muiño.append(numero_muiño)

    print("Escriba un número")
    numero_muiño = int(input())

print(lista1_muiño)

for i in range(0,len(lista1_muiño)):
    contador1_muiño = i
    contador2_muiño = i+1
    print(contador1_muiño)
    print(contador2_muiño)
    for i in range(contador1_muiño+1,len(lista1_muiño)):
        if lista1_muiño[contador1_muiño] == lista1_muiño[contador2_muiño]:
            print(contador1_muiño)
            print(contador2_muiño)
            contador2_muiño = contador2_muiño+1

print(lista1_muiño)