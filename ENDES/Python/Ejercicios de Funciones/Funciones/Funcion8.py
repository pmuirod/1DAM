# Funcion para realizar el factorial de un número

def factorial(num_muino):
    if num_muino==0:
        return 1
    else:
        return num_muino*factorial(num_muino-1)