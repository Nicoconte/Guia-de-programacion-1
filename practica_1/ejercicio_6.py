"""
Entrada => 2 numeros enteros

Proceso => Concatener ambos numeros y devolverlo como uno solo

Salida => Un solo numero

"""

def concatenar_valores(n,n2):
	respuesta = str(n)+str(n2)
	return respuesta

num = int(input("Primer numero "))
num2 = int(input("Segundo numer "))

print(concatenar_valores(num,num2))