Algoritmo sin_titulo
	Escribir "¿De que sabor quiere la tarta?"
	Leer sabor
	Según sabor Hacer
		"chocolate":
			Escribir "¿Chocolate blanco o negro?"
			Leer chocolate
			Si chocolate=negro Entonces
				Base = 14
			SiNo
				Base = 15
			FinSi
		"manzana":
			Base = 18
		De Otro Modo:
			Base = 16
	FinSegún
	Escribir "¿Quiere nata?"
	Leer nata
	Si nata="si" Entonces
		Escribir "¿Quieres poner un nombre?"
		Leer nombre
		Si nombre="si" Entonces
			Precio = base+2.75+2.5
		SiNo
			Precio = base+2.5
		FinSi
	SiNo
		Escribir "¿Quieres poner un nombre?"
		Leer nombre
		Si nombre="si" Entonces
			Precio = base+2.75
		SiNo
			Precio = base
		FinSi
	FinSi
	Escribir "El precio de su tarta es " Precio
FinAlgoritmo
