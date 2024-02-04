# Función para leer la fracción

def leerFraccion():
    print("Escriba el numerador")
    numerador_muino = int(input())
    print("Escriba el denominador")
    denominador_muino = int(input())

    return numerador_muino, denominador_muino

# Función para calcular el MCD de dos números introducidos por teclado

def calcularMCD(numerador_muino,denominador_muino):
    print(numerador_muino, denominador_muino)

    if numerador_muino%denominador_muino == 0:
        return denominador_muino
    else:
        denominador_muino = numerador_muino%denominador_muino
        return calcularMCD(numerador_muino,denominador_muino)

# Función para simplificar la fracción

def simplificarFraccion(numerador_muino,denominador_muino,MCD_muino):
    print(MCD_muino)

    numerador_muino = (int)(numerador_muino/MCD_muino)
    denominador_muino = (int)(denominador_muino/MCD_muino)

    return numerador_muino, denominador_muino

# Función para escribir la fracción

def escribirFraccion(numerador_muino,denominador_muino):
    if denominador_muino!=1:
        print(numerador_muino,"/",denominador_muino)
    else:
        print(numerador_muino)

# Función para sumar dos fracciones

def sumarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino):
    numerador_muino = (numerador1_muino*denominador2_muino)+(numerador2_muino*denominador1_muino)
    denominador_muino = (denominador1_muino*denominador2_muino)

    return numerador_muino, denominador_muino

# Función para restar dos fracciones

def restarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino):
    numerador_muino = (numerador1_muino*denominador2_muino)-(numerador2_muino*denominador2_muino)
    denominador_muino = (denominador1_muino*denominador2_muino)
    return numerador_muino, denominador_muino

# Función para multiplicar dos fracciones

def multiplicarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino):
    numerador_muino = numerador1_muino*numerador2_muino
    denominador_muino = denominador1_muino*denominador2_muino
    return numerador_muino, denominador_muino

# Función para dividir dos fracciones

def dividirFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino):
    numerador_muino = (int)(numerador1_muino*denominador2_muino)
    denominador_muino = (int)(denominador1_muino*numerador2_muino)
    return numerador_muino, denominador_muino