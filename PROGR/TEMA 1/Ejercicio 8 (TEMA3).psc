Algoritmo sin_titulo
	//Leer 100 numeros no nulos y muestre cuantos numeros negativos ha leido algun numero negativo
	Definir N Como Entero
	Definir nulo Como Logico
	Definir negativo,positivo Como Entero
	
	nulo=falso
	negativo=0
	positivo=0
	
	
	Repetir
		Escribir "Escriba un numero no nulo (0-100)"
		Leer N
		Si N<0 Entonces
			nulo=verdadero
			negativo=negativo+1
		SiNo
			positivo=positivo+1
		Fin Si
	Hasta Que N=0
	
	Si nulo=verdadero Entonces
		Escribir "Se ha introducido algun numero nulo"
	SiNo
		Escribir "No se ha introducido ningun numero nulo"
	Fin Si
	
	Escribir "Se ha introducido " negativo " numeros nulos"
	Escribir "Se ha introducido " positivo " numeros no nulos"
	
FinAlgoritmo