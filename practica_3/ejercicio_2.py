def crearmatriz():
    
    dato1 = int(input("Por favor ingrese el tamaño de la fila en la matriz "))
    dato2 = int(input("Por favor ingrese el tamaño de la columna en la matriz "))
    matriz = []
    for i in range(dato1):
        #multiplico la cantidad la longitud de data1(fila) por datos2(columnas)
        matriz.append([0] * dato2) 
    return matriz

def rellenarmatriz():
    matriz = crearmatriz()
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        impar = -1
        for c in range(columna):
            impar += 2
            print(f," => ",c) 
            if f == c:
                n = impar
            else:
                n = 0
            matriz[f][c] = n
    return matriz

def imprimirmatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
def main():
    imprimirmatriz(rellenarmatriz())

main()