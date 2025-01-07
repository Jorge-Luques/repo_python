
#Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 
#que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.
def mezclador(string_a, string_b):
    # Asegurarse de que ambas cadenas tengan al menos 2 caracteres
    if len(string_a) < 2 or len(string_b) < 2:
        return "Ambas cadenas deben tener al menos 2 caracteres."
    resultado = string_a[:2] + string_b[-2:]
    return resultado

#Escriba una función que reciba dos strings como parámetros y retorne un nuevo string 
#que consista del primero, pero con el segundo string intercalado entre cada letra del primero.

def intercalar(string_a, string_b):
    resultado = ""
    for i in range(len(string_a)):
        resultado += string_a[i] + string_b
    return resultado

#Escriba una función que reciba un string consistente de unos y ceros 
#y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
def ocurrencias(string):
    cont1s = 0
    cont0s = 0
    for i in range(len(string)):
        if string[i] == "1":
            cont1s += 1
        else:
            cont0s += 1
    return cont1s - cont0s

#Escriba una función que reciba un string s y un número n como parámetros
#y retorne el mismo string s pero sin el elemento en el índice n.
def remover_enesimo(s, n):
    if n in range(len(s)):
        if n == 0:
            resultado = s[1:]  # Eliminar el primer carácter
        elif n == (len(s) - 1):
            resultado = s[:-1]  # Eliminar el último carácter
        else:
            resultado = s[:n] + s[n+1:]  # Eliminar el carácter en la posición n
    else:
        return s  # Si n está fuera de rango, devolver la cadena original
    return resultado

#Escriba una función que reciba un string como parámetro y retorne el string, 
#pero con cada elemento que estuviese en mayúsculas reemplazado por "$"
def reemplazo(string):
    resultado = ""
    for i in range(len(string)):
        if s[i].isupper():
            resultado += "$"
        else:
            resultado += string[i]
    return resultado

print(mezclador("familia","sentarse"))
print(intercalar("paz","so"))
print("resta de 1s y 0s da ",ocurrencias("10100101"))
print(remover_enesimo("hasta luego",10))
print(reemplazo("Vamos CarAjo"))