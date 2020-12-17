
def obtener_registro(ruta="aeropuertos.txt"):
    archivo = None  
    registro = []

    try:
        archivo = open(f"{ruta}", mode="r+", encoding="utf8")

        for linea in archivo:
            registro.append(linea.strip("\n").split(";"))

    except:
        print(f"No se pudo abrir el archivo {archivo}")

    finally:
        if archivo != None:
            archivo.close()

    return registro

def obtener_provincias_argentinas(registros):
    ubicaciones = []

    for registro in registros:
        if registro[3].count("Argentina") >= 1:
            ubicaciones.append(registro[3].split(","))
    
    return ubicaciones

def armar_listado_aeropuertos_argentinos(ubicaciones):
    listado = {}

    for ubicacion in ubicaciones:
        listado.update(dict([(ubicacion[1], [])]))

    return listado

def filtrar_aeropuertos_argentinos(registros):
    
    aeropuertos_argentinos = []

    for registro in registros:
        if registro[3].count("Argentina") >= 1:
            aeropuertos_argentinos.append(registro)
    
    return aeropuertos_argentinos

def actualizar_listado_aeropuertos_argentinos(aeropuertos, listado):
    
    clave = None

    for aeropuerto in aeropuertos:
        clave = aeropuerto[3].split(",")[1]
        if clave in listado:
            listado[clave].append([aeropuerto[0], aeropuerto[1], aeropuerto[2]])
        
    return listado


def imprimir_listado(listado):
    for clave in listado:
        for provincia in listado[clave]:
            print(f"{provincia[0]}  {provincia[1]}  {provincia[2]} {clave}")
        print(f"TOTAL DE AEROPUERTOS EN {clave}: {len(listado[clave])} \n")


def crear_archivo_aeropuertos_internacionales(registros):
    archivo = None

    try:
        archivo = open("aeropuertos_internacionales.txt", mode="w+", encoding="utf8")

        for registro in registros:
            if registro.count("") == 0:
                archivo.write(f"{';'.join(registro)} \n")

    except:
        print(f"No se pudo crear el archivo {archivo}")

    finally:
        if archivo != None:
            archivo.close()


def main():
    registros = obtener_registro()
    ubicaciones = obtener_provincias_argentinas(registros)
    listado = armar_listado_aeropuertos_argentinos(ubicaciones)
    aeropuertos = filtrar_aeropuertos_argentinos(registros)
    actualizar_listado_aeropuertos_argentinos(aeropuertos, listado)

    imprimir_listado(listado)
    crear_archivo_aeropuertos_internacionales(registros)

if __name__ == "__main__":
    main()