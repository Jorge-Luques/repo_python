i = 1
promedio = 0
suma = 0
CANTIDAD = 3
while i <= CANTIDAD:
    valor = int(input("Ingrese un valor: "))
    suma += valor
    i = i+1
promedio = suma / CANTIDAD
print("El promedio es: "+ str(promedio))

#ejemplo con for
for x in range(5, 10):
    print("x vale "+ str(x))
