def obtenerCadenaNueva(cadena):
	
	cadena_en_lista = cadena.split()

	primera_letra = ""
	resto_de_cadena = ""
	cadena_resultante = ""

	for n in cadena_en_lista:

		primera_letra = n[0 : 1 : 1].upper()	
		resto_de_cadena = n[1 : len(n) : 1]

		cadena_resultante += " "+ primera_letra + resto_de_cadena

	return cadena_resultante.replace(" ","")

print(f"{obtenerCadenaNueva('esta es una cadena de prueba que no tiene sentido alguno')}")