# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
contador_muiño = int (1)
max_muiño = int (0)
min_muiño = int (0)
suma_muiño = int (0)

print("Escriba cinco notas (comprendidas entre 0-10)")

while contador_muiño<=5:
    nota_muiño = int(input())
    if (nota_muiño>=0) and (nota_muiño<=10):
        lista1_muiño.append(nota_muiño)
        suma_muiño = suma_muiño+nota_muiño
        media_muiño = suma_muiño/contador_muiño
        if contador_muiño==1:
            if nota_muiño>max_muiño:
                max_muiño = nota_muiño
                min_muiño = nota_muiño
                contador_muiño = contador_muiño+1
        else:
            if nota_muiño>max_muiño:
                max_muiño = nota_muiño
                contador_muiño = contador_muiño+1
            if nota_muiño<min_muiño:
                min_muiño = nota_muiño
                contador_muiño = contador_muiño+1
    else:
        print("Se han introducido mal los datos")

print("Las notas son:",lista1_muiño)
print("La nota media es:",media_muiño)
print("La nota más alta es:",max_muiño)
print("La nota más baja es:",min_muiño)