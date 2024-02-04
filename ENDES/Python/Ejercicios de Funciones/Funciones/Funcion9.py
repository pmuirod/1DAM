# Función para encontrar el MCD de dos números

def calcularMCD(num1_muino,num2_muino):
    if num1_muino%num2_muino == 0:
        return num2_muino
    else:
        num2_muino = num1_muino%num2_muino
        return calcularMCD(num1_muino,num2_muino)