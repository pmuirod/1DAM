# Por: Pablo Muiño Rodríguez
# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
#   - Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. 
#     Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#   - Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#   - Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#   - Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

dict1_muiño = {}
numero_muiño = int
respuesta_muiño = int
respuesta_muiño = 0

print("Bienvenido a la agenda, ¿que desea hacer?")

while respuesta_muiño != 5:
    print("")
    print("1.Añadir/modificar")
    print("2.Buscar")
    print("3.Borrar")
    print("4.Listar")
    print("5.Salir")
    respuesta_muiño = int(input())

    if respuesta_muiño == 1:
        print("Escriba un nombre")
        nombre_muiño = input()
        if nombre_muiño in dict1_muiño:
            print(valor)
            print("¿Desea modificarlo?")
            respuesta_muiño = input()
            if respuesta_muiño == "si":
                print("Introduzca el nuevo número")
                numero_muiño = int(input())
                valor = numero_muiño
        else:
            print("Escriba el número correspondiente")
            numero_muiño = int(input())
            dict1_muiño[nombre_muiño] = numero_muiño

    if respuesta_muiño == 2:
        print("Escriba una cadena")
        cadena_muiño = input()
        for clave in dict1_muiño.keys():
            if cadena_muiño in clave:
                print(clave)
            else:
                print("No hay ningun nombre que contenga esa cadena")

    if respuesta_muiño == 3:
        print("Escriba un nombre")
        nombre_muiño = input()
        if nombre_muiño in dict1_muiño:
            print("¿Quiere borrar este contacto?")
            respuesta_muiño = input()
            if respuesta_muiño == "si":
                dict1_muiño.pop(nombre_muiño)

    if respuesta_muiño == 4:
        print("Las nombres y sus numeros son:")

        for clave,valor in dict1_muiño.items():
            print(clave,"->",valor)
    
    if respuesta_muiño == 5:
        break