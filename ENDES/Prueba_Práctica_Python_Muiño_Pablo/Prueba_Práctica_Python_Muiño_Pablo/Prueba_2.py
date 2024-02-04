# Pablo Muiño Rodríguez
# Codifica un programa en python que nos permita guardar la temperatura mínima y máxima de los últimos 7 días la semana. Dicha información deberá ser guardada en un diccionario.
# El programa pedirá al usuario las temperaturas de todos los días . Al final el programa nos mostrará:
#   -La lista de todos los días de la semana con su temperatura mínima y máxima con el siguiente formato:
#       El día_de_la-semana ha tenido las siguientes temperaturas mínimas y máximas: ('mímima', 'máxima') 
#   -Deberá mostrar también la temperatura media mínima y la temperatura media máxima de los últimos 7 días redondeada a dos cifras decimales.

dias_pablo = {}
temperaturas_pablo = []
suma_minima_pablo = int
suma_minima_pablo = 0
suma_maxima_pablo = int
suma_maxima_pablo = 0

for i in range(0,7):        # Bucle para introducir los días de la semana así como su temperatura mínima y máxima correspondiente
    print("Escriba el dia de la semana: ",end="")
    dia_pablo = input()
    print("Ahora indique la temperatura mínima y máxima de este día (en ese orden):")
    temperatura_minima_pablo = int(input())
    suma_minima_pablo = suma_minima_pablo+temperatura_minima_pablo      # Acumulo los valores mínimos en una variable para después realizar la media
    temperatura_maxima_pablo = int(input())
    suma_maxima_pablo = suma_maxima_pablo+temperatura_maxima_pablo      # Acumulo los valores máximos en una variable para después realizar la media
    temperaturas_pablo.append(temperatura_minima_pablo)     # Añado la temperatura mínima de ese día a su lista correspondiente
    temperaturas_pablo.append(temperatura_maxima_pablo)     # Añado la temperatura máxima de ese día a su lista correspondiente

    dias_pablo[dia_pablo] = temperaturas_pablo      # Aadjunto la lista con las temperaturas (valor) al día al que pertenecen (clave) en el diccionario

    temperaturas_pablo = []     # Reinicio la lista puesto que en la siguiente iteración las temperaturas serán diferentes ya que serán las de otro día

for clave,valor in dias_pablo.items():      # Escribo tanto las claves como los valores del diccionario
    print("El",clave,"ha tenido las siguientes temperaturas mínimas y máximas:",valor)
print("")
print("La temperatura media mínima de los últimos 7 días es:",suma_minima_pablo/7)      # Escribo la media de las temperaturas mínimas a lo largo de la semana
print("La temperatura media máxima de los últimos 7 días es:",suma_maxima_pablo/7)      # Escribo la media de las temperaturas máximas a lo largo de la semana