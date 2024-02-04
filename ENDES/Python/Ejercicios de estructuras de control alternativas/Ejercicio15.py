# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes
# por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, 
# de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
# Por: Pablo Muiño Rodríguez

print("Especifique cuántos alumnos van a ir a el viaje")
alumnos = int(input())

if alumnos<30:
    costo = 4000/alumnos
    precio = (costo*alumnos)
    print("Los alumnos tendrán que pagar",costo,"€, sumando un total de",precio,"que se deberá pagar a la empresa de viajes")
else:
    if alumnos>=30 and alumnos<=49:
        costo = 95
        precio = (costo*alumnos)
        print("Los alumnos tendrán que pagar",costo,"€, sumando un total de",precio,"que se deberá pagar a la empresa de viajes")
    else:
        if alumnos>=50 and alumnos<=99:
            costo = 70
            precio = (costo*alumnos)
            print("Los alumnos tendrán que pagar",costo,"€, sumando un total de",precio,"que se deberá pagar a la empresa de viajes")
        else:
            if alumnos>=100:
                costo = 65
                precio = (costo*alumnos)
                print("Los alumnos tendrán que pagar",costo,"€, sumando un total de",precio,"que se deberá pagar a la empresa de viajes")
            else:
                print("Se han introducido mal los datos")