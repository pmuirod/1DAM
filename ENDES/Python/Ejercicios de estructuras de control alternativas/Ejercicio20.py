# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

# Zona	Ubicación	        Costo/gramo
# 1	    América del Norte	24.00 euros
# 2	    América Central	    20.00 euros
# 3	    América del Sur	    21.00 euros
# 4	    Europa	            10.00 euros
# 5	    Asia	            18.00 euros

# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
# Por: Pablo Muiño Rodríguez

print("Indique el peso del paquete (kilos)")
peso = float(input())

if peso>5:
    print("No se puede transportar")
else:
    print("Indique hacia donde se dirige el paquete (1-5)")
    zona = int(input())

    if zona == 1:
        destino = "América del Norte"
        costo = 24*(peso*1000)
        costo = int(costo)
        print("El paquete con destino a",destino,"vale",costo,"euros")
    else:
        if zona == 2:
            destino = "América Central"
            costo = 20*(peso*1000)
            costo = int(costo)
            print("El paquete con destino a",destino,"vale",costo,"euros")
        else:
            if zona == 3:
                destino = "América del Sur"
                costo = 21*(peso*1000)
                costo = int(costo)
                print("El paquete con destino a",destino,"vale",costo,"euros")
            else:
                if zona == 4:
                    destino = "Europa"
                    costo = 10*(peso*1000)
                    costo = int(costo)
                    print("El paquete con destino a",destino,"vale",costo,"euros")
                else:
                    if zona == 5:
                        destino = "Asia"
                        costo = 18*(peso*1000)
                        costo = int(costo)
                        print("El paquete con destino a",destino,"vale",costo,"euros")
                    else:
                        print("Se han introducido mal los datos")