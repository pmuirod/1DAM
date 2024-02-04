# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

from math import sqrt

cateto1 = int(input("Dime uno de los dos catetos de un triángulo rectángulo: "))
cateto2 = int(input("Dime el otro cateto de un triángulo rectángulo: "))

hipotenusa2 = (cateto1^2)+(cateto2^2)
hipotenusa = sqrt(hipotenusa2)

print("La hipotenusa del triángulo rectángulo con catetos",cateto1,"y",cateto2,"es",hipotenusa)