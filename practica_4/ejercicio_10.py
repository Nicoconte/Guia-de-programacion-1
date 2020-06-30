def reemplazarApariciones(cadena, palabra_a_reemplazar, palabra):
	cadena_en_lista = cadena.split()
	nueva_cadena = ""

	aparaciones = 0

	for i in cadena_en_lista:
		
		if palabra_a_reemplazar == i:
			aparaciones += 1
		
		nueva_cadena += " " + i.replace(palabra_a_reemplazar, palabra)

	return nueva_cadena, aparaciones

cadena, informe_aparaciones = reemplazarApariciones('Es prueba una cadena de prueba de cadena', 'prueba', '-')

print(f"Cadena => {cadena} | Aparaciones => {informe_aparaciones}")
