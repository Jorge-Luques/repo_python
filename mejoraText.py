fFinal = []
with open("mitexto.txt","rt+") as f:
    listaSaltos = f.readlines()
    aux = ""
    miniS = ""
    #print(listaSaltos)
    for salto in listaSaltos:
        aux = salto[-2]
        #print(aux)
        if  aux != ".": # si antes del salto de linea no hay un punto
            miniS = salto.replace("\n"," ")
            fFinal.append(miniS)
        else: 
            fFinal.append(salto)
    print(fFinal)
    for linea in fFinal:
        f.write(linea)
