Algoritmo sin_titulo
	Definir N,contador,total Como Entero
	Definir media Como Real
	
	contador<-0
	total<-0
	Escribir "Introduzca una serie de numeros"
	Repetir
		Leer N
		contador=1+contador
		total=N+total
	Hasta Que total>10000
	total=total-N
	contador=contador-1
	media=total/contador
	Escribir "El total acumulado es de " total
	Escribir "Se han introducido " contador " numeros"
	Escribir "La media es " media
	
FinAlgoritmo