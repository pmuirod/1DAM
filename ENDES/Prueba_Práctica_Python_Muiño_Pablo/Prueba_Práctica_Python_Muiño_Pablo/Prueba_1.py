# Pablo Muiño Rodríguez
# Codifica un programa en python que solicite información al usuario y nos permita guardar en un diccionario los nombres de tres alumnos de la clase junto con cuatro notas de actividades de clase. 
# A continuación deberá imprimir los tres alumnos con sus notas correspondientes y en el siguiente formato:
#       Nombre_de_alumno ha sacado las siguientes notas: ['nota1', 'nota2', 'nota3']

alumnos_pablo = {}
notas_pablo = []

for i in range(0,3):        # Bucle para introducir los nombres de los tres alumnos
    print("Escriba el nombre del alumno",i+1,": ",end="")
    nombre_pablo = input()
    print("Escriba a continuación las cuatro notas correspondientes al",i+1,"alumno:")
    for i in range(0,4):        # Bucle para introducir las cutro notas de cada alumno
        nota_pablo = int(input())
        notas_pablo.append(nota_pablo)      # Añado la nota introducida por teclado a la lista creada anteriormente
    alumnos_pablo[nombre_pablo] = notas_pablo       # Adjunto la lista con las notas (valor) al alumno al que pertenecen (calve) en el diccionario
    notas_pablo = []        # Reinicio la lista puesto que en la siguiente iteracion las notas serán diferentes ya que serán las de otro alumno

for clave,valor in alumnos_pablo.items():       # Escribo tanto las claves como los valores del diccionario
    print(clave,"ha sacado las siguientes notas:",valor)