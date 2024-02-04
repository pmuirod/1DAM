# Por: Pablo Muiño Rodríguez
# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, 
# y los valores sean los cuadrados de las claves.

dict1_muiño = {}
N_muiño = int
contador_muiño = int
contador_muiño = 1

print("Escriba un número")
N_muiño = int(input())

while contador_muiño != N_muiño+1:
    dict1_muiño[contador_muiño] = contador_muiño*contador_muiño
    contador_muiño = contador_muiño+1

print("Las claves y sus valores son:")

for clave,valor in dict1_muiño.items():
    print(clave,"->",valor)