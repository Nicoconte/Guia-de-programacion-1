def main():
	while True:
		try:
			nro = int(input("Ingrese un numero entero "))
			if (nro < 0):
				print("Debe ser positivo")
			else:
				print(f"Numero {nro}")
				break

		except ValueError:
			print("Error, debe ser un numero entero")

main()