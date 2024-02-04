# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
#   - Nombre: Lista para guardar los nombres de los conductores.
#   - kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
# Por: Pablo Muiño Rodríguez

lista_nombre_muiño = []
lista_kms_muiño = []
lista_total_kms = []
contador_muiño = int
contador_muiño = 0

print("Escriba el nomrbe del conductor(* para salir)")
nombre_muiño = input()
print("Indique cuántos km hace al dia")
km_muiño = int(input())

while nombre_muiño!="*":
    lista_nombre_muiño.append(nombre_muiño)
    lista_kms_muiño.append(km_muiño)
    lista_total_kms.append(lista_kms_muiño[contador_muiño]*7)

    contador_muiño = contador_muiño+1

    print("Escriba el nomrbe del conductor(* para salir)")
    nombre_muiño = input()
    if nombre_muiño=="*":
        break
    print("Indique cuántos km hace al dia")
    km_muiño = int(input())

print("Los nombres y sus kms semanales son respectivamente:")
print(lista_nombre_muiño)
print(lista_total_kms)