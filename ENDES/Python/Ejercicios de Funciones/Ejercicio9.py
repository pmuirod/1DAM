# Crear una función que calcule el MCD de dos números por el método de Euclides. El método de Euclides es el siguiente:
#   - Se divide el número mayor entre el menor.
#   - Si la división es exacta, el divisor es el MCD.
#   - Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Crea un programa principal que lea dos números enteros y muestre el MCD.

from Funciones.Funcion9 import calcularMCD
num1_muino = int
num2_muino = int

print("Escriba dos números")
num1_muino = int(input())
num2_muino = int(input())

print("El MCD de",num1_muino,"y",num2_muino,"es",calcularMCD(num1_muino,num2_muino))