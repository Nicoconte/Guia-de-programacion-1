"""
Entrada = un numero N entre 0 y 100

Proceso => -Verificar que el numero ingresado este entre 0 y 100
		   -Devolver la suma de los cuadrados de los numeros que se encuentran entre 1 y N (Sumar y elevar cada 4 unidades)

Salida => -Suma de los numeros al cuadrado

"""


import random

def suma_de_cuadrados(n):
	num = 0
	for i in range(1,n,4):
		print("n=> ",n," i=> ",i," i**2=>",i**2," num=> ",num)
		num = num + i ** 2
	return num

#numero = random.randint(1,100)
# o sino

def obtener_resultado():
	numero = int(input("Coloque un numero entre 0 y 100: "))
	if numero > 0 and numero < 100:
		print(suma_de_cuadrados(numero))
	else:
		print("Ingrese un numero entre 0 y 100. Numero ingresado => ",numero)
		return obtener_resultado()
	

obtener_resultado()