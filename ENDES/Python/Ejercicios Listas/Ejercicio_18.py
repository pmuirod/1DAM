# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
#   - Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#   - Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.
#   - Eliminar: Me pide una cadena, y la elimina de la lista.
#   - Mostrar: Muestra la lista de cadenas
#   - Terminar
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
respuesta_muiño = int
veces_muiño = int

print("¿Cuántas cadenas quieres poner dentro de la lista?")
cantidad_muiño = int(input())

while cantidad_muiño!=0:
    print("Escriba la",cantidad_muiño,"cadena")
    cadena_muiño = input()
    lista1_muiño.append(cadena_muiño)
    cantidad_muiño = cantidad_muiño-1

print("----MENÚ----")
print("1. Contar")
print("2. Modificar")
print("3. Eliminar")
print("4. Mostrar")
print("5. Terminar")
respuesta_muiño = int(input())

while respuesta_muiño!=5:
    if respuesta_muiño==1:
        print("Escriba una cadena para contar cuántas veces aparece en la lista")
        cadena_muiño = input()
        veces_muiño = lista1_muiño.count(cadena_muiño)
        print("La cadena",cadena_muiño,"aparece",veces_muiño,"veces")
        print()
    if respuesta_muiño==2:
        print("Esciba una cadena para sustituirla por otra")
        cadena_muiño = input()
        print("Indique la cadena a sustituir")
        sustitucion_muiño = input()
        lista1_muiño.insert(sustitucion_muiño,cadena_muiño)
        print()
    if respuesta_muiño==3:
        print("Escriba una cadena para eliminarla")
        cadena_muiño = input()
        lista1_muiño.remove(cadena_muiño)
        print()
    if respuesta_muiño==4:
        print(lista1_muiño)
        print()

    print("----MENÚ----")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")
    respuesta_muiño = int(input())

print("Saliendo del menú...")