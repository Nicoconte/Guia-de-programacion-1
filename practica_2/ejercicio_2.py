import random as r

def generar_lista():
	lista = []
	numeros = r.randint(1,100)
	for i in range(1,50,1):
		lista.append(numeros)
		numeros = r.randint(1,100)
	return lista

def identificar_repetidos(l):
	repetidos = False
	for i in l:
		for j in l:
			if i == j:
				repetidos = True
			else:
				repetidos = False
	return repetidos

def eliminar_repetidos(l):
	nueva_lista = []
	for i in l:
		if i not in nueva_lista:
			nueva_lista.append(i)
	return nueva_lista

def main():
	lista = generar_lista()

	print("Lista original => ", lista,"\n")
	print("Hay repetidos? => ", identificar_repetidos(lista),"\n")
	print("Lista sin repetidos => ", eliminar_repetidos(lista))

main()