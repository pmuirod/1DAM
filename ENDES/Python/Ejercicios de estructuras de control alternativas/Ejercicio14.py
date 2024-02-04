# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
# Por: Pablo Muiño Rodríguez

print ("Escriba cuánto vale el kilo de uva")
precio_bruto = int(input())
print("¿De qué tipo quiere la uva? (A o B)")
tipo = input()
print("¿De qué tamaño la quiere? (1 o 2)")
tamaño = input()
print("¿Cuántos kilos quiere?")
kilos = int(input())

if tipo == "A" and tamaño == "1":
    precio_final = (precio_bruto*1.20)*kilos
    print("El productor recebirá",precio_final,"€")
else:
    if tipo == "A" and tamaño == "2":
        precio_final = (precio_bruto*1.30)*kilos
        print("El productor recebirá",precio_final,"€")
    else:
        if tipo == "B" and tamaño == "1":
            precio_final = (precio_bruto*0.70)*kilos
            print("El productor recebirá",precio_final,"€")
        else:
            if tipo == "B" and tamaño == "2":
                precio_final = (precio_bruto*0.50)*kilos
                print("El productor recebirá",precio_final,"€")
            else:
                print("Se han introducido mal los datos")