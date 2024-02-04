# Algoritmo que pida un número y diga si es positivo, negativo o 0.
# Por: Pablo Muiño Rodríguez

print("Escriba un número")
num = int(input())

if num>0:
    print ("El número es positivo")
else:
    if num<0:
        print ("El número es negativo")
    else:
        print ("El número es 0")