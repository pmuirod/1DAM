Algoritmo sin_titulo
	Escribir '¿Cuántas horas trabajas a la semana?'
	Leer h
	Escribir '¿Cuanto cobras por hora trabajada?'
	Leer a
	Si h>35 Entonces
		b <- ((h-35)*(a*1.5))+(h*a)
	SiNo
		b <- h*a
	FinSi
	Si b>=500 Entonces
		Si b>=900 Entonces
			n <- b*0.75
			Escribir "La tasa es del 45%"
		SiNo
			n <- b*0.55
			Escribir "La tasa es del 25%"
		FinSi
	SiNo
		n <- b
		Escribir "La tasa es del 0%"
	FinSi
	Escribir "Su salario bruto es de " b
	Escribir 'Su salario neto es de ', n
FinAlgoritmo
