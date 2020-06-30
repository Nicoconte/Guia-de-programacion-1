import random as r

def generar_listas():
	l1 = []

	n = r.randint(10,50)
	f = r.randint(0,100)

	for i in range(f):
		if n % 2 == 0:
			l1.append(n)
		n = r.randint(10,50)

	return l1


def main():
	lista = generar_listas()
	listaR1 = []
	listaR2 = []

	listaR1 = lista[0:len(lista)//2]

	listaR2 = lista[len(lista)//2:]

	print("Lista original => ",lista,"\n","Primera mitad => ",listaR1,"\n","Segunda mitad => ",listaR2)
	print()

	print(len(lista)," ",len(listaR1)," ",len(listaR2))


main()