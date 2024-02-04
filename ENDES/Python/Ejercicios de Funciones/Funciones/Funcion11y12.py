# Función para leer la fecha dada por teclado

def leerFecha():
    print("Escriba una fecha siguiendo el siguiente orden: año, mes, día")
    año_muino = int(input())
    mes_muino = int(input())
    dia_muino = int(input())

    return año_muino, mes_muino, dia_muino

# Función para comprobar que la fecha dada por teclado es correcta

def validar(año_muino,mes_muino,dia_muino):
    if esBisiesto(año_muino)==True:
        if mes_muino==1 or mes_muino==3 or mes_muino==5 or mes_muino==7 or mes_muino==8 or mes_muino==10 or mes_muino==12:
            if dia_muino<=31:
                return True
            else:
                return False
        else:
            if mes_muino==2:
                if dia_muino<=29:
                    return True
                else:
                    return False
            else:
                if dia_muino<=30:
                    return True
                else:
                    return False
    else:
        if mes_muino==1 or mes_muino==3 or mes_muino==5 or mes_muino==7 or mes_muino==8 or mes_muino==10 or mes_muino==12:
            if dia_muino<=31:
                return True
            else:
                return False
        else:
            if mes_muino==2:
                if dia_muino<=29:
                    return True
                else:
                    return False
            else:
                if dia_muino<=30:
                    return True
                else:
                    return False

# Función para comprobar que el año dado por teclado es bisiesto

def esBisiesto(año):
    if año%4==0:
        return True
    else:
        return False

# Función para saber cuántos días tiene un mes en un año (ambos dados por teclado)

def diasDelMes(mes,año):
    if esBisiesto(año)==True:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            return 31
        else:
            if mes==2:
                return 29
            else:
                return 30
    else:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            return 31
        else:
            if mes==2:
                return 28
            else:
                return 30

# Función para calcular el día juliano de una fecha dada por teclado

def calcular_Dia_Juliano(año_muino,mes_muino,dia_muino):
    suma_muino = int
    suma_muino = 0

    for i in range(1,mes_muino):
        suma_muino += diasDelMes(i,año_muino)
    
    suma_muino+=dia_muino

    print("El dia juliano es",suma_muino)