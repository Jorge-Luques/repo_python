import math as ma
import re
def number_length(value: int) -> int:
    if value == 0:
        cant = 1
    else :
        cant = ma.log10(value)
        print("cant es "+ str(cant))
        pDec, pEnt = ma.modf(cant) # FUNCION que separa en la parte decimal de la parte entera
        print("pDec es "+ str(pDec))
        print("pEnt es "+ str(pEnt))
        cant = int(pEnt + 1)
    return cant

def is_acceptable_password(password: str) -> bool:
    acep = False
    if len(password) > 6:
        expRegDig = r"[a-zA-Z]\d+" 
        hayDig = re.search(expRegDig, password)
        if hayDig :
            acep = True
    return acep
    #------ Forma sencilla de hacer lo mismo
    # return len(password) > 6 and any(i.isdigit() for i in password)

def max_digit(value: int) -> int:
    # Convertir el número en una cadena de texto
    cadInt = str(value)
    max: int
    max = -60000
    for i in cadInt:
        i = int(i) #reconvierto el digito de la cadena en entero
        if i > max:
            max = i
    return max

def sum_numbers(text: str) -> int:
    # your code here
    sum = 0
    lis = text.split()
    for i in lis:
        if i.isnumeric():
            i = int(i)
            sum += i
    return sum

valor = int(input("Ingresar numero: "))
print(" El numero {} tiene {} cifras".format(valor,number_length(valor)))
print("El digito mayor es: "+ str(max_digit(valor)))
pwd = input("Ingresar contraseña: ")
if is_acceptable_password(pwd):
    print("contraseña aceptada")
else:
    print("la contraseña es muy corta o no contiene numeros")
texto = ("ingresar un texto que contenga numeros: ")
print("La suma de los digitos del texto es de : "+ str(sum_numbers(texto)))
