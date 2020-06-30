import random as r


def generar_listas():
	l1 = []
	l2 = []
	elementos = r.randint(1,100)

	for i in range(1,50):
		l1.append(elementos)
		elementos = r.randint(1,100)

	for i in range(1,50):
		l2.append(elementos)
		elementos = r.randint(1,100)

	return l1,l2

def superposicion(l1,l2):

	repetidos = False

	for i in l1:
		for j in l2:
			if i in l2 or j in l1:
				repetidos = True
			else:
				repetidos = False

	return repetidos


def main():
	lista1,lista2 = generar_listas()

	print("Lista 1 => ", lista1, "\n", "Lista 2 => ",lista2)

	print(superposicion(lista1,lista2))


main()