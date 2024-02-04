Algoritmo sin_titulo
	//Se pide que se digan los numeros pares comprendidos entre 1 y 200
	Definir i Como Entero
	
	//Con un bucle de tipo FOR ya que se sabe que va a haber un número finito de secuencias.
	Para i<-2 Hasta 200 Con Paso 2 Hacer
		Escribir i
	Fin Para
	
	//Con un bucle WHILE donde mientras que la variable sea <=199 se repita el proceso; en caso contrario se acaba.
	i=2
	Mientras i<=200 Hacer
		Escribir i
		i=i+2
	Fin Mientras
	
	//Con un bucle DO-WHILE donde mientras que i<=199 se vuelvan a repetir las operaciones del principio; en caso contrario se acaba.
	i=2
	Repetir
		Escribir i
		i=i+2
	Hasta Que i=200
FinAlgoritmo