def invertirCadena(cad):
    return (cad[::-1])

def primerPalabra(cad: str):
    """fp = ""
    i = 0
    while i < len(cad):
        fp = fp + cad[i]
        if cad[i+1] < len(cad) and cad[i+1] == " ":
            break
        i = i+1
    return fp
"""
    salida = cad.split()
    return salida[0]

def primerPalabra2(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text

def between_markers(text: str, start: str, end: str) -> str:
    ini = text.index(start) #obtenemos la posición del carácter start
    fin = text.index(end) #obtenemos la posición del carácter end
    subcadena = text[ini+1:fin]
    return subcadena
    #la forma simplificada es: return text[text.index(start)+1:text.index(end)]

""" en la funcion primerPalabra2 vemos que usamos find para que devuelva una posicion
 a la variable index mientras en la funcion between_markers utilizamos la funcion index para
 sea guardada en las variables ini y fin.
 LA PRINCIPAL DIFERENCIA entre ambas funciones de string es que find si no encuentra la posicion
 en la que deberia estar la subcadena o el caracter a buscar retorna -1
 en cambio, para la misma situacion, la funcion index retorna error """

texto = input("ingresar texto: ")
print("Todas la palabras con mayusculas, uso .title(): "+ texto.title())
print("Todas las repeticiones de una palabra, uso .count('palabra'): "+ str(texto.count("palabra")))
print("Quedo: "+invertirCadena(texto))
print("la primera palabra es: "+ primerPalabra2(texto))
cad = "What is >apple<"
start = ">"
end = "<"
print("la subcadena palabra entre {} y {} es: {}".format(start,end,between_markers(cad,start,end)))
# con el método .isnumeric(), o .isdecimal() se puede buscar cadenas que parezcan decimales.
# "-70".isnumeric() devolverá False.
#  Esto se debe a que todos los caracteres de la cadena tendrían que ser numéricos y el guión (-) no lo es
alfanum = input("introducir texto que contenga numeros: ")
for item in alfanum.split():
   if item.isnumeric():
       print(item)