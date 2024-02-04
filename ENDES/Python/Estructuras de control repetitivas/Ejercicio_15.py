# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
# Por: Pablo Muiño Rodríguez

pago_muiño=40
mes_muiño=3

while mes_muiño!=20:
    pago_muiño = pago_muiño*2
    mes_muiño = mes_muiño+1
    print("El mes",mes_muiño,"ha pagado",pago_muiño)

print("En total se han pagado",pago_muiño,"euros")