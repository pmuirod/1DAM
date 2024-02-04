# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería y muestre en la terminal cuántos libros hay en la librería.

import json
contador_muino = int
contador_muino = 0

with open ("libreria.json","r") as fichero_muino:
    datos_muino = json.load(fichero_muino)

for libro in datos_muino:
    contador_muino = contador_muino+1

print("Hay",contador_muino,"libros")