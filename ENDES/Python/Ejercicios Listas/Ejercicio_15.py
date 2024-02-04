# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
#   - Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
#   - Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado 
#     en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# Por: Pablo Muiño Rodríguez

lista_equipos_muiño = []
lista_goles_muiño = []
contador_muiño = int
contador_muiño = 0

for i in range(1,16):
    print("Escriba el nombre del primer equipo del",i,"partido")
    equipos_muiño = input()
    lista_equipos_muiño.append(equipos_muiño)
    print("Escriba el nombre del segundo equipo del",i,"partido")
    equipos_muiño = input()
    lista_equipos_muiño.append(equipos_muiño)
    print("Escriba el resultado del partido (goles del primer equipo y a continuación goles del segundo equipo)")
    goles_muiño = input()
    lista_goles_muiño.append(goles_muiño)
    goles_muiño = input()
    lista_goles_muiño.append(goles_muiño)

print("La quiniela de esta jornada es:")

while contador_muiño<=29:
    print(lista_equipos_muiño[contador_muiño],":",lista_goles_muiño[contador_muiño])
    print(lista_equipos_muiño[contador_muiño+1],":",lista_goles_muiño[contador_muiño+1])
    print("--------------")
    contador_muiño = contador_muiño+2