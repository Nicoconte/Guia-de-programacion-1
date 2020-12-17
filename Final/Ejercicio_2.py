def encontrar_raiz(numero_min, numero_max, numero):

    if (numero_min <= numero_max) : 
        medio = (numero_min + numero_max) // 2
        
        if ((medio * medio <= numero) and ((medio + 1) * (medio + 1) > numero)): 
            return medio

        elif (medio * medio < numero):
            return encontrar_raiz(medio + 1, numero_max, numero)

        else: 
            return encontrar_raiz(numero_min, medio - 1, numero)

    return numero_min

def main():
    numero = 16
    print(f" Raiz => {encontrar_raiz(0, numero, numero)}")

if __name__ == "__main__":
    main()