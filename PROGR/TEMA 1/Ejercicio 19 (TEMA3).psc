Algoritmo sin_titulo
	Definir N2,contador Como Entero
	Definir media Como Real
	
	Escribir "Introduzca una serie de numeros positivos (si quiere parar ponga uno negativo)"
	contador=0
	N2=0
	Mientras N>=0 Hacer
		N2=N+N2
		Leer N
		Si N<>-1 Entonces
			contador=contador+1
		SiNo
			
		Fin Si
	Fin Mientras
	media=N2/contador
	Escribir "La media de estos numeros es " media
	
FinAlgoritmo