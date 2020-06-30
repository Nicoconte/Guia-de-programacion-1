def extraerSubcadenaConRebanada(cadena, indice):
	subcadena = cadena[indice : len(cadena)]
	return subcadena, len(subcadena)

def extraerSubcadenaSinRebanadas(cadena, indice):
	subcadena = ""
	long = 0

	for i in range(indice, len(cadena)):
		subcadena += cadena[i]
		long = i

	return subcadena, long

def main():
	#cadena_nueva, longitud_cadena = extraerSubcadenaConRebanada("Esto es una cadena", 2)
	
	cadena_nueva, longitud_cadena = extraerSubcadenaSinRebanadas("Esto es una cadena", 2)
	
	print(f"Cadena nueva {cadena_nueva} y su longitud es {longitud_cadena}")

main()