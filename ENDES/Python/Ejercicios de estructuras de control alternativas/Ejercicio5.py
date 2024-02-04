# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
# Por: Pablo Muiño Rodríguez

print("Escriba el nombre de usuario")
nombre = input()
print("Escriba la contraseña")
contraseña = input()

if nombre=="pepe" and contraseña=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error de inicio de sesión")