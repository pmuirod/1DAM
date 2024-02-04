# Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.

from Funciones.Funcion11y12 import leerFecha, validar, calcular_Dia_Juliano

año_muino, mes_muino, dia_muino = leerFecha()

if validar(año_muino,mes_muino,dia_muino)==True:
    calcular_Dia_Juliano(año_muino,mes_muino,dia_muino)
else:
    print("La fecha dada no es correcta")