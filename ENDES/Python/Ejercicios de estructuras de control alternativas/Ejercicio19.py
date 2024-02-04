# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
# Por: Pablo Muiño Rodríguez

print("Escriba un número de mes (1-12)")
mes = int(input())

if mes==2:
    print("Hay 28 días")
else:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print("Hay 31 días")
    else:
        if mes==4 or mes==6 or mes==9 or mes==11:
            print("Hay 30 días")
        else:
            print("Se han introducido mal los datos")