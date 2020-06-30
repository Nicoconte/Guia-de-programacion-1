"""
Entrada => 3 numeros positivos

Proceso => -Ingresar 3 numeros mayores a 0
		   -Guardalos en una lista
		   -Recorrer la lista e ir comparando sus elementos
		   		*El elemento mayor se guarda en una variable llamada num_max
		   		*Si los elementos son iguales retorna -1 (No hay mayor estricto)
		   	-Retornar el numero mas grande (num_max = Mayor estricto)
		   	
Salida => El numero mayor 

"""

def obtener_mayor_estricto(numbers):
	print(numbers)
	num_max = 0
	for i in numbers:
		if i > num_max:
			num_max = i
		elif i == num_max:
			num_max = -1
		else:
			pass
	return num_max


def dar_numeros():
	num = int(input("Ingrese un numero "))
	if num < 0:
		print("Los numeros deben ser positivos")
		return dar_numeros()
	else:
		list_of_numbers = []
		for i in range(0,3,1):
			list_of_numbers.append(num)
			num = int(input("Ingrese un numero nuevo "))
		return list_of_numbers

#-----------------------------------------------------------------------------

numbers = dar_numeros()
if obtener_mayor_estricto(numbers) == -1:
	print("No hay mayor estricto ",obtener_mayor_estricto(numbers))
else:
	print("El numero mayor estricto es ", obtener_mayor_estricto(numbers))