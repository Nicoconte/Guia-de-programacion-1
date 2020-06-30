"""
Entrada => 3 numeros positivos

Proceso:
	=> Verificar si son positivos
	=> Que cada numero pertenezca a una fecha gregoriana
		Ej: El primer numero debe estar entre 1 y 31
			El segundo numero entre 1 y 12
			El tercer numero entre 1582(Creacion de calendario gregoriano) y 2020
	=> Si los numeros ingresados pertenecen al calendario gregoriano, retornar TRUE sino retorno FALSE
	=> Crear una funcion que verifique si realmente la funcion anterior funciona como tal(No tengo idea a que se refiere)

Salida:
	=> True o False

Tablas de verdad (Necesario para este programa):

p | q  | p ^ q
F   F      F
F   V      F
V   F      F
V   V      V
"""

import random
import time

def introducir_fecha(d,m,a):
	if (d > 0 and d < 32) and (m > 0 and m < 13) and (a > 1582 and a < 2020):
		return True
	else:
		return False

def pruebas():
	dia  = random.randint(0,50)
	mes  = random.randint(0,20)
	anio = random.randint(0,2200)
	intentos = 0
	while(True): #solo para probbarlo y no tener que reiniciarlo
		if introducir_fecha(dia,mes,anio) == True:
			print("Fecha generada: ",dia,"/",mes,"/",anio,"\n",introducir_fecha(dia,mes,anio))
			print("Intentos => ",intentos,"\n","Fin del ejercicio")
			break
		else:
			print("Fecha generada: ",dia,"/",mes,"/",anio)
			print(introducir_fecha(dia,mes,anio))
		dia  = random.randint(0,50)
		mes  = random.randint(0,20)
		anio = random.randint(0,2200)
		intentos += 1
		time.sleep(1)


pruebas()