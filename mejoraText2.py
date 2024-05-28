try: 
    nomFile = input("ingresar el nombre del archivo de texto con su extension a modificar: ")
    with open(nomFile,"rt+") as f:
        listaSaltos = f.readlines()
        aux = ""
        fModif = open("textoModif.txt", "x+",encoding="UTF-8")
        #print(listaSaltos)
        for salto in listaSaltos:
            aux = salto[-2]
            #print(aux)
            if  aux != ".": # si antes del salto de linea no hay un punto
                miniS = salto.replace("\n"," ")
                fModif.write(miniS)
            else: 
                fModif.write(salto)
            
        fModif.close()
        
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos para abrir el archivo.")
except IsADirectoryError:
    print("Ese es un directorio, y no se puede leer o modificar su contenido")
except FileExistsError:
    print("Ya se existe un archivo con ese nombre")
finally:
    f.close()