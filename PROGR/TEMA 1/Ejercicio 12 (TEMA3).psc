Algoritmo sin_titulo
	Definir A,B Como Entero
	
	Escribir "Introduzca la base de una potencia"
	Leer A
	Escribir "Introduzca el exponente de una potencia"
	Leer B
	
	N=A
	Repetir
		Si B=1 Entonces
			A=A
		SiNo
			A=N*A
			B=B-1
		Fin Si
	Hasta Que B=1
	Escribir "La potencia es " A
	
FinAlgoritmo