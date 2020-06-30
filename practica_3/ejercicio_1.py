import random as r

n = int(input("Ingresa la cantidad de filas "))
m = int(input("Ingresa la cantidad de columnas "))

num = 1

matriz = []

for i in range(n):
	matriz.append([1])
	for j in range(m):
		num += 2
		matriz[i].append(num)
	

print(matriz)

n = 5
a = [[0] * n for i in range(n)]
contador = 1
for f in range(n):
    if (f%2):
        for c in range(n-1, -1, -1):
            if (f>c):
                a[f][c] = 0
            else:
                a[f][c] = contador
                contador = contador +1
    else:
        for c in range(n):
            if (f>c):
                a[f][c] = 0
            else:
                a[f][c] = contador
                contador = contador +1

print(a)