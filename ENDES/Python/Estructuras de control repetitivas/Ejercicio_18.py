# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
# Por: Pablo Muiño Rodríguez

segundos_muiño=0
minutos_muiño=0
horas_muiño=0

while horas_muiño!=24:
    print(horas_muiño,":",minutos_muiño,":",segundos_muiño)
    if segundos_muiño == 30:
        print("Quiere parar (si o no)")
        respuesta_muiño = input()
        if respuesta_muiño=="si":
            break
    segundos_muiño = segundos_muiño+1
    if segundos_muiño == 60:
        minutos_muiño = minutos_muiño+1
        segundos_muiño=0
        if minutos_muiño == 60:
            horas_muiño = horas_muiño+1
            minutos_muiño=0