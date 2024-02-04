# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
# - La suma de los números que están dentro del intervalo (intervalo abierto).
# - Cuantos números están fuera del intervalo.
# - He informa si hemos introducido algún número igual a los límites del intervalo.
# Por: Pablo Muiño Rodríguez

print("Escriba el límite inferior y el superior de un intervalo")
inferior_muiño = int(input())
superior_muiño = int(input())

while inferior_muiño>superior_muiño:
    print("Escriba el límite inferior y el superior de un intervalo")
    inferior_muiño = int(input())
    superior_muiño = int(input())

print("Escriba una serie de números (se acaba al poner un 0)")
num_muiño = int(input())

suma_muiño = 0
fuera_muiño = 0
igual_muiño = False
contador_muiño = 0

while num_muiño!=0:
    if (num_muiño>=inferior_muiño) and (num_muiño<=superior_muiño):
        suma_muiño = suma_muiño + num_muiño
        if (num_muiño==inferior_muiño) or (num_muiño==superior_muiño):
            igual_muiño = True
            contador_muiño = contador_muiño+1
    else:
        fuera_muiño = fuera_muiño+1
    num_muiño = int(input())

print("La suma de los números dentro del intervalo es",suma_muiño)
if fuera_muiño!=0:
    print("Hay",fuera_muiño,"números fuera de los intervalos")
if igual_muiño==True:
    print("Hay",contador_muiño,"números iguales a los límites del intervalo")