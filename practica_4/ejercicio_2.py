clave_entrante = int(input("Ingrese una clave "))

clave_maestra = str(clave_entrante)
clave_1, clave_2 = "", ""

"""
for i in range(len(clave_maestra)):
	if i % 2 == 0:
		clave_1 += clave_maestra[i]
	else:
		clave_2 += clave_maestra[i]
"""

clave_1 = clave_maestra[0 : len(clave_maestra) : 2]
clave_2 = clave_maestra[1 : len(clave_maestra) : 2]

print(f"Clave 1 = {clave_1} | Clave 2 = {clave_2}") 