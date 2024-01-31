def calcular_operacion(operacion, valor1, valor2):
    if operacion == 'suma':
        resultado = valor1 + valor2
    elif operacion == 'resta':
        resultado = valor1 - valor2
    elif operacion == 'multiplicacion':
        resultado = valor1 * valor2
    elif operacion == 'division':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            resultado = "Error: No se puede dividir por cero"
    else:
        resultado = "Error: Operación no válida"
    
    return resultado

if __name__ == "__main__":
    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    operacion_elegida = input("Ingrese la operacion deseada: ").lower()
    
    if operacion_elegida in ['suma', 'resta', 'multiplicacion', 'division']:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        
        resultado_operacion = calcular_operacion(operacion_elegida, valor1, valor2)
        print(f"El resultado de {operacion_elegida} es: {resultado_operacion}")
    else:
        print("Operación no válida.")
