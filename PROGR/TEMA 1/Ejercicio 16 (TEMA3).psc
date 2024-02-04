Algoritmo sin_titulo
	Definir i Como Entero
	
	//Este es un bucle FOR donde se limita las veces que se ejecuta este bucle
	Para i<-320 Hasta 160 Con Paso -20 Hacer
		Escribir i
	Fin Para
	
	//Este es un bucle WHILE donde, mientras i sea mayor o igual a 160 se hagan las operaciones adjuntas
	i<-320
	Mientras i>=160 Hacer
		Escribir i
		i=i-20
	Fin Mientras
	
	//Este es un bucle DO-WHILE donde, se ejecutan primero las acciones hasta que i sea menor a 160
	i<-320
	Repetir
		Escribir i
		i=i-20
	Hasta Que i<160
	
FinAlgoritmo