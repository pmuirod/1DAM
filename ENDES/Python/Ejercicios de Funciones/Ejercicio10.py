# Escribir dos funciones que permitan calcular:
#   - La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#   - La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas, minutos y segundos o salir del programa.

from Funciones.Funcion10 import calcularSegundos, calcularHorasMinutosSegundos

print("1. Convertir a segundos")
print("2. Convertir a hora, minuots y segundos")
print("3. Salir del programa")
respuesta_muino = int(input())

while respuesta_muino <= 3:
    if respuesta_muino == 1:
        print("Escriba las horas")
        horas_muino = int(input())
        print("Escriba los minutos")
        minutos_muino = int(input())
        print("Escriba los segundos")
        segundos_muino = int(input())

        calcularSegundos(horas_muino,minutos_muino,segundos_muino)

    if respuesta_muino == 2:
        print("Escriba los segundos")
        segundos_muino = int(input())

        calcularHorasMinutosSegundos(segundos_muino)

    if respuesta_muino == 3:
        print("____¡Hasta luego!____")
        break

    print("1. Convertir a segundos")
    print("2. Convertir a hora, minuots y segundos")
    print("3. Salir del programa")
    respuesta_muino = int(input())
