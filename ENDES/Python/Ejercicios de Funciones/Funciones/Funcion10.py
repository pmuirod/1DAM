# Funcion para calcular los segundos de una hora dada en horas, minutos y segundos

def calcularSegundos(horas,minutos,segundos):
    print("La hora",horas,":",minutos,":",segundos,"son",((horas*3600)+(minutos*60)+segundos),"segundos")
    print("")

#Función para calcular la hora en horas, minutos y segundos dado unos segundos

def calcularHorasMinutosSegundos(segundos):
    print("Los",segundos,"segundos corresponden a la hora",int(segundos/3600),":",int((segundos%3600)/60),":",int((segundos%3600)%60))
    print("")