# Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a
# dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
# Por: Pablo Muiño Rodríguez

print("Escriba su nota")
nota = int(input())
print("Escriba su edad")
edad = int(input())
print("Escriba su sexo (M o F)")
sexo = input()

if (nota>=5 and edad>=18 and sexo=="F"):
    print("ACEPTADA")
else:
    if (nota>=5 and edad>=18 and sexo=="M"):
        print("POSIBLE")
    else:
        print("NO ACEPTADA")