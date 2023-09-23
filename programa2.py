import sys

def calcular_suma(valores):
    return sum(valores)

def calcular_promedio(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

if NameError == "_main_":
    # Obtener los argumentos de la línea de comandos, excluyendo el nombre del programa
    argumentos = sys.argv[1:]
    
    # Convertir los argumentos en una lista de valores enteros
    valores = [int(valor) for valor in argumentos[0].split(",")]

    # Calcular la suma y el promedio
    suma = calcular_suma(valores)
    promedio = calcular_promedio(valores)

    # Mostrar el resultado
    print(f"La suma es {suma} y el promedio es {promedio}")