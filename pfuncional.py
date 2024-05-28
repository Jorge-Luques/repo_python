#Estas lineas son para quitar los warning de pylint
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

#lista por comprension
listaMultX1000 = [i * 1000 for i in range(10)]
print(listaMultX1000)

listaCuadrados = [i*i for i in range(10)]
print(listaCuadrados)

#funcion con lambda
multiplicacion = lambda a, b: a*b #donde a y b son los parametros
res: int  = multiplicacion(12,37)
print("la multiplicacion da "+str(res))

def multip_rusa(x, y):
    resultado: int = 0
    while y >= 1:
        if y % 2 == 1: # si es impar sumo a
            resultado = resultado + x
            #print("res = "+ str(res))
        x = x * 2
        #print("a ="+str(a))
        y = y // 2
        #print("b ="+str(b))
    return resultado

print("Por medio de la multiplicacion rusa da: "+ str(multip_rusa(12, 37)))