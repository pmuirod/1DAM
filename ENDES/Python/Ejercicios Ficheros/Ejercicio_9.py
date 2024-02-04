# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero json pedidos.json con datos de órdenes, deberá mostrar en la terminal todos las órdenes de pedidos que no se hayan entregado.

import json

with open ("pedidos.json","r") as fichero_muino:
        datos_muino = json.load(fichero_muino)

for orden in datos_muino["ordenes"]:
        tamaño_muino = orden["tamano"]
        precio_muino = orden["precio"]
        toppings_muino = orden["toppings"]
        queso_muino = orden["queso_extra"]
        delivery_muino = orden["delivery"]
        cliente_muino = orden["cliente"]

        if delivery_muino==False:
            print(f"Tamaño = {tamaño_muino}")
            print(f"Precio = {precio_muino}")
            print(f"Toppings = {toppings_muino}")
            print(f"Queso extra = {queso_muino}")
            print(f"Entregado = {delivery_muino}")
            print(f"Cliente = {cliente_muino}")