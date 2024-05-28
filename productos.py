print ("CARGA DE PRODUCTOS Y VER SI HAY DESCUENTO")
# Comentario para aclarar que se solicitan datos por pantalla
nombre1 = input("ingrese el nombre del producto ")
precio1 = int(input("inrese el valor del precio $"))
nombre2 = input("ingrese el nombre del producto ")
precio2 = int(input("inrese el valor del precio $"))

#creo unas constantes
PRECIO_MAX = 1000
DESCUENTO = 25
ahorro = 0
total = precio1 + precio2
if (total > PRECIO_MAX and nombre1 != nombre2):
    ahorro = total * (DESCUENTO/100)
    total -= ahorro

print("El producto "+ nombre1 +" tiene "+str(len(nombre1))+" letras \n")
cadena = ("Se compraron los productos {0} y {1} ")
print(cadena.format(nombre1,nombre2))
print("Se ahorro en la compra "+ str(ahorro))
print("SE ABONO $"+ str(total))