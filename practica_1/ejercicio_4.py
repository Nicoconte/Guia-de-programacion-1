"""
Entrada =>  Cantidad de viajes hechos en un mes

Proceso =>  Valor de la tarifa?
			Verificar cuantos viajes hizo, en base a eso sacar:
				* 1 a 20 viajes    => Valor x 
				* 21 a 30 viajes   => 20% sobre el total
				* 31 a 40 viajes   => 30% sobre el total
				* mas de 40 viajes => 40% sobre el total  

Salida =>   Cantidad de dinero gastado en un mes de viaje

"""
import random

def obtener_gasto(v):
	tarifa = 135 #Nunca especifica cual es el valor de la tarifo, solo los desc que se aplican
	gasto_total = 0
	if v > 1 and v <= 20:
		gasto_total = tarifa * v
	elif v >= 21 and v <= 30:
		gasto_total = (20 * (tarifa * v)) // 100
	elif v >= 31 and v <= 40:
		gasto_total = (30 * (tarifa * v)) // 100
	elif v >= 41:
		gasto_total = (40 * (tarifa * v)) // 100
	return gasto_total

def viajes_hechos():
	#viajes = int(input("Cantidad de viajes realizados en un mes "))
	for i in range(0,20,1):	#Solo para probar 20 veces sin tener que reiniciarlo
		viajes = random.randint(0,1000)
		print("\n","Cantidad de viajes hechos ",viajes,"\n","Gasto total: ",obtener_gasto(viajes))

viajes_hechos()