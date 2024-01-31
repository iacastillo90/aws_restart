import math

def calcular_operacion_cientifica(operacion, valor1, valor2=None):
    if operacion == 'potencia':
        resultado = math.pow(valor1, valor2)
    elif operacion == 'raiz':
        resultado = math.sqrt(valor1)
    elif operacion == 'seno':
        resultado = math.sin(math.radians(valor1))
    elif operacion == 'coseno':
        resultado = math.cos(math.radians(valor1))
    elif operacion == 'tangente':
        resultado = math.tan(math.radians(valor1))
    elif operacion == 'logaritmo':
        resultado = math.log(valor1, 10)
    else:
        resultado = "Error: Operación no válida"
    
    return resultado

if __name__ == "__main__":
    print("Operaciones disponibles: potencia, raiz, seno, coseno, tangente, logaritmo")
    operacion_elegida = input("Ingrese la operacion deseada: ").lower()
    
    if operacion_elegida in ['potencia', 'raiz', 'seno', 'coseno', 'tangente', 'logaritmo']:
        valor1 = float(input("Ingrese el primer valor: "))
        
        if operacion_elegida == 'potencia' or operacion_elegida == 'logaritmo':
            valor2 = float(input("Ingrese el segundo valor: "))
            resultado_operacion = calcular_operacion_cientifica(operacion_elegida, valor1, valor2)
        else:
            resultado_operacion = calcular_operacion_cientifica(operacion_elegida, valor1)
        
        print(f"El resultado de {operacion_elegida} es: {resultado_operacion}")
    else:
        print("Operación no válida.")
