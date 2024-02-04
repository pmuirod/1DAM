# Por: Pablo Muiño Rodríguez
# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos 
# mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

lista1_muiño = []
dict1_muiño = {}
cantidad_muiño = int
nota_muiño = int
nota_muiño = 0

print("Escriba cuántos alumnos quiere introducir")
cantidad_muiño = int(input())

for i in range(0,cantidad_muiño):
    print("Escriba el nombre del",i,"alumno")
    nombre_muiño = input()
    
    while nota_muiño >= 0:
        print("Indique las notas de",nombre_muiño,"(introduzca un número negativo para parar)")
        nota_muiño = int(input())
        if nota_muiño<0:
            break
        lista1_muiño.append(nota_muiño)

    dict1_muiño[nombre_muiño] = lista1_muiño
    lista1_muiño = {}
    nota_muiño = 0

for clave,valor in dict1_muiño.items():
    print(clave,"->",valor)