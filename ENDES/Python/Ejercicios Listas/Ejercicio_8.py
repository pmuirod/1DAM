# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
#   - Todos lo alumnos mayores de edad.
#   - Los alumnos mayores (los que tienen más edad)
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
mayor_muiño = int
mayor_muiño = 0

print("Escriba el nomrbe del alumno (* para terminar):")
nombre_muiño = input()
print("Escriba la edad del alumno:")
edad_muiño = int(input())

while nombre_muiño != "*":
    if edad_muiño>=18:
        lista1_muiño.append(nombre_muiño)
    if edad_muiño>=mayor_muiño:
        mayor_muiño = edad_muiño
    print("Escriba el nombre del alumno:")
    nombre_muiño = input()
    if nombre_muiño == "*":
        break
    print("Escriba la edad del alumno:")
    edad_muiño = int(input())

print("Los alumnos mayores de edad son:",lista1_muiño)
print("El o los alumnos mayores tienen",mayor_muiño,"años")