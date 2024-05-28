fichero = open("pedidosMesas.txt","r+")
nro_mesa = -1
pedido = ""
info_pedidos = dict()

for linea in fichero.readlines():
    linea = linea.replace("\n","")
    #comprobar si estamos en la linea que tiene la palabra mesa
    if "mesa" in linea.lower():
        nro_mesa = int(linea.split(" ")[1])
    elif len(linea) != 0:
        pedido = linea.replace(" y ",", ") #reemplaza el conector y por ,
        pedido = pedido.split(", ")
        info_pedidos[nro_mesa] = pedido
        
for pedido in info_pedidos:
    print ("La mesa "+str(pedido)+" ha realizado los siguientes pedidos: \n"+ str(info_pedidos[pedido]))

fichero.close()
    
#-------------- AHORA ABRIMOS EL DICCIONARIOS CON LOS PEDIDOS Y LOS PASAMOS A UN ARCHIVO NUEVO -----------

def escribirPedidos(archivo, mesa, pedidos):
    archivo.write("Mesa ")
    archivo.write(str(mesa))
    archivo.write("\n")
    #escribimos en el archivo nuevo el pedido
    for p in range(len(pedidos)):
        #escribimos el pedido de la pos p
        archivo.write(pedidos[p])
        #miramos si el sig pedido es el ultimo
        if p == len(pedidos) - 2:
            archivo.write(" y ")
        elif p < len(pedidos) -2:  
            archivo.write(", ")
    archivo.write("\n")
    archivo.write("\n")

ficheroNuevo = open("pedidosFinal.txt","w+")
for mesa in info_pedidos:
    escribirPedidos(ficheroNuevo, mesa, info_pedidos[mesa])

ficheroNuevo.close()


