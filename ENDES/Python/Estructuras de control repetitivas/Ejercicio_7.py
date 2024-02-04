# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
# Por: Pablo Muiño Rodríguez

print("Escriba un número")
num_muiño = int(input())
print("La tabla de multiplicar de dicho número es:")

contador_muiño = 1
producto_muiño = 1

while contador_muiño<=10:
    producto_muiño = num_muiño*contador_muiño
    print(producto_muiño)
    contador_muiño = contador_muiño+1