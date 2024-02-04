Algoritmo sin_titulo
	//Se pide que se digan los 20 primeros numeros naturales (1-20)
	definir i Como Entero
	
	//Con un bucle de tipo FOR ya que se sabe que va a haber un número finito de secuencias.
	Para i<-1 Hasta 20 Con Paso 1 Hacer
		Escribir i
	Fin Para
	
	//Con un bucle WHILE donde mientras que la variable sea <=20 se repita el proceso; en caso contrario se acaba.
	i<-1
	Mientras i<20 Hacer
		i=i+1
		Escribir i
	Fin Mientras
	
	//Con un bucle DO-WHILE donde mientras que i>19 se vuelvan a repetir las operaciones del principio; en caso contrario se acaba.
	i<-1
	Repetir
		i=i+1
		Escribir i
	Hasta Que i=20
FinAlgoritmo