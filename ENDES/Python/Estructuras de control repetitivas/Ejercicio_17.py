# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.
# Por: Pablo Muiño Rodríguez

print("¿Cuántos trabajadores hay?")
trabajadores_muiño = int(input())
print("¿Cuánto cobra por hora?")
base_muiño = float(input())
print("¿Cuántas horas trabaja al dia?")
horas_muiño = float(input())
print("¿Cuántos días a trabajado esta semana?")
dias_muiño = int(input())

sueldo_muiño = base_muiño*(horas_muiño*dias_muiño)

print("El trabajador cobrará a la semana",sueldo_muiño,"euros")
print("La empresa pagará",sueldo_muiño*trabajadores_muiño,"euros")