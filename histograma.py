
tupla = ('a', 'b', 'c', 'd', 'e')
tupla2 = (1,2,6,4.8,16)
print ("t1 en main ",tupla)
print ("t2 en main",tupla2)
"""
print (type(tupla))
t1 = (2,3,11)
print(type(t1))
t2 = ('b')
print(type(t2))
print(tupla[2:])
t1, t2 = t2, t1
print(t1, t2)

def intercambio(t1, t2):
    print("t1 en func ",t1)
    print("t2 en func",t2)
    return t2, t1

tupla, tupla2 = intercambio(tupla, tupla2)
print("t1 pos intcb ",tupla)
print("t2 pos intcb ",tupla2)
"""
import random
# aleatorios en el balde
def listaAleatorios(n):
    s = [0] * n #inicializa la lista
    for i in range(n):
        s[i] = random.random()
    return s
"""
def enElBalde(lista, minimo, maximo):
    cuenta = 0
    for num in lista:
        if minimo < num < maximo:
            cuenta = cuenta + 1
    return cuenta

#reparticion de baldes
numBaldes = 8

anchuraBalde = 1.0 / numBaldes
for i in range(numBaldes):
    minimo = i * anchuraBalde
    maximo = minimo + anchuraBalde
    print (minimo, "hasta", maximo)

lista = listaAleatorios(1000)
baldes = [0] * numBaldes
anchuraBalde = 1.0 / numBaldes
for i in range(numBaldes):
    minimo = i * anchuraBalde
    maximo = minimo + anchuraBalde
    baldes[i] = enElBalde(lista, minimo, maximo)
print (baldes)

baldes = [0] * numBaldes
for i in lista:
    indice = int(i * numBaldes)
    baldes[indice] = baldes[indice] + 1
print(baldes)
"""

def histograma(lista, numBaldes):
    baldes = [0] * numBaldes
    for i in lista:
        indice = int(i * numBaldes)
        baldes[indice] = baldes[indice] + 1
    return baldes

lis = listaAleatorios(100)
numBaldes = 5
print(histograma(lis,numBaldes))
