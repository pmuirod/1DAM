# Pablo Muiño Rodríguez
# Escriba un programa en python que permita crear un menú con las siguientes opciones:
#   - Insertar: Me solicitará una cadena de caracteres que representará los nombres de los alumnos de una clase. Se deberá insertar en la lista al menos 6 nombres y varios repetidos. 
#   - Contar: Me pide un nombre de alumno y me dice cuantas veces aparece en la lista
#   - Mostrar: Muestra la lista de alumnos uno debajo de otro
#   - Terminar
# El programa debe informar de que se ha pulsado una opción correcta.

terminar_pablo = False
alumnos_pablo = []
seguir_pablo = True
contador_pablo = int
contador_pablo = 0

while terminar_pablo!=True:     # Bucle para que siga apareciendo el menú mientras que la condición siga siendo Verdadera
    print("Bienvenido al menú")
    print("1. Insertar")
    print("2. Contar")
    print("3. Mostrar")
    print("4. Terminar")
    print("Escoja una opción para continuar (1-4): ",end="")
    respuesta_pablo = int(input())      # Pido que introduzca una de las opciones del menú

    if respuesta_pablo==1:
        print("Introduzca los nombres de al menos 6 alumnos")
        while seguir_pablo == True:     # Bucle para introducir al menos 6 nombres (mínimo establecido) mientras que la condición sea Verdadera
            nombre_pablo = input()
            alumnos_pablo.append(nombre_pablo)
            contador_pablo = contador_pablo+1       # Contador para saber cuándo se han introducido 6 nombres o más
            if contador_pablo >= 6:
                print("¿Desea continuar?")      # Al llegar a 6 nombres el programa preguntará si se desea seguir
                respuesta2_pablo = input()
                if respuesta2_pablo == "Si":        # En caso afirmativo la condición del bucle seguirá siendo Verdedera
                    seguir_pablo = True
                if respuesta2_pablo == "No":        # En caso negativo la condición del bucle será Falsa y se parará
                    seguir_pablo = False
    print("")
    
    if respuesta_pablo==2:
        if contador_pablo<6:        # Si el contador anterior cuenta menos de 6 nombres en la tabla dará un error, ya que es el mínimo necesario para realizar las operaciones
            print("No se cumple el mínimo de datos en la lista (minimo 6 alumnos)")
        else:
            print("Escriba el nombre de un alumno introducido con anterioridad: ",end="")       # Se pide un nombre para contar cuántas veces sale en la lista
            nombre_pablo = input()
            cuenta_pablo = alumnos_pablo.count(nombre_pablo)        # Asigno a una variable la operación de contar
            print("Aparece un total de",cuenta_pablo,"veces el nombre",nombre_pablo)
    print("")
    
    if respuesta_pablo==3:
        if contador_pablo==0:       # Si no hay ningún nombre en la lista dará este fallo puesto que es si no hay nombres en la lista estos no se pueden mostrar
            print("No se puede ejecutar porque no hay ningún valor en la lista")
        else:
            print("Los alumnos de la lista son:")
            for i in range(0,contador_pablo):       # Escribo los nombres de la lista apoyándome en el contador anterior
                print("-",alumnos_pablo[i])
    print("")
    
    if respuesta_pablo==4:
        terminar_pablo = True       # Al querer salir del menú, la condición del bucle principal cambia a ser Falsa y se parará