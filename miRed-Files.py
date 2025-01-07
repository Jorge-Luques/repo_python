#Hola.
#Hasta ahora nuestra red social incluye estas caracterÃ­sticas:

#El programa de la semana anterior permitÃ­a:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#4. Modificar el perfil del usuario
#
#Y ademÃ¡s algunas de estas funcionalidades estÃ¡n encapsulados en un mÃ³dulo, de manera
#que tu cÃ³digo principal es cada vez mÃ¡s corto y puedes concentrarte en la funcionalidad principal.

#Vamos por la siguiente evoluciÃ³n de nuestra red social.

#HabrÃ¡s notado que cada vez que ejecutamos nuestro programa de red social, debemos ingresar
#todos los datos del usuario que estÃ¡ utilizando el programa, antes de poder alcanzar
#el menÃº de opciones. Esto es bastante engorroso.

#Sin embargo, ahora sabemos que podemos utilizar memoria secundaria de nuestro computador,
#esto es, espacio del disco, para guardar archivos. Vamos a usar esto para que nuestro
#programa pueda recordar los datos de los usuarios, y evitar tener que escribirlos en cada ocasiÃ³n.

#Y la estrategia que usaremos es la siguiente.
#Cada vez que un usuario nuevo utilice nuestro programa, vamos a guardar un archivo con sus datos.
#El nombre de este archivo serÃ¡ el nombre del usuario, seguido de la extensiÃ³n '.user'.
#En este archivo guardaremos una lÃ­nea por cada variable importante de nuestro usuario.

#De esta manera, la prÃ³xima vez que ejecutemos nuestro programa, lo primero que haremos serÃ¡ preguntar
#el nombre del usuario, y ver si existe un archivo con ese nombre.
#Si existe, entonces lo leemos desde el disco, y evitamos tener que preguntar todos sus datos.
#Si no existe, entonces seguimos comportÃ¡ndonos como antes, lo tratamos como un usuario nuevo, y preguntamos
#sus datos para luego crear un archivo.


#Recordemos que en este mÃ³dulo estÃ¡n todos las funciones adicionales que hemos creado.
import SSred as Red
#El mÃ³dulo 'os' nos permitirÃ¡ consultar si un archivo existe.


Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habÃ­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
Red.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        Red.mostrar_muro(muro)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 5:
        amigo = input("¿Que amigo/a deseas agregar? ")
        amigos = Red.agregarAmigo(nombre,amigo)
    elif opcion == 6:
        print("------------- Mostrando publicaciones de amigos -----------------")
        for publicacion in Red.verPublicacionesAmigos(nombre):
            print(publicacion)
    elif opcion == 7:
        nuevo_nombre = input("¿A que perfil quieres cambiar?")
        if Red.existe_archivo(nuevo_nombre+".user"):
            print("Has decidido salir. Guardando perfil en ",nombre+".user")
            Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado,muro)
            print("Archivo",nombre+".user","guardado")
            print("Leyendo datos del NUEVO PERFIL de usuario", nuevo_nombre, "desde archivo.")
            (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nuevo_nombre)
            
        else:
            print("No hay perfil con ese nombre")
        

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado,muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")