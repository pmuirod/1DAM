Algoritmo sin_titulo
	Definir base,exponente Como Entero
	
	Escribir "Introduzca la base de una potencia"
	Leer base
	Escribir "Introduzca el exponente de una potencia"
	Leer exponente
	
	N=base
	Repetir
		Si esponente=1 Entonces
			base=base
		SiNo
			base=N*base
			exponente=esponente-1
		Fin Si
	Hasta Que exponentee=1
	Escribir "La potencia es " base
	
FinAlgoritmo