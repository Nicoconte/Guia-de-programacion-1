import random as r

def generar_lista():
	lista = []
	elementos = r.randint(0,10)
	
	for i in range(1,10,1):
		lista.append(elementos)
		elementos = r.randint(0,10)

	return lista

def main():
	lista = generar_lista()
	nueva_lista = []

	numero = 0
	total = 0
	suma = 0

	for i in range(1,len(lista),1):
		suma = lista[i-1] + lista[i]
		total = total + (suma + lista[i])
		print("Suma ", suma , " = > total ", total)
		nueva_lista.append(total)

	print(lista)
	print()
	print(nueva_lista)

main()
 
"""
Pendiente!!!!!!!!!
"""