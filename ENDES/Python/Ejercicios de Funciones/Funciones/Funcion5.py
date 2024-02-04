# Pablo Muiño Rodríguez
# Módulo para calcular el máximo y el mínimo de una lista de números

def calcularMaxMin(lista1,longitud):
    mayor = int
    mayor = 0
    menor = int
    menor = 1000000

    for i in range(1,longitud):
        if lista1[i]>mayor:
            mayor = lista1[i]
        if lista1[i]<menor:
            menor = lista1[i]
    
    print("El mayor es",mayor)
    print("El menor es",menor)