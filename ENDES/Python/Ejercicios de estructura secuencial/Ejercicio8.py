# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá 
#por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

print("Escriba las 3 ventas del mes")
venta1 = int(input())
venta2 = int(input())
venta3 = int(input())

print("Escriba el sueldo base")
sueldo = int(input())

comision = (venta1+venta2+venta3)*0.10

print("El sueldo base es de",sueldo)
print("La comisión del mes es de",comision)
print("El sueldo total del mes es de",(sueldo+comision))