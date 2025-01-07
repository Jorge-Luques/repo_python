"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizzbuzz(cant):
    for i in range(1,cant+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i,"fizzbuzz")
        elif i % 3 == 0:
            print(i,"fizz")
        elif i % 5 == 0:
            print(i,"buzz")

#fizzbuzz(100)
#--------------------------------------
"""
Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
     las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def sonAnagramas(pal1,pal2):
    
    if pal1 == pal2:
        return False
    else:
        if len(pal1) != len(pal2):
           return False
        else:
            aux = [char for char in pal1]
            aux = sorted(aux) #se usa la funcion sorted para ordenar la lista
            aux2 = [char for char in pal2]
            aux2 = sorted(aux2) #de usar la funcion .sort ordena la lista pero retorna None (no se puede seguir usando)
            for letra in range(len(aux2)):
                if aux2[letra] != aux[letra]:
                    return False
    return True
            

if sonAnagramas("pal1","pla1"):
    print("siii")
else:
    print("Naaaa")