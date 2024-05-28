def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano:")
        ing=input("Ingrese palabra en ingles:")
        diccionario[caste]=ing
        continua=input("Quiere cargar otra palabra:[s/n]")
    return diccionario


def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])


def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en castellano a consultar:")
    if pal in diccionario:
            print("En ingles significa:",diccionario[pal])


# bloque principal

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)

# mirar explicación en el apartado 34 de python ya ejercicio último