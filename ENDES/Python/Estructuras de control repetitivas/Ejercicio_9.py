# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), 
# saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
# Por: Pablo Muiño Rodríguez

print("Escriba dos números para hacer su potencia")
base_muiño = float(input())
exponente_muiño = int(input())

potencia_muiño = base_muiño

if exponente_muiño<0:
    print("Se han introducido mal los datos")
else:
    while exponente_muiño!=1:
        potencia_muiño = potencia_muiño*base_muiño
        exponente_muiño = exponente_muiño-1

print("La potencia de los dos números anteriores es:",int(potencia_muiño))