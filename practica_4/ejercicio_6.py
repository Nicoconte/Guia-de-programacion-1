def ordenarPalabras(cadena):
	cadena_ordenada = " ".join(sorted(cadena.lower().replace("  "," ").split(" ")))
	return cadena_ordenada

print(f"{ordenarPalabras('Esta es una cadena que no tiene sentido alguno')}")

