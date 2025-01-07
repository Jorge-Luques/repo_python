
"""
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
 * Los signos de puntuación no forman parte de la palabra.
 * Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * No se pueden utilizar funciones propias del lenguaje que
 lo resuelvan automáticamente.
 
 -> subdividir la cadena de texto en palabras
 a cada palabra sacarle los signos de puntuacion y llevarla a minusculas
 contar las palabras resultantes
"""
import re
texto = "Contar las PALABRAS que se repiten!! Si no se repiten el que tengan sera UNO. Las PalabraS que se repiten deben una forma de contar esas palabras."
texto_limpio = re.sub(r'[^\w\s]', '', texto)
plbs = texto_limpio.split()

def normalizarPalabras(p):
    txtAux = ""
    for palb in range(len(p)):
        txtAux = p[palb].lower()
        p[palb] = txtAux
        txtAux = ""


def contarPalabras(p):
    dict = {}
    for word in p:
        if not word in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
    print(dict)

normalizarPalabras(plbs)
contarPalabras(plbs)

