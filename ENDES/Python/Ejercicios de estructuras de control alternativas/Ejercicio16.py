# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, 
# y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 
# 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
# Por: Pablo Muiño Rodríguez

print("Indique cuanto ha durado la llamada (en minutos)")
minutos = int(input())
print("Indique el dia que ha realizado la llamada")
dia = input()
print("Indique el momento de la realización de la llamada (Mañana o Tarde)")
turno = input()

coste = float

if minutos<=5:
    coste=1*minutos
else:
    if minutos>5 & minutos<=8:
        coste=(5*1)+(0.80*(minutos-5))
    else:
        if minutos>8 & minutos<=10:
            coste=(5*1)+(3*0.8)+(0.70*minutos-8)
        else:
            if minutos>10:
                coste=0.50*minutos
            else:
                print("Se han introducido mal los datos")

if dia == "Domingo":
    coste = coste*1.03
else:
    if turno == "Mañana":
        coste = coste*1.15
    else:
        coste = coste*1.10

print("Debe pagar por la llamada",coste,"€")