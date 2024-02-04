# Diseñar el algoritmo correspondiente a un programa, que:
#   - Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#   - Carga la tabla con valores numéricos enteros.
#   - Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
lista2_muiño = []
lista3_muiño = []
primeros_muiño = int
segundos_muiño = int
suma_primeros_muiño = int
suma_primeros_muiño = 0
suma_segundos_muiño = int
suma_segundos_muiño = 0
suma_columnas_muiño = int
suma_columnas_muiño = 0
contador_muiño = int
contador_muiño = 0

print("Escriba 5 números")
for i in range(1,6):
    primeros_muiño = int(input())

    lista1_muiño.append(primeros_muiño)

    suma_primeros_muiño = suma_primeros_muiño+primeros_muiño

print("Escriba otros 5 números")
for i in range(1,6):
    segundos_muiño = int(input())

    lista2_muiño.append(segundos_muiño)

    suma_segundos_muiño = suma_segundos_muiño+segundos_muiño

for i in range(1,6):
    suma_columnas_muiño = (lista1_muiño[contador_muiño])+(lista2_muiño[contador_muiño])
    lista3_muiño.append(suma_columnas_muiño)
    contador_muiño = contador_muiño+1

print("La primera lista contiene los valores:",lista1_muiño)
print("La segunda lista contiene los valores:",lista2_muiño)
print("La suma de las filas son respectivamente:",suma_primeros_muiño,",",suma_segundos_muiño)
print("La suma de los datos a modo de columnas son:",lista3_muiño)