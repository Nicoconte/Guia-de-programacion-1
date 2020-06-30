"""
Desarrollar cada una de las siguientes funciones y escribir un programa que 
permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de ele-mentos también 
será un número al azar de dos dígitos.

b.Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a elimi-nar se 
ingresa desde el teclado y la función lo recibe como parámetro.

"""

import random

def generar_lista():
	lista = []
	cantidad_elementos = random.randint(0,99)
	numeros = random.randint(0,9999)
	for i in range(1,cantidad_elementos,1):
		lista.append(numeros)
		numeros = random.randint(0,9999)
	return lista

def sumar_elementos(lista):
	suma = 0
	for i in lista:
		suma = suma + i
	return suma

def eliminar_elemento(n,l):
	nueva_lista = []

	for i in l:
		if (i) == n:
			l.remove(n)
		else:
			if l not in nueva_lista:
				nueva_lista.append(i)

	return nueva_lista


def main():
	lista_obtenida = generar_lista()
	print("Elementos de la lista original => ",lista_obtenida)
	print("\n","Suma de los elementos => ", sumar_elementos(lista_obtenida),"\n")
	elemento = int(input("Que elemento desea eliminar: "))
	print("\n","Elementos de la nueva lista ", eliminar_elemento(elemento, lista_obtenida))

main()