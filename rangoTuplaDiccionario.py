"""La función range() devuelve genera una secuencia de números, 
comenzando desde el límite inferior hasta el límite superior.

range (límite_inferior, límite_superior, tamaño_paso)

límite_inferior: El valor inicial de la lista.
límite_superior: El valor máximo de la lista, excluyendo este número.
tamaño_paso: El tamaño del paso, la diferencia entre cada número en la lista.
"""
print(list(range(1,5)))

"""La estructura de datos de tupla se utiliza para almacenar un grupo de datos. 
Los elementos de este grupo están separados por una coma. 
Una vez creada, los valores de una tupla no pueden cambiar. 

nombreTupla(elem1,elem2,...)
"""
personInfo = ( "Diana" , 32 , "Nueva York" )
print(personInfo)
print(personInfo[0])
print(personInfo[1])
print(personInfo[2])

"""Se puede pensar en un diccionario como un conjunto desordenado de pares clave:valor .
Un par de llaves crea un diccionario vacío: {} . Cada elemento puede asignarse a un cierto valor. 
Se puede utilizar un número entero o una cadena para el índice. Los diccionarios no tienen un orden.

nombreDiccionario = {}
nombreDiccionario[clave] = valor
"""

words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
words["Mr"] = "Monsieur"

print(words)
print(words["Hello"])
print(words["No"])       # si no encuentra tira excepcion KeyError
print(words.get("Bye"))  # si no encuentra retorna None
del words["Mr"]
for k in words.keys():
    print(f'Translate: {k}: {words[k]}')

for value in words.values():
    print(f'French: {value}')
#print(words)

planet = {
    'name': 'Mars',
    'moons': 2
}

planet['circumference (km)'] = { #diccionario dentro de un diccionario
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has {planet["moons"]} moons and a polar circumference of {planet["circumference (km)"]["polar"]}')