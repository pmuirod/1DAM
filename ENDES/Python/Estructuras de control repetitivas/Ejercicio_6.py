# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
# Por: Pablo Muiño Rodríguez

print("Esriba dos números")
num1_muiño = int(input())
num2_muiño = int(input())

print("Los números pares entre estos dos números son:")

while num1_muiño<(num2_muiño-1):
    num1_muiño = num1_muiño+1
    if num1_muiño%2==0:
        print(num1_muiño)