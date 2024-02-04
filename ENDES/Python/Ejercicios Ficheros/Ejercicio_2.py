# Pablo Muiño Rodríguez
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

print("Escriba un número (1-10)")
n_muino = int(input())

nombre_muino = "muiño-" + str(n_muino) + ".txt"

fichero_muino = open(nombre_muino,"r")

for i in fichero_muino:
    print(i)

fichero_muino.close()