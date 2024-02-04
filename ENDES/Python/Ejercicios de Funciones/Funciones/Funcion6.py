# Función para calcular el área y el perímetro de una circunferencia

import math

def calcularAreaPerimetro(r_muino):
    area_muino = math.pi*(r_muino**2)
    perimetro_muino = math.pi*(r_muino*2)

    print("El área de la circunferencia es",area_muino)
    print("El perimetro de la circunferencia es",perimetro_muino)