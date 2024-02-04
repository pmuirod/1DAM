# Por: Pablo Muiño Rodríguez
# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

dict1_muiño = {}
dict1_muiño["manzana"] = 1.22
dict1_muiño["pera"] = 1.14
dict1_muiño["naranja"] = 1.36
dict1_muiño["ciruela"] = 0.98
dict1_muiño["banana"] = 1.11
contador_muiño = int
contador_muiño = 0
contador2_muiño = int
contador2_muiño = 0
precio_muiño = int
precio_muiño = 0

print("Escriba una fruta")
fruta_muiño = input()
print("Indique la cantidad que se ha vendido")
cantidad_muiño = int(input())

if fruta_muiño in dict1_muiño:
    for clave in dict1_muiño.keys():
        contador_muiño = contador_muiño+1
        if clave == fruta_muiño:
            break
    for valor in dict1_muiño.values():
        contador2_muiño = contador2_muiño+1
        if contador2_muiño == contador_muiño:
            precio_muiño = valor
    print("El precio final de la fruta es de",precio_muiño*cantidad_muiño,"euros")
else:
    print("La fruta que se ha indicado no existe")