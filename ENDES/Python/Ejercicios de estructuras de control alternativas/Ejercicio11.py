# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#   - Si se cumple Pitágoras entonces es triángulo rectángulo
#   - Si sólo dos lados del triángulo son iguales entonces es isósceles.
#   - Si los 3 lados son iguales entonces es equilátero.
#   - Si no se cumple ninguna de las condiciones anteriores, es escaleno.
# Por: Pablo Muiño Rodríguez

print("Escriba los 3 lados de un triángulo")
A = float(input())
B = float(input())
C = float(input())

if ((A*A)+(B*B)==(C*C)):
    print("Es un triángulo rectángulo")
else:
    if A==B and B==C:
        print("Es un triángulo equilátero")
    else:
        if A==B or B==C or C==A:
            print("Es un triángulo isósceles")
        else:
            print("Es un triángulo escaleno")