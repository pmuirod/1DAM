# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería, recibe por teclado un límite inferior y superior para el 
# precio y muestre en la terminal todos los libros cuyo precio esta en ese intervalo.

import json

print("Escriba un límite inferor de precio")
inferior_muino = int(input())
print("Escriba un límite superior de precio")
superior_muino = int(input())

with open ("libreria.json","r") as fichero_muino:
    datos_muino = json.load(fichero_muino)

for libro in datos_muino["book"]:
    nombre_muino = libro["title"]
    autor_muino = libro["author"]
    ano_muino = libro["year"]
    precio_muino = libro["price"]
    categoria_muino = libro["_category"]

    if (inferior_muino<precio_muino) & (superior_muino>precio_muino):
        with open ("muino_pelicula1994.json","w") as fichero_muino:
            json.dump(f"Nombre = {nombre_muino}", fichero_muino)
            json.dump(f"Autor = {autor_muino}", fichero_muino)
            json.dump(f"Año = {ano_muino}", fichero_muino)
            json.dump(f"Precio = {precio_muino}", fichero_muino)
            json.dump(f"Categoría = {categoria_muino}", fichero_muino)