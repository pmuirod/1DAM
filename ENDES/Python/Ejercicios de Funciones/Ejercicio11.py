# El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
#   - LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#   - DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#   - EsBisiesto: Recibe un año y nos dice si es bisiesto.
#   - Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

from Funciones.Funcion11 import leerFecha, calcular_Dia_Juliano

año_muino, mes_muino, dia_muino = leerFecha()

calcular_Dia_Juliano(año_muino,mes_muino,dia_muino)