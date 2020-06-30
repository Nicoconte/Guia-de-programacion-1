def discriminarDigitos(cadena):
	digitos, letras = 0, 0 

	for i in range(0, len(cadena)):
		if cadena[i].isdigit():
			digitos += 1
		else:
			letras += 1

	return letras, digitos



informe_letras, informe_digitos = discriminarDigitos("Hola 1232323")

print(f"{informe_letras} ~ {informe_digitos}")
