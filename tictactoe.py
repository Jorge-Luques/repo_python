theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def hayLinea(ficha, board, pos1, pos2, pos3):
    return board[pos1] == ficha and board[pos2] == ficha and board[pos3] == ficha

def hayGanador(ficha, board):
    if hayLinea(ficha, board, "top-L", "mid-M", "low-R") or hayLinea(ficha, board, "top-R", "mid-M", "low-L") or hayLinea(ficha, board, "top-L", "top-M", "top-R") or hayLinea(ficha, board, "mid-L", "mid-M", "mid-R") or hayLinea(ficha, board, "low-L", "low-M", "low-R") or hayLinea(ficha, board, "top-L", "mid-L", "low-L") or hayLinea(ficha, board, "top-M", "mid-M", "low-M") or hayLinea(ficha, board, "top-R", "mid-R", "low-R"):
        return True

def tableroLleno(board):
    return all(space != ' ' for space in board.values())

def jugar(theBoard):
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turno para ' + turn + '. ¿En qué espacio quieres mover?')
        move = input()
        
        if move in theBoard and theBoard[move] == ' ':
            theBoard[move] = turn
            
            if hayGanador(turn, theBoard):
                printBoard(theBoard)
                print("¡Ganaron las " + turn + "!")
                break
            
            if tableroLleno(theBoard):
                printBoard(theBoard)
                print("¡Es un empate!")
                break
            
            turn = 'O' if turn == 'X' else 'X'
        else:
            print("Movimiento inválido. Intenta de nuevo.")
    
    print("Juego terminado. Reiniciando el tablero...")
    # Reiniciar el tablero
    for key in theBoard:
        theBoard[key] = ' '


jugar(theBoard)