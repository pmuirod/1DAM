Algoritmo sin_titulo
	Escribir 'Cu�l es tu cargo siendo 1-Prog. Junior, 2-Prog. senior y 3-Jefe de proyecto'
	Leer cargo
	Escribir 'Cu�ntos d�as has estado de viaje visitando clientes durante el mes'
	Leer d�as
	Escribir 'Indique su estado civil siendo 1-Soltero y 2-Casado'
	Leer estado
	Si cargo=1 Entonces
		sueldo <- 950
	SiNo
		Si cargo=2 Entonces
			sueldo <- 1200
		SiNo
			sueldo <- 1600
		FinSi
	FinSi
	bruto <- sueldo+(d�as*30)
	Si estado=1 Entonces
		neto <- bruto-(bruto*0.25)
	SiNo
		neto <- bruto-(bruto*0.20)
	FinSi
	Escribir 'Su salario neto es de ', neto
FinAlgoritmo
