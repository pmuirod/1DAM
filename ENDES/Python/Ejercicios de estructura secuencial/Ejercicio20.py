# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

print("¿Cuántas monedas de 2€ tiene?")
euro_2 = input()
print("¿Cuántas monedas de 1€ tiene?")
euro_1 = input()
print("¿Cuántas monedas de 50 céntimos tiene?")
cent_50 = input()
print("¿Cuántas monedas de 20 céntimos tiene?")
cent_20 = input()
print("¿Cuántas monedas de 10 céntimos tiene?")
cent_10 = input()

dinero = (euro_2*2)+(euro_1*1)+(cent_50*0.50)+(cent_20*0.20)+(cent_10*0.10)

print("Tienes",dinero"euros")