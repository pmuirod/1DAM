# Vamos a crear un programa que tenga el siguiente menú:
#   1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#   2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#   3. Longitud de la lista: te muestra el número de elementos de la lista.
#   4. Eliminar el último número: Muestra el último número de la lista y lo borra.
#   5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#   6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#   7. Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#   8. Mostrar números: Muestra los números de la lista
#   9. Salir
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
numero_muiño = int
posicion_muiño = int
respuesta_muiño = int

while respuesta_muiño!="9":
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    print("Introduzca un número para continuar:")
    respuesta_muiño = input()

    if respuesta_muiño=="1":
        print("Escriba un número")
        numero_muiño = int(input())
        lista1_muiño.append(numero_muiño)
    if respuesta_muiño=="2":
        print("Escriba un número")
        numero_muiño = int(input())
        print("Escriba la posición donde insertar su número")
        posicion_muiño = int(input())
        lista1_muiño.insert(posicion_muiño,numero_muiño)
    if respuesta_muiño=="3":
        print("La lista tiene una longitud de",len(lista1_muiño)+1,"elementos")
    if respuesta_muiño=="4":
        lista1_muiño.pop()
    if respuesta_muiño=="5":
        print("Escriba una posición")
        posicion_muiño = int(input())
        lista1_muiño.remove(posicion_muiño)
    if respuesta_muiño=="6":
        print("Escriba un número")
        numero_muiño = int(input())
        lista1_muiño.count(numero_muiño)
    if respuesta_muiño=="7":
        print("Escriba un número")
        numero_muiño = int(input())
        lista1_muiño.index(numero_muiño)
    if respuesta_muiño=="8":
        print(lista1_muiño)
    if respuesta_muiño=="9":
        break