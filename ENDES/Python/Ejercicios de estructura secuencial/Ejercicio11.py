# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)

print ("Escriba dos números")
num1 = input()
num2 = input()

distancia = num1-num2
distancia = abs(distancia)

print ("La distancia entre estos dos números es",distancia)