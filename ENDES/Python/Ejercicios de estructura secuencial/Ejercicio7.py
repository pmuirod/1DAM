# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

entrada = int(input("Escriba una cantidad de minutos: "))

horas = int(entrada/60)
minutos = (entrada%60)

print(entrada,"minutos son",horas,"horas y",minutos,"minutos")