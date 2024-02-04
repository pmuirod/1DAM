Algoritmo sin_titulo
	Definir min,max Como Real
	Definir respuesta Como Caracter
	
	Escribir "Voy a intentar adivinar un número que estes pensando (escriba + si es mayor, - si es menor o = si es su número)"
	min<-0
	max<-100
	mitad=(min+max)/2
	Escribir mitad
	Repetir
		Leer respuesta
		Si respuesta="+" Entonces
			min<-mitad
			mitad=(min+max)/2
			mitad=TRUNC(mitad)
			Escribir mitad
		SiNo
			Si respuesta="-" Entonces
				max<-mitad
				mitad=(min+max)/2
				mitad=TRUNC(mitad)
				Escribir mitad
			SiNo
				
			Fin Si
		Fin Si
	Hasta Que respuesta="="
	
FinAlgoritmo