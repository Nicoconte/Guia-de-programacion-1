import random

# 3 Listas: 1- La original / 2- Palabras a eliminar / 3- La resultante

def ingresar_palabras_a_eliminar():
	palabras_a_eliminar = []
	entrada = input(("Que palabras deseas eliminar "))
	while(entrada != "listo"):
		palabras_a_eliminar.append(entrada)
		entrada = input(("Que palabras deseas eliminar "))
	return palabras_a_eliminar

def eliminar_palabras(l1,l2):
	lista_resultante = []
	for i in l1:
		if i not in l2:
			lista_resultante.append(i)
	return lista_resultante

def main():
	lista_original_palabras = ['hola','chau','nicolas','adios','linkin park']
	lista_de_palabras = ingresar_palabras_a_eliminar()
	lista_resultante = eliminar_palabras(lista_original_palabras, lista_de_palabras)
	
	print("Lista original => ", lista_original_palabras,"\n","Lista de palabras a eliminar => ", lista_de_palabras)
	print("\n","Lista resultante => ", lista_resultante)


main()
