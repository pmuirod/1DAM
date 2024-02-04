# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
# Por: Pablo Muiño Rodríguez

print("Escriba una fecha (dia, mes y año)")
dia = int(input())
mes = int(input())
año = int(input())

if mes<1 or dia<1:
    print("Se ha introducido una fecha errónea")
else:
    if año%4==0:
        if mes==2 and dia>29:
            print("Se ha introducido una fecha errónea")
        else:
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>31:
                print("Se ha introducido una fecha errónea")
            else:
                if mes==4 or mes==6 or mes==9 or mes==11 and dia>30:
                    print("Se ha introducido una fecha errónea")
                else:
                    print("La fecha es correcta")
    else:
        if mes==2 and dia>28:
            print("Se ha introducido una fecha errónea")
        else:
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>31:
                print("Se ha introducido una fecha errónea")
            else:
                if mes==4 or mes==6 or mes==9 or mes==11 and dia>30:
                    print("Se ha introducido una fecha errónea")
                else:
                    print("La fecha es correcta")