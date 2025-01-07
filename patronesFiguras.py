
def showTriangle(rowes, figure):
    for i in range(0, rowes):
        for j in range(0, i+1):
            print(figure, end=" ")
        print("\r")



#alineados a derecha
def rightJustifiedTriangle(cant, simb):
    for i in range(1, cant + 1):
        # Imprime espacios para justificar a la derecha
        print(" " * (cant - i) + simb * i)



#alineados a izquierda hacia abajo
def triangleLeftToDown(cant,simb):
    for i in range(cant + 1, 0, -1):
        for j in range(0, i - 1):
            print(simb, end=" ")
        print(" ")
    

#centrados hacia abajo
def inversePiramide(cant,simb):
    k = 2 * cant - 2
    for i in range(cant, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(simb, end=" ")
        print("")

def separador():
    print("\n ------------------------- \n")

#rombo de asteriscos
def rombe(cant, simb):
    # Parte superior del rombo
    for i in range(cant):
        for j in range(cant * 2 - 1):
            # Condiciones para imprimir solo el contorno
            if j == cant - 1 - i or j == cant - 1 + i:
                print(simb, end="")
            else:
                print(end=" ")
        print()
    
    # Parte inferior del rombo
    for i in range(cant - 2, -1, -1):
        for j in range(cant * 2 - 1):
            # Condiciones para imprimir solo el contorno
            if j == cant - 1 - i or j == cant - 1 + i:
                print(simb, end="")
            else:
                print(end=" ")
        print()

#diamante relleno
def showDiamond(cant, simb):
    # Parte superior del diamante
    for i in range(1, cant + 1):
        print(" " * (cant - i) + simb * (2 * i - 1))
    
    # Parte inferior del diamante
    for i in range(cant - 1, 0, -1):
        print(" " * (cant - i) + simb * (2 * i - 1))


#marco rectangular
def hollowSquare(cant, simb):
    for i in range(cant):
        if i == 0 or i == cant - 1:
            print(simb * cant)  # Imprime la línea superior e inferior
        else:
            print(simb + " " * (cant - 2) + simb)  # Imprime el marco de los lados


showTriangle(5,"*")
separador()
rightJustifiedTriangle(4,"=")
separador()
triangleLeftToDown(6,"@")
separador()
inversePiramide(4,"H")
separador()
rombe(5,"+")
separador()
showDiamond(4,"X")
separador()
hollowSquare(6,"%")