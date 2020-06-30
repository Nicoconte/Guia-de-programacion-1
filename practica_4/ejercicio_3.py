"""
Entrada => Frase y un numero entero 
Salida => Otra frase con parte de la entrada determinada por el numero entero

"""

def aux(palabra, n):
	if n < len(palabra):
		return True
	else:
		return False


def filtrar_palabras(palabra, n):
	nueva_cadena = "Hola => "
	
	"""
	for i in range(n):
		
		#Es lo mismo nada mas que al usar ternario, se concatena tantas veces el ciclo lo dicte
		#nueva_cadena += palabra[i] if n < len(palabra) else palabra

	
		if n < len(palabra):
			nueva_cadena += palabra[i]
		else:
			nueva_cadena += palabra
			break #Rompemos con el ciclo y concatenamos solo una vez
	"""

	#rebanadas
	#nueva_cadena += palabra[0 : n]	

	#compresion
	#nueva_cadena += "".join([palabra[i] for i in range(n)])

	return nueva_cadena

print(filtrar_palabras("Nicolas", 2))
