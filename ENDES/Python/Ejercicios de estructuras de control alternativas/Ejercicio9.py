# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
# Por: Pablo Muiño Rodríguez

print("Escriba tres números")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1>num2 and num2>num3):
    print(num1,num2,num3)
else:
    if (num1>num2 and num2<num3 and num1>num3):
        print(num1,num3,num2)
    else:
        if (num2>num1 and num1>num3):
            print(num2,num1,num3)
        else:
            if (num2>num1 and num1<num3 and num2>num3):
                print(num2,num3,num1)
            else:
                if(num3>num1 and num1>num2):
                    print(num3,num1,num2)
                else:
                    if (num3>num1 and num1<num2 and num3>num2):
                        print(num3,num2,num1)
