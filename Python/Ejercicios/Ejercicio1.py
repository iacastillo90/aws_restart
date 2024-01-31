def obtener_datos():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")

    return nombre, apellido, edad

def imprimir_datos(nombre, apellido, edad):
    print("Datos ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")

if __name__ == "__main__":
    nombre, apellido, edad = obtener_datos()
    imprimir_datos(nombre, apellido, edad)
