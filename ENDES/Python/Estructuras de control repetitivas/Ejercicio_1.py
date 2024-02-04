# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y 
# el propio número y se representa por el número seguido de un signo de exclamación.
# Por: Pablo Muiño Rodríguez

print("Escriba un número")
num_muiño = int(input())

contadorFactorial_muiño = int
factorial_muiño = int

if num_muiño==0 or num_muiño==1:
    factorial_muiño = 1
    print("Su factorial es",factorial_muiño)
else:
    factorial_muiño = num_muiño
    contadorFactorial_muiño = 1
    while contadorFactorial_muiño!=num_muiño:
        factorial_muiño=factorial_muiño*(num_muiño-contadorFactorial_muiño)
        contadorFactorial_muiño=contadorFactorial_muiño+1
    print("Su factorial es",factorial_muiño)