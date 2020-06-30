def main():
	l1, l2 = [12,43,62,10,300],[8,0,5,6,132]
	l3 = []

	cont = -2

	for i in range(len(l2)):
		cont += 2
		l1[cont:cont+1:1] += l2[i:i+1:1]


	print(l1)

main()

