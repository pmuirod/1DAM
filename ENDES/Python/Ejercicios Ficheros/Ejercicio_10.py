# Pablo Muiño Rodríguez
# Escribe un programa en python que lea el fichero json pedidos.json con datos de ordenes, a continuación deberá crear otro fichero primerapellido_clientes.json 
# con todos los datos de los clientes.

import json

with open ("pedidos.json","r") as fichero_muino:
        datos_muino = json.load(fichero_muino)

for orden in datos_muino["ordenes"]:
        cliente_muino = orden["cliente"]

        with open ("muino_clientes.json","w") as fichero_muino:
                json.dump(cliente_muino, fichero_muino)
