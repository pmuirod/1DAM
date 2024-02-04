# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B

print("Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escriba la hora (HH;MM;SS) de la que parte de la ciudad y el tiempo que tiene que se tarda hasta llegar a la otra ciudad (en minutos)")
horas = input()
minutos = input()
segundos = input()
t = input()

minutos = t + minutos

if minutos>59:
    horas=horas+(minutos//60)
    minutos=minutos%60

print("La hora de llegada es a las",horas":"minutos":"segundos)