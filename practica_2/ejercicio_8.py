import random as r

#Revisar

def generar_listas():
	primera_lista = []
	segunda_lista = []

	n = r.randint(1,50)

	for i in range(3):
		primera_lista.append(n)
		n = r.randint(1,50)

	for i in range(3):
		segunda_lista.append(n)
		n = r.randint(1,50)

	return primera_lista, segunda_lista


def generar_lista_resultante(l1, l2):

	aux = []
	lista_resultante = []

	for i in l1:
		aux.append(i)

	for j in l2:
		aux.append(j = [1:len(aux):1+1])



	return aux


def main():
	lista1, lista2 = generar_listas()
	listaR = generar_lista_resultante(lista1, lista2)

	print("Listas originales => ",lista1,"\n",lista2,"\n","\n","Lista resultante => ",listaR)

main()