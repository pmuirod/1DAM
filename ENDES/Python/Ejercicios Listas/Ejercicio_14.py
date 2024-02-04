# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
#   - Las cantidades totales de cada articulo.
#   - La cantidad de artículos en la sucursal 2.
#   - La cantidad del articulo 3 en la sucursal 1.
#   - La recaudación total de cada sucursal.
#   - La recaudación total de la empresa.
#   - La sucursal de mayor recaudación.
# Por: Pablo Muiño Rodríguez

precio_muiño = int
unidades_muiño = int
lista_precio_muiño = []
lista_sucursal1_muiño = []
lista_sucursal2_muiño = []
lista_sucursal3_muiño = []
lista_sucursal4_muiño = []
lista_total_muiño = []
lista_recaudacion_sucursal1_muiño = []
lista_recaudacion_sucursal2_muiño = []
lista_recaudacion_sucursal3_muiño = []
lista_recaudacion_sucursal4_muiño = []
lista_recaudacion_total_muiño = []
suma_articulos2_muiño = int
suma_articulos2_muiño = 0
contador_muiño = int
contador_muiño = 0

for i in range(1,6):
    print("Indique cuánto vale el",i,"artículo:")
    precio_muiño = int(input())
    lista_precio_muiño.append(precio_muiño)

    print("Escriba cuántas unidades se han vendido en las 1 sucursal:")
    unidades_muiño = int(input())
    lista_sucursal1_muiño.append(unidades_muiño)

    print("Escriba cuántas unidades se han vendido en las 2 sucursal:")
    unidades_muiño = int(input())
    lista_sucursal2_muiño.append(unidades_muiño)

    print("Escriba cuántas unidades se han vendido en las 3 sucursal:")
    unidades_muiño = int(input())
    lista_sucursal3_muiño.append(unidades_muiño)

    print("Escriba cuántas unidades se han vendido en las 4 sucursal:")
    unidades_muiño = int(input())
    lista_sucursal4_muiño.append(unidades_muiño)

    lista_total_muiño.append(lista_sucursal1_muiño[contador_muiño]+lista_sucursal2_muiño[contador_muiño]+lista_sucursal3_muiño[contador_muiño]+lista_sucursal4_muiño[contador_muiño])
    suma_articulos2_muiño = suma_articulos2_muiño+(lista_sucursal2_muiño[contador_muiño])
    lista_recaudacion_sucursal1_muiño.append((lista_precio_muiño[contador_muiño])*(lista_sucursal1_muiño[contador_muiño]))
    lista_recaudacion_sucursal2_muiño.append((lista_precio_muiño[contador_muiño])*(lista_sucursal2_muiño[contador_muiño]))
    lista_recaudacion_sucursal3_muiño.append((lista_precio_muiño[contador_muiño])*(lista_sucursal3_muiño[contador_muiño]))
    lista_recaudacion_sucursal4_muiño.append((lista_precio_muiño[contador_muiño])*(lista_sucursal4_muiño[contador_muiño]))
    lista_recaudacion_total_muiño.append(lista_recaudacion_sucursal1_muiño[contador_muiño]+lista_recaudacion_sucursal2_muiño[contador_muiño]+lista_recaudacion_sucursal3_muiño[contador_muiño]+lista_recaudacion_sucursal4_muiño[contador_muiño])

    contador_muiño = contador_muiño+1

print("La cantidad total de cada artículo es:")
print(lista_total_muiño)
print("La cantidad de artículos en la sucursal 2 son:")
print(suma_articulos2_muiño)
print("La cantidad del artículo 3 en la sucursal 1 es:")
print(lista_sucursal1_muiño[2])
print("La recaudación total (euros) de cada sucursal son respectivamente (1-4):")
print(lista_recaudacion_sucursal1_muiño)
print(lista_recaudacion_sucursal2_muiño)
print(lista_recaudacion_sucursal3_muiño)
print(lista_recaudacion_sucursal4_muiño)
print("La recaudación total de la empresa es (euros):")
print(lista_recaudacion_total_muiño)