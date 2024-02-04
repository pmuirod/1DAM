# Escribir un programa que lea un año indicando si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
# Por: Pablo Muiño Rodríguez

print("Escriba un año")
año = int(input())

if año%100==0 and año%400==0:
    print("Es un año bisiesto")
else:
    if año%4==0:
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")