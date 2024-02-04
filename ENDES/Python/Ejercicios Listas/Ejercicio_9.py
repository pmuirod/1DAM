# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#   - La temperatura media de cada día
#   - Los días con menos temperatura
#   - Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. Si no existe ningún día se muestra un mensaje de información.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
lista2_muiño = []
lista3_muiño = []
media_muiño = int
media_muiño = 0
contador_muiño = int

print("Escriba la temperatura mínima del dia",1)
minima_muiño = int(input())
print("Escriba la temperatura máxima del dia",1)
maxima_muiño = int(input())

menor_muiño = maxima_muiño
contador_muiño = 0

for i in range(2,6):
    if minima_muiño<menor_muiño:
        menor_muiño = minima_muiño

    lista1_muiño.append(minima_muiño)
    lista2_muiño.append(maxima_muiño)
    
    media_muiño = ((lista1_muiño[contador_muiño])+(lista2_muiño[contador_muiño]))/2

    lista3_muiño.append(media_muiño)

    contador_muiño = contador_muiño+1

    print("Escriba la temperatura mínima del dia",i)
    minima_muiño = int(input())
    print("Escriba la temperatura máxima del dia",i)
    maxima_muiño = int(input())

print("La temperatura media de todos los dias son:",lista3_muiño)
print("La temperatura menor en los 5 días es:",menor_muiño,"grados")

print("Escriba una temperatura máxima")
temperatura_muiño = int(input())

if temperatura_muiño in lista2_muiño:
    print("La temperatura máxima coincide con uno de los dias:",lista2_muiño)
else:
    print("La temperatura no coincide con ningún día")