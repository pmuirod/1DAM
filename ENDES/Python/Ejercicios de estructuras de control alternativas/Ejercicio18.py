# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
# Por: Pablo Muiño Rodríguez

print("Escriba el dia de la semana (1-7)")
dia = int(input())

if dia>=1 and dia<=7:
    if dia==1:
        print("Hoy el Lunes")
    else:
        if dia==2:
            print("Hoy es Martes")
        else:
            if dia==3:
                print("Hoy es Miércoles")
            else:
                if dia==4:
                    print("Hoy es Jueves")
                else:
                    if dia==5:
                        print("Hoy es Viernes")
                    else:
                        if dia==6:
                            print("Hoy es Sabado")
                        else:
                            print("Hoy es Domingo")
else:
    print("Se han introducido mal los datos")