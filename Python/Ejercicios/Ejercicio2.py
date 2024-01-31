def calcular_longitud_cadena(frase):
    return len(frase)

if __name__ == "__main__":
    cadena_usuario = input("Ingresa una frase: ")
    resultado_contador = calcular_longitud_cadena(cadena_usuario)
    print(f"El número de caracteres en la frase es: {resultado_contador}")
