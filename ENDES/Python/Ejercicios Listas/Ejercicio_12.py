# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, 
# mientras que el resto de los elementos contendrán el valor 0.
#  111111111111111
#  100000000000001
#  100000000000001
#  100000000000001
#  111111111111111
# Visualiza el contenido de la matriz en pantalla.
# Por: Pablo Muiño Rodríguez

lista1_muiño = []
lista2_muiño = []
valor_muiño = int

for i in range(1,6):
    if i==1 or i==5:
        for i in range(1,16):
            valor_muiño = 1
            lista1_muiño.append(valor_muiño)
        print(lista1_muiño)
        lista1_muiño = []
    else:
        for i in range(1,16):
            if i==1 or i==15:
                valor_muiño = 1
                lista2_muiño.append(valor_muiño)
            else:
                valor_muiño = 0
                lista2_muiño.append(valor_muiño)
        print(lista2_muiño)
        lista2_muiño = []