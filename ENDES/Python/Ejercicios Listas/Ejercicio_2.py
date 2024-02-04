# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
contador_muiño = int

print("Escriba cinco cadenas de carácteres")

for i in range(0,5):
    cadena_muiño = input()
    lista1_muiño.append(cadena_muiño)

lista1_muiño.reverse()

print(lista1_muiño)