# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
# Por: Pablo Muiño Rodríguez

print("A continuación se va a tener que escribir una serie de números, ¿cuántos desea introducir?")
cantidad_muiño = int(input())
print("Escriba la serie de números")

mayor_muiño = 0
igual_muiño = 0
menor_muiño = 0

while cantidad_muiño!=0:
    num_muiño = int(input())
    if num_muiño>0:
        mayor_muiño = mayor_muiño+1
    else:
        if num_muiño==0:
            igual_muiño = igual_muiño+1
        else:
            menor_muiño = menor_muiño+1
    
    cantidad_muiño = cantidad_muiño-1

print("Hay",mayor_muiño,"números mayores que 0")
print("Hay",igual_muiño,"números iguales a 0")
print("Hay",menor_muiño,"números menores que 0")