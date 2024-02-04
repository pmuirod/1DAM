# Vamos a crear las siguientes funciones para trabajar con funciones:
#   - Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
#   - Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
#   - Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
#   - Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
#   - Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
#   - Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
#   - Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
#   - Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.

# Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
#   1. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
#   2. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
#   3. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
#   4. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
#   5. Salir

from Funciones.Funcion13 import leerFraccion, calcularMCD, simplificarFraccion, escribirFraccion, sumarFracciones, restarFracciones, multiplicarFracciones, dividirFracciones

print("")
print("1. Sumar dos fracciones")
print("2. Restar dos fracciones")
print("3. Multiplicar dos fracciones")
print("4. Dividir dos fracciones")
print("5. Salir")
respuesta_muino = int(input())

while respuesta_muino <= 5:
    if respuesta_muino == 1:
        numerador1_muino, denominador1_muino = leerFraccion()
        print("")
        numerador2_muino, denominador2_muino = leerFraccion()

        numerador_muino, denominador_muino = sumarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino)
        MCD_muino = calcularMCD(numerador_muino,denominador_muino)
        numerador_muino, denominador_muino = simplificarFraccion(numerador_muino,denominador_muino,MCD_muino)
        print("La suma de",numerador1_muino,"/",denominador1_muino,"y",numerador2_muino,"/",denominador2_muino,"es:")
        escribirFraccion(numerador_muino,denominador_muino)

        numerador1_muino = 0
        numerador2_muino = 0
        denominador1_muino = 0
        denominador2_muino = 0
    
    if respuesta_muino == 2:
        numerador1_muino, denominador1_muino = leerFraccion()
        print("")
        numerador2_muino, denominador2_muino = leerFraccion()

        numerador_muino, denominador_muino = sumarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino)
        MCD_muino = calcularMCD(numerador_muino,denominador_muino)
        numerador_muino, denominador_muino = simplificarFraccion(numerador_muino,denominador_muino,MCD_muino)
        print("La resta de",numerador1_muino,"/",denominador1_muino,"y",numerador2_muino,"/",denominador2_muino,"es:")
        escribirFraccion(numerador_muino,denominador_muino)

        numerador1_muino = 0
        numerador2_muino = 0
        denominador1_muino = 0
        denominador2_muino = 0
    
    if respuesta_muino == 3:
        numerador1_muino, denominador1_muino = leerFraccion()
        print("")
        numerador2_muino, denominador2_muino = leerFraccion()

        numerador_muino, denominador_muino = sumarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino)
        MCD_muino = calcularMCD(numerador_muino,denominador_muino)
        numerador_muino, denominador_muino = simplificarFraccion(numerador_muino,denominador_muino,MCD_muino)
        print("La multiplicación de",numerador1_muino,"/",denominador1_muino,"y",numerador2_muino,"/",denominador2_muino,"es:")
        escribirFraccion(numerador_muino,denominador_muino)

        numerador1_muino = 0
        numerador2_muino = 0
        denominador1_muino = 0
        denominador2_muino = 0
    
    if respuesta_muino == 4:
        numerador1_muino, denominador1_muino = leerFraccion()
        print("")
        numerador2_muino, denominador2_muino = leerFraccion()

        numerador_muino, denominador_muino = sumarFracciones(numerador1_muino,denominador1_muino,numerador2_muino,denominador2_muino)
        MCD_muino = calcularMCD(numerador_muino,denominador_muino)
        numerador_muino, denominador_muino = simplificarFraccion(numerador_muino,denominador_muino,MCD_muino)
        print("La división de",numerador1_muino,"/",denominador1_muino,"y",numerador2_muino,"/",denominador2_muino,"es:")
        escribirFraccion(numerador_muino,denominador_muino)

        numerador1_muino = 0
        numerador2_muino = 0
        denominador1_muino = 0
        denominador2_muino = 0
    
    if respuesta_muino == 5:
        print("____¡Hasta luego!____")
        break

    print("")
    print("1. Sumar dos fracciones")
    print("2. Restar dos fracciones")
    print("3. Multiplicar dos fracciones")
    print("4. Dividir dos fracciones")
    print("5. Salir")
    respuesta_muino = int(input())