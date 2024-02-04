# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y 
# tienen la misma velocidad. Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.
# Por: Pablo Muiño Rodríguez

print("Escriba la velocidad de los dos coches")
velocidad_muiño = int(input())

tiempo_muiño = ((150-70)/(velocidad_muiño+velocidad_muiño))
distancia_muiño = velocidad_muiño*tiempo_muiño

print("El km donde se encontrarán es en el",int(distancia_muiño))