def obtenerUltimosCaracteres(cadena, caracteres):
	nueva_cadena = "".join([cadena[i] for i in range(len(cadena) - caracteres, len(cadena))])
	return nueva_cadena

print(f"{obtenerUltimosCaracteres('Esto es una cadena', 6)}")