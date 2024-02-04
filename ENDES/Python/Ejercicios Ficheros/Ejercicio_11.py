# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero gazpacho.json con datos su origen e ingredientes, a continuación deberá crear otro fichero primerapellido_ingredientes.json 
# con los todos los datos de sus ingredientes.

import json

with open ("gazpacho.json","r") as fichero_muino:
    datos_muino = json.load(fichero_muino)

for ingrediente in datos_muino["ingredientes"]:
    nombre_muino = ingrediente["nombre"]
    cantidad_muino = ingrediente["cantidad"]

    with open ("muino_ingredientes.json","w") as fichero_muino:
        json.dump(f"Nombre = {nombre_muino}", fichero_muino)
        json.dump(f"Cantidad = {cantidad_muino}", fichero_muino)