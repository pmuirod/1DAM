# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos

print("Escriba el valor del primer punto")
x1 = int (input())
y1 = int (input())

print("Escriba el valor del degundo punto")
x2 = int (input())
y2 = int (input())

import math

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("La distancia entre los dos puntos es de",distancia)