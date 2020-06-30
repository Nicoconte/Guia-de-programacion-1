def obtenerCadenas(cadena_1, cadena_2):
	
	respuesta = ""

	try:
		num_1, num_2 = float(cadena_1), float(cadena_2)
		respuesta = str(num_1 + num_2)
	
	except ValueError:
		respuesta = "-1" 

	return respuesta


print(obtenerCadenas("3.5","3.2"))	