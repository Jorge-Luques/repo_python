
# Calculadora de interes compuesto basica
def calcular_incremento(inv, porcentaje):
    return (porcentaje/100)* inv
    
def interesCompuesto(invIni, incPorc,anos):
    if anos == 0:
        return invIni
    else:
        incremento = round(calcular_incremento(invIni,incPorc),2)
        print("el % crece: ",incremento)
        return interesCompuesto(invIni+incremento, incPorc, anos-1)
"""
version 1
inv = int(input('Ingresar la inversion inical: '))
porcentaje = float(input('Ingresar el porcentaje anual: '))
anos = int(input('Ingresar la cantidad de años a invertir: '))
"""

while True:
    try:
        inv = int(input('Ingresar la inversión inicial: '))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

while True:
    try:
        porcentaje = float(input('Ingresar el porcentaje anual: '))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingrese un número decimal válido.")

while True:
    try:
        anos = int(input('Ingresar la cantidad de años a invertir: '))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

print(f'Invirtiendo ${inv} con porcentaje de {porcentaje}% durante {anos} años..')
print('da un total de: $',round(interesCompuesto(inv,porcentaje,anos),2))

