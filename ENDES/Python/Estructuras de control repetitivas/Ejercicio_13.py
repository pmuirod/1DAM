# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) 
# y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
# Por: Pablo Muiño Rodríguez

print("Escriba las horas trabajadas diariamente")
horas_muiño = int(input())
print("Escriba a cuánto se paga una hora")
dinero_muiño = int(input())

sueldo_muiño = (horas_muiño*6)*dinero_muiño

print("El trabajador cobrará de sueldo a la semana es de",sueldo_muiño,"euros")