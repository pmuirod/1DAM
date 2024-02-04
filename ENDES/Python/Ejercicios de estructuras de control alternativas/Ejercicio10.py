# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:
# - exteriores
# - tangentes exteriores
# - secantes
# - tangentes interiores
# - interiores
# - concéntricas
# Por: Pablo Muiño Rodríguez

print("Escriba los puntos centrales de dos circunferencias (x1,y1)(x2,y2)")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print("Escriba el radio de las dos circunferencias")
radio1 = int(input())
radio2 = int(input())

distancia = ((x2-x1)**2)+((y2-y1)**2)

if distancia>(radio1+radio2):
    print("Son circunferencias exteriores")
else:
    if distancia==(radio1+radio2):
        print("Son circunferencias tangentes exteriores")
    else:
        if (distancia<(radio1+radio2) and distancia>(radio1-radio2)):
            print("Son circunferencias secantes")
        else:
            if distancia==(radio1-radio2):
                print("Son circunferencia tangentes interiores")
            else:
                if distancia<(radio1-radio2):
                    print("Son circunferencias interiores")
                else:
                    print("Son circunferencias concéntricas")