#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuacion preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta informacion en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el codigo, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco mas del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su aÃ±o de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#Â¿Como lo haremos?, usaremos una variable para guardar el resultado del calculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuacion le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta informacion para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos sera escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambien estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de lÃ­nea que ocurran en el codigo se consideraran como parte del string.
# Si no estas convencido, prueba el funcionamiento reemplazando los delimitadores por "

import datetime

def versionAnt():
    print("Bienvenido a ... ")
    print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

    """)
    #Primera interaccion. Solicitamos al usuario que ingrese su nombre,
    # y lo guardamos en una variable de tipo str
    nombre = input("Para empezar, dime como te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()

    #Segunda interaccion. Solicitamos el ingreso del aÃ±o, y utilizamos este
    #dato para estimar la edad de la persona. Â¿Por que decimos que solo estamos "estimando" su edad?
    #Â¿Que ocurre si eliminamos la conversion a tipo de dato 'int' de la siguiente lÃ­nea?
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    anyo_actual = datetime.datetime.now().year
    edad = anyo_actual-agno-1
    print()
    
    #Tercera interaccion. Solicitamos la estatura, medida en metros.
    #Utilizamos la conversion a 'int', y una expresion para convertir esto
    #a una medida en metros y centÃ­metros
    estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. Â¿Cuanto mides? DÃ­melo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    
    #Cuarta interaccion. Consultamos cuantos amigos tiene el usuario.
    num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))

    #Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
    print()
    print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")
    print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
    print()

    #Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
    mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")


    #Ahora puedes practicar solicitando mas datos al usuario. Solo tienes que usar apropiadamente input() y print()
    #1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
    #   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrÃ­belos en pantalla
    #   utilizando print. Puedes agregar todas las lÃ­neas que necesites.
    sexo = input("Ingresa el genero con el que defines: ").lower()
    city = input("Ingresa la ciudad donde naciste: ")
    pais = input("Ingresa a que pais a la que pertenece (tu nacionalidad nativa): ")
    dire = input("Ingresa tu direccion: ")
    print("--------------------------------------------------")
    print("Tu sexo es: ",sexo)
    print("Naciste en la ciudad de ",city)
    print("Tu pais natal es ",pais)
    print("Y tu direccion es: ",dire)
    print("--------------------------------------------------")
    #Usaremos una variable bool para indicar si el usuario desea continuar
    #utilizando el programa o no
    #continuar = True
    modif = False
    #Este ciclo se mantiene en ejecucion hasta que el usuario desee salir


    #Solicitamos opcio³n al usuario
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    while escribir_mensaje != "N" and escribir_mensaje != "n":
        mensaje = input("¿Que desesa escribir hoy?: ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
        perfil = str(input("¿Deseas modificar tus datos personales? (S/N) "))
        if perfil == "S" or perfil == "s":
            modif = True
            print("¿Que dato deseas modificar?")
            print("1. Nombre")
            print("2. Cantidad de amigos")
            print("3. Año de nacimiento")
            print("4. Sexo")
            print("5. Ciudad de nacimiento")
            print("6. Pais de nacimiento")
            print("7. Direccion")
            print("8. Salir")
            dato = int(input("Ingresa el numero del dato que deseas modificar: "))
            if dato == 1:
                nombre = input("Ingresa tu nuevo nombre: ")
            elif dato == 2:
                amigos = int(input("Ingresa la cantidad de amigos que deseas tener: "))
                while amigos < 0:
                    amigos = int(input("La cantidad de amigos no puede ser negativa. Ingresa la cantidad: "))
            elif dato == 3:
                agno = int(input("Ingresa tu nuevo año de nacimiento: "))
            elif dato == 4:
                sexo = input("Ingresa tu nuevo genero: ")
            elif dato == 5:
                city = input("Ingresa tu nueva ciudad de nacimiento: ")
            elif dato == 6:
                pais = input("Ingresa tu nuevo pais de nacimiento: ")
            elif dato == 7:
                dire = input("Ingresa tu nueva direccion: ")
            elif dato == 8:
                print("Hasta luego!")
            else:
                print("opcion incorrecta!!!")
        #Si el usuario desea escribir un mensaje, solicitamos el mensaje
        escribir_mensaje = str(input("¿Deseas escribir un nuevo mensaje? (S/N) "))
        
"""             
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteracion el ciclo terminara
    else:
        continuar = False"""

    #Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la accion de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mas acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafÃ­os:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opcion al usuario.
#
#2. Modifica este menÃº para que le permita el usuario realizar mas de una accion.
#   Por ejemplo, puedes agregar una accion que permita al usuario modificar su nombre.

#VERSION MODULARIZADA

#Vamos a modificar el codigo que acabamos de ver para encapsular algunas partes de el
#en funciones.

#En particular haremos esto con:
#1. El mensaje de bienvenida
#2. El codigo para solicitar datos al usuario.
#3. El codigo para mostrar el perfil del usuario
#4. El codigo para mostrar un mensaje en pantalla

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    return 2024-agno-1

def obtener_estatura(estatura):
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return metros, centimetros

def obtenerGenero():
    sexo = input("Ingresa el genero con el que defines: ").lower()
    print(" hombre - mujer - otro - lgtb")
    while sexo not in ["hombre", "mujer", "otro", "lgtb"]:
        sexo = input("Ingresa el genero con el que defines: ").lower()
    return sexo

def obtener_paisNacimiento():
    pais = input("Ingresa el pais de nacimiento: ").lower()
    return pais

#Ahora vamos a crear una funcion que permita al usuario realizar acciones
def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
    return amigos

def mostrar_perfil(nombre, edad, estatura, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "aÃ±os")
    print("Estatura: ", obtener_estatura(estatura)[0], "m y ", obtener_estatura(estatura)[1], "centi­metros")
    print("Genero:   ", obtenerGenero())
    print("Pais de nacimiento: ", obtener_paisNacimiento())
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje pÃºblico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opcion: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opcion que has ingresado. Intentalo otra vez.")
        opcion = int(input("Ingresa una opcion: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. Â¿Que piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

############################################################
# El codigo anterior era solamente definicion de funciones que seran usadas mas adelante
# Ahora empieza el programa principal.

mostrar_bienvenida()
nombre = obtener_nombre()
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
edad = obtener_edad()
estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
num_amigos = obtener_num_amigos()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(nombre, edad, estatura, num_amigos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi Red")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    # Mostramos el menu
    opcion = opcion_menu()

    #Codigo para la opcion 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = obtener_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    #Codigo para la opcion 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    #Codigo para la opcion 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura, num_amigos)

    #Codigo para la opcion 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        num_amigos = obtener_num_amigos()
        mostrar_perfil(nombre, edad, estatura, num_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi Red. ¡Hasta pronto!")

#Como puedes ver, una vez que no hay mas definiciones de funciones, el programa principal empieza.
#Si lo lees, podras ver que es mucho mas corto, y que hay menos codigo repetido que en la version anterior.

#Te proponemos como desafÃ­o:
#1. Agrega el atributos como "sexo" y "pais de nacimiento"
#   a los datos que se le piden al usuario, y permite que sean solicitados y leÃ­dos usando funciones.
#   Tendras que identificar en que partes del codigo debes hacer esa modificacion.