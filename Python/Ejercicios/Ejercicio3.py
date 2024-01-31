def dibujar_rombo(numero):
    for i in range(1, numero + 1):
        print(" " * (numero - i) + "*" * i)
    
    for i in range(numero - 1, 0, -1):
        print(" " * (numero - i) + "*" * i)

if __name__ == "__main__":
    numero_ingresado = int(input("Ingresa un número para el rombo: "))
    dibujar_rombo(numero_ingresado)
