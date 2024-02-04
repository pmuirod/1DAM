# Pablo Muiño Rodríguez
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre primer apellido-n.txt la tabla de multiplicar de ese número, 
# donde n es el número introducido.

print("Escriba un número entero del 1 al 10:")
num_muino = int(input())

nombre_muino = "muino-" + str(num_muino) + ".txt"

fichero_muiño = open(nombre_muino,"w")

for i in range(1,11):
    print(num_muino,"x",i,"=",num_muino*i, file= fichero_muiño)

fichero_muiño.close()