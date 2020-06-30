def eliminarSubcadenas(cadena, posicion, caracteres):
	
	cadena_1 = cadena[0 : posicion]
	cadena_2 = cadena[caracteres : len(cadena)]
	
	nueva_cadena = cadena_1 + cadena_2

	return nueva_cadena

def eliminarSubcadenasSinRebanadas(cadena, posicion, caracteres):

	cadena_1 = "".join([cadena[i] for i in range(0, posicion)])
	cadena_2 = "".join([cadena[i] for i in range(caracteres, len(cadena))])

	nueva_cadena = cadena_1 + cadena_2

	return nueva_cadena

c = eliminarSubcadenasSinRebanadas("Hola, soy una cadena de caracteres", 4, 9)
#c = eliminarSubcadenas("Hola, soy una cadena de caracteres", 4, 9)


