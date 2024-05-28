def presentacion():
    input("Programa hecho con funciones")
    input("----------------------------")

"""def cargarDatos():
    global valor1
    global valor2"""
    

def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def resta():
    resultado = valor1 - valor2
    strResta = "El resultado de la resta entre {0} y {1} es: {2}"
    input(strResta.format(valor1,valor2,resultado))

def funcConParametrosArbitrarios(v1, v2, *lista):
    suma = v1 + v2
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma


# declaracion del programa main
presentacion()
valor1 = int(input("Ingresar el primer valor: "))
valor2 = int(input("Ingresar el segundo valor: "))
input("El resultado de la suma es: "+ str(suma(valor1,valor2)))
resta()
input("suma con 2 parametros "+ str(funcConParametrosArbitrarios(10,24)))
input("suma con 3 parametros "+ str(funcConParametrosArbitrarios(1,2,3)))
input("suma con 8 parametros "+ str(funcConParametrosArbitrarios(1,2,3,4,5,6,7,8)))