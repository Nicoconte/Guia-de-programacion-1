def verificar_lista(l):
	ordenada = False
	if(l == sorted(l)):
		ordenada = True
	else:
		ordenada = False

	return ordenada,l

def main():
	lista = [3,2,1] 
	print(verificar_lista(lista))


main()