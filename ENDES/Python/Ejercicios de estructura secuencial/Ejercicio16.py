# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
#El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia 
#entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en 
#que tiempo (minutos) alcanzará el vehículo más rápido al otro.

print("Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d, indique las dos velocidades (siendo la segunda mayor) y la distancia entre los dos")
v1 = input()
v2 = input()
d = input()

d + v1*tiempo == v2*tiempo
d == v2*tiempo - v1*tiempo
tiempo = d/v2
tiempo = tiempo*60

print("El tiempo que tardará es de",tiempo" minutos")