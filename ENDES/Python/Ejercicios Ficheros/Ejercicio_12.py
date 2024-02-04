# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero movies.json con datos de películas. A continuación deberá crear un fichero primerapellido_pelicula1994.json 
# con los títulos de las películas que se hayan estrenado en 1994.

import json

with open ("movies.json","r") as fichero_muino:
    datos_muino = json.load(fichero_muino)

for pelicula in datos_muino:
    nombre_muino = pelicula["title"]
    año_muino = pelicula["year"]
    genero_muino = pelicula["genres"]
    calificacion_muino = pelicula["ratings"]
    duracion_muino = pelicula["duration"]
    fecha_salida_muino = pelicula["releaseDate"]
    titulo_original_muino = pelicula["originalTitle"]
    sinopsis_muino = pelicula["storyline"]
    actores_muino = pelicula["actors"]
    url_poster_muino = pelicula["posterurl"]

    if año_muino==1994:
        with open ("muino_pelicula1994.json","w") as fichero_muino:
            json.dump(f"Nombre = {nombre_muino}", fichero_muino)
            json.dump(f"Año = {año_muino}", fichero_muino)
            json.dump(f"Genero = {genero_muino}", fichero_muino)
            json.dump(f"Calificación = {calificacion_muino}", fichero_muino)
            json.dump(f"Duración = {duracion_muino}", fichero_muino)
            json.dump(f"Fecha de salida = {fecha_salida_muino}", fichero_muino)
            json.dump(f"Título original = {titulo_original_muino}", fichero_muino)
            json.dump(f"Sinopsis = {sinopsis_muino}", fichero_muino)
            json.dump(f"Actores = {actores_muino}", fichero_muino)
            json.dump(f"Url del poster = {url_poster_muino}", fichero_muino)