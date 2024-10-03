
# Online Python - IDE, Editor, Compiler, Interpreter
#------- el metodo Divide y Conquista o incremental en su maxima expresion!!!

# objetivo: funcion distancia = distancia =math.srt((x2 - x1)**2 + (y2 - y1)**2)
import math
# paso 1: bosquejo de funcion
"""
def distancia(x1, y1, x2, y2):
    return 0.0
// salida: la distancia es: 0.0

# paso 2: hacer las restas
def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print ("dx es", dx)
    print ("dy es", dy)
    return 0.0
// salida: dx es 3, dy es 4, la distancia es: 0.0

# paso 3: calcular suma de cuadrados
def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dalcuadrado = dx**2 + dy**2
    print ("dalcuadrado es: ", dalcuadrado)
    return 0.0
// salida: dalcuadrado es: 25, la distancia es: 0.0
"""
# paso 4: funcion completa
def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dalcuadrado = dx**2 + dy**2
    resultado = math.sqrt(dalcuadrado)
    return resultado

print("la distancia es: ",distancia(1,2,4,6))