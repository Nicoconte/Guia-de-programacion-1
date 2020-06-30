def dibujar_cuadrado(c,f):
	for i in range(1,c + 1):
		for j in range(1,f + 1):
			print("*", end=" ")
		print(" ")

def dibujar_triangulo(c):
	for i in range(c+1):
		print("*"*i)


columnas = int(input("Ingrese la cantidad de columnas "))
filas = int(input("Ingrese la cantidad de filas "))

print("\n","Rectangulo/Cuadrado: ")
dibujar_cuadrado(columnas,filas)

print("\n","Triangulo rectangulo (Solo toma el valor de las columnas): ")
dibujar_triangulo(columnas)