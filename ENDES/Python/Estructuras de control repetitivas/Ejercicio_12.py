# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.
# Por: Pablo Muiño Rodríguez

mes_muiño = 1
suma_muiño = 0

while mes_muiño<=12:
    print("¿Cuánto has ahorrado este mes?")
    ahorro_muiño = float(input())

    mes_muiño = mes_muiño+1

    suma_muiño = suma_muiño + ahorro_muiño

    print("Llevas ahorrado",suma_muiño,"euros")