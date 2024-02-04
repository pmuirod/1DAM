# Pablo Muiño Rodríguez
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número, y muestre 
# por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

contador_muino = int
contador_muino = 1


print("Escriba un número (1-10)")
num_muino = int(input())
print("Escriba otro número (1-10)")
m_muino = int(input())
print("")

nombre_muino = "muiño-" + str(num_muino) + ".txt"

fichero_muino = open(nombre_muino,"r")

for i in fichero_muino:
    if contador_muino == m_muino:
        print(i)
    contador_muino = contador_muino+1

fichero_muino.close()