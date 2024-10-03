inventario = {'manzanas': 430, 'bananas': 312,'naranjas': 525, 'peras': 217}

print(inventario.keys())
print(inventario.values())
print(inventario.items())
print(inventario.get("manzanas"))

anteriores = {0:1, 1:1}
def fibonacci(n):
    if anteriores.__contains__(n):
        return anteriores[n]
    else:
        nuevoValor = fibonacci(n-1) + fibonacci(n-2)
        anteriores[n] = nuevoValor
        return nuevoValor
"""
print(fibonacci(40))
print(anteriores)
"""
cuentaLetras = {}
for letra in "Mississippi":
    cuentaLetras[letra] = cuentaLetras.get (letra, 0) + 1

itemsLetras = list(cuentaLetras.items())
itemsLetras.sort()
print(itemsLetras)
