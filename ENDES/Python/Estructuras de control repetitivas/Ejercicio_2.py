# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y 
# va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.
# Por: Pablo Muiño Rodríguez

import random
contador = 0

aleatorio_muiño = random.randint(1,100)

while contador!=11:
    contador = contador+1
    print("Escriba un número a adivinar (1-100)")
    num_muiño = int(input())
    
    if num_muiño>aleatorio_muiño:
        print("El número es menor")
    else:
        if num_muiño<aleatorio_muiño:
            print("El número es mayor")
        else:
            if num_muiño==aleatorio_muiño:
                print("¡Felicidades, has acertado!")
                print("Lo has conseguido en",contador,"intentos")
                break
if contador==11:
    print("Se han agotado los intentos")