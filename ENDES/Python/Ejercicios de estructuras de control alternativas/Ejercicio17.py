# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en 
# letras (dato cadena) de la cara opuesta al resultado obtenido.
# - Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# - Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
# Por: Pablo Muiño Rodríguez

print("Escriba el resultado al haber tirado el dado")
cara = int(input())

if cara>=1 and cara<=6:
    if cara==1:
        opuesta = "Seis"
        print("La cara opuesta es",opuesta)
    else:
        if cara==2:
            opuesta = "Cinco"
            print("La cara opuesta es",opuesta)
        else:
            if cara==3:
                opuesta = "Cuatro"
                print("La cara opuesta es",opuesta)
            else:
                if cara==4:
                    opuesta = "Tres"
                    print("La cara opuesta es",opuesta)
                else:
                    if cara==5:
                        opuesta = "Dos"
                        print("La cara opuesta es",opuesta)
                    else:
                        opuesta = "Uno"
                        print("La cara opuesta es",opuesta)
else:
    print("ERROR: número incorrecto")