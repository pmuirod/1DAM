# Pablo Muiño Rodríguez
# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, 
# vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

from Funciones.Funcion3 import mediaTemperatura

dias_muino = int(input("Escriba el número de días a introducir: "))

for i in range(0,dias_muino):
    temp_maxima = int(input("Escriba la temperatura máxima de este día: "))
    temp_minima = int(input("Escriba la temperatura minima de este día: "))
    mediaTemperatura(temp_maxima,temp_minima)