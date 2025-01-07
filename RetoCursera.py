
# escriba una función de nombre mcd que reciba dos números n1 y n2 como argumentos,
# y retorne el máximo común divisor. Por ejemplo para los argumentos 10 y 15 debe retornar 5
def mcd(n1, n2):
    maxcodi = 0
    for i in range(min(n1,n2) +1):
        if i > 0:
            if (n1 % i) == 0 and (n2 % i) == 0:
                maxcodi = i
    return maxcodi
# Escribe una función exponente, que dado un número n, retorne el exponente de dicha potencia de 2 más grande. 
# Por ejemplo, si el número es 65, tu programa debe retornar 6, ya que 2⁶  = 64.
def exponente(n):
    import math
    return int(math.log2(n))

# Los números pandigitales son aquellos que contienen todos los dígitos del 0 al 9 al menos una vez, como el 1023478695. 
# Escribe una función panprimo que determine si un número n es pandigital y si al mismo tiempo, 
# sus últimos 3 dígitos conforman un número primo, retornando True o False según corresponda
def panprimo(n):
    numText = str(n)
    for i in range(10):
        if str(i) not in numText:
            return False
    
    ult3 = n % 1000
    for j in range((ult3//2)+1):
        if j > 1:
            if ult3 % j == 0:
                return False
    return True

tablero = [ 1,3,2,1,4,2,1,3,5,7,1 ]

# Escriba una función de nombre promedio_std(). La función debe recibir una lista de números llamada lista, 
# y debe retornar retornar el promedio de ellos, junto con su desviación estándar.
def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista)/len(lista)
    sumaCuad = 0
    for i in range(len(lista)):
        sumaCuad += (lista[i] - x)** 2
    y = (sumaCuad/(len(lista)-1)) ** 0.5
    return (x,y)

print(promedio_std(tablero))


# Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: azul, rojo, verde y amarillo. 
# Desea saber cual de esos colores es el que más se repite. Escriba una función color_frecuente que reciba como argumento
# a una lista de strings llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.
#En caso de que haya varios colores con el máximo número, se retornará con la siguiente prioridad: azul, rojo, verde, amarillo.
colores = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']

def color_frecuente(lista):
    color = lista[0]
    frec = 0
    frecMay = lista.count(color)
    for i in range(len(lista)):
        frec = lista.count(lista[i])
        if frec > frecMay:
            color = lista[i]
            frecMay = frec
        elif frec == frecMay:
            if lista[i] != color:
                if lista[i] == "azul":
                    color = lista[i]
                elif lista[i] == "rojo" and color != "azul":
                    color = lista[i]
                elif lista[i] == "verde" and color != "azul" and color != "rojo":
                    color = lista[i]
    return (color, frecMay)

print(color_frecuente(colores))

# Un uso muy común de las listas es el de representar tableros con ellas. Para eso se utilizan listas de listas, 
# de este modo, se puede entender una lista de listas como una matriz. 
# Así, para acceder a un elemento i,j de la matriz, se debe acceder a: matriz[i][j].
# El objetivo de este ejercicio, es que programes una función buscaminas que reciba como argumento
# a una matriz tablero y dos coordenadas i, j, y que entregue la cantidad de bombas 'X' que rodean a esa posición.

tabla = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]

def buscaminas(tablero, i, j):
    cuentaMinas = 0
    # Definir las posiciones relativas de las celdas vecinas
    direcciones = [(-1, -1), (-1, 0), (-1, 1), 
                   (0, -1),          (0, 1), 
                   (1, -1), (1, 0), (1, 1)]
    
    # Iterar sobre cada dirección
    for di, dj in direcciones:
        ni, nj = i + di, j + dj  # Nueva posición
        # Verificar si la nueva posición está dentro de los límites del tablero
        if 0 <= ni < len(tablero) and 0 <= nj < len(tablero[0]):
            if tablero[ni][nj] == "X":  # Verificar si hay una mina
                cuentaMinas += 1

    return cuentaMinas
    
print(buscaminas(tabla, 1, 1))