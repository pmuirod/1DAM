# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#   - El exponente sea positivo, sólo tienes que imprimir la potencia.
#   - El exponente sea 0, el resultado es 1.
#   - El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
# Por: Pablo Muiño Rodríguez

print("Escriba una base y un exponente para calcular su potencia")
base = int(input())
exponente = int(input())

if exponente>=0:
    if exponente==0:
        print("El resultado es 1")
    else:
        print("El resultado es",base**exponente)
else:
    exponente = exponente*-1
    print("El resultado es",1/(base**exponente))