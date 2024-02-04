Algoritmo sin_titulo
	//Leer 100 numeros no nulos y muestre cuantos numeros negativos ha leido algun numero negativo
	Definir N Como Entero
	Definir nulo Como Logico
	Definir negativo,positivo Como Entero
	
	nulo=falso
	negativo=0
	positivo=0
	
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir "Escriba un numero no nulo (0-100)"
		Leer N
		Si N<0 Entonces
			nulo=verdadero
		SiNo
			
		Fin Si
	Fin Para
	
	Escribir "Se han introducido algunos numeros nulos"
	

FinAlgoritmo