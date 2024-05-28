#Estas lineas son para quitar los warning de pylint
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

#para el warning trailing whitespaces hay que borrar los espacios antes del salto de linea
lista = []
cantidad = int(input("Ingrese la cantidad de datos de la lista -> "))

# cargo los valores a la lista
for i in range(cantidad): # es el equivalente a for(int i=0;i<cantidad;i++)
    lista.append(input("Cargar un nombre: "))
#muestro los valores de la lista por pantalla
print("Los valores de la lista son: "+ str(lista))

# Extend hace lo mismo que append pero agrega varios elementos de una a la lista
#lista.extend([1,2,3])

#se carga la posicion
pos = int(input("Ingresar la posicion de la lista donde esta el valor a modificar: "))
valor = input("Introduce el nuevo valor: ") #se carga el valor
if pos < cantidad:
    lista[pos] = valor
#se carga la posicion
pos = int(input("Ingresar la posicion de la lista donde esta el valor a modificar otra vez: "))
valor = input("Introduce el nuevo valor: ") #se carga el valor
# otra funcion equivalente a lo anterior
# tiene la particularidad de que...
# si la posicion ingresada supera a la ultima agrega igual el valor pero a la posicion final
lista.insert(pos,valor)
valor = input("Introduce el valor a eliminar: ") #se carga el valor
lista.remove(valor) #se elimina el valor de la lista, si lo encuentra
print("Los valores de la lista con los cambios son: "+ str(lista))

valor = input("Ingresa un valor a buscar: ")
estaValor = valor in lista
if estaValor:
    print(str(valor)+" se encuentra en la lista y esta en la posicion "+ str(lista.index(valor)))
else:
    print("No se encuentra el valor "+str(valor)+" en la lista")
