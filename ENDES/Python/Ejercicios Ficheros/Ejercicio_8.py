# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero json colores.json con datos de colores, deberá mostrar en la terminal todos los nombres de colores, 
# sus códigos rgba y hexadecimal respectivamente.

import json

with open ("colores.json","r") as fichero_muino:
        datos_muino = json.load(fichero_muino)

for color in datos_muino["colors"]:
        nombre_muino = color["color"]
        rgba_muino = color["code"]["rgba"]
        hexadecimal_muino = color["code"]["hex"]
        
        print(f"Nombre del color = {nombre_muino}")
        print(f"RGBA = {rgba_muino}")
        print(f"Hexadecimal = {hexadecimal_muino}")
        print("")