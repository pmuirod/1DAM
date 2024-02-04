# Pablo Muiño Rodríguez
# Módulo para comprobar si un número es múltiplo de otro

def EsMultiplo(n1,n2):
    if n1>n2:
        if n1%n2==0:
            print(n1,"es múltiplo de",n2)
        else:
            print(n1,"no es múltiplo de",n2)
    if n2>n1:
        if n2%n1==0:
            print(n2,"es múltiplo de",n1)
        else:
            print(n2,"no es múltiplo de",n1)