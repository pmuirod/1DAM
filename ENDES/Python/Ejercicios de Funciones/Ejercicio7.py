# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

from Funciones.Funcion7 import comprobarAcceso
acceso = bool
acceso = False
intentos_muino = int
intentos_muino = 0

while acceso!=True:
    print("Escriba el nombre de usuario:")
    nombre_muino = input()
    print("Escriba la clave:")
    clave_muino = input()

    acceso = comprobarAcceso(nombre_muino,clave_muino)

    if intentos_muino > 3:
        print("Se han acabado los intentos")
        break

    if acceso==False:
        print("____Acceso denegado____")
        intentos_muino +=1
        print("Numero de intentos fallidos:",intentos_muino)

if acceso==True:
    print("____Bienvenido____")