import random as r

def generar_lista(n):
	lista = []
	elementos = r.randint(0,20)

	for i in range(1,n,1):
		lista.append(elementos**2)
		elementos = r.randint(0,20)
	return lista

def main():
	elemento = int(input("Cuantos elementos quiere en la lista "))
	if elemento >  0 and elemento <= 10:
		print("Coloque un numero positivo o mayor a 10")
		main()
	else:
		lista = generar_lista(elemento)
		ultimos_elementos = []

		lon = len(lista)

		for i in range(lon-10,lon):
			ultimos_elementos.append(lista[i])


	print("Lista original => ", lista,"\n","Ultimos 10 elementos => ",ultimos_elementos)

main()
