Algoritmo sin_titulo
	Definir i Como Entero
	
	//Este es un bucle FOR donde se limita las veces que se ejecuta este bucle
	Para i<-1 Hasta 100 Con Paso 1 Hacer
		Si i%5=0 Entonces
			Escribir i
		SiNo
			
		Fin Si
	Fin Para
	
	//Este es un bucle WHILE donde, mientras i sea menor o igual a 100 se hagan las operaciones adjuntas
	i<-1
	Mientras i<=100 Hacer
		Si i%5=0 Entonces
			Escribir i
		SiNo
			
		Fin Si
		i=i+1
	Fin Mientras
	
	//Este es un bucle DO-WHILE donde, se ejecutan primero las acciones hasta que i sea igual a 100
	i<-1
	Repetir
		Si i%5=0 Entonces
			Escribir i
		SiNo
			
		Fin Si
		i=i+1
	Hasta Que i>100
	
FinAlgoritmo