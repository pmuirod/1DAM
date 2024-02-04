# Función para comprobar que el nombre de usuario y la contraseña introducidos son los correctos

def comprobarAcceso(nombre,clave):
    if nombre=="usuario1" or clave=="asdasd":
        acceso = True
    else:
        acceso = False
    
    return acceso