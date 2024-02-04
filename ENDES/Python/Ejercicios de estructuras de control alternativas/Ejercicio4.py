# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
# Por: Pablo Muiño Rodíguez

print("Escriba dos números para hacer su división")
num1 = int(input())
num2 = int(input())

if num2==0:
    print("No se puede dividir entre 0")
else:
    print("La división da como resultado",(num1/num2))