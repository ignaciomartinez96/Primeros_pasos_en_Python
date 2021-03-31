"""
Proyecto #1: Un juego sencillo!

En esta oportunidad, voy a diseñar un programa que le permita a dos usuarios jugar a 
Conecta 4. En este sentido, el programa podrá dibujar un tablero de siete columnas y seis filas. 
El jugador 1 posee fichas en forma de "X" y el jugador 2 posee las que tienen forma de "O".

El primer jugador en conectar cuatro fichas idénticas de forma vertical, horizontal o diagonal, gana.

"""






# Esta función devuelve un tablero con las medidas adecuadas para jugar a Conecta 4
def DibujarTablero(jugada):  #  El argumento que toma es una lista de listas que se verá más abajo
    for row in range(11):
        if row % 2 == 0:
            practicalrow = int(row/2)
            for column in range(13):
                if column % 2 == 0:
                    practicalcolumn = int(column/2 + 0.5)
                    if column != 12:
                        print(jugada[practicalcolumn][practicalrow] ,end='')
                    else:
                        print(jugada[practicalcolumn][practicalrow])
                else:
                    print('|',end = '')
        else:
            print('-' * column + '-')


#  Las funciones siguientes se encargan de verificar si algún jugador ganó
def CheckVertical(tablero):
    P1=['X','X','X','X']
    P2=['O','O','O','O']
    for columna in range(7):
        for fila in range(5,2,-1):
            counter = 4
            list = []
            while counter > 0: 
                list.append(tablero[columna][fila])
                fila -= 1
                counter -= 1
                if list == P1:
                    print('\n EL JUGADOR 1 GANA!')
                    globals()['winner'] = 1
                    return
                elif list == P2:
                    print('\n EL JUGADOR 2 GANA!')
                    globals()['winner'] = 2
                    return


def CheckHorizontal(tablero):
    P1=['X','X','X','X']
    P2=['O','O','O','O']
    
    for fila in range(6):
        for columna in range(4):
            counter = 4
            f = columna
            list = []
            while counter > 0:
                list.append(tablero[f][fila])
                f += 1
                counter -= 1
                if list == P1:
                    print('\n EL JUGADOR 1 GANA!')
                    globals()['winner'] = 1
                    return
                elif list == P2:
                    print('\\n EL JUGADOR 2 GANA!')
                    globals()['winner'] = 2
                    return

def CheckDiag(tablero):
    P1=['X','X','X','X']
    P2=['O','O','O','O']


    for columna in range(4):
        for fila in range(3):
            counter = 4
            c = columna
            r = fila
            list=[]
            while counter > 0:
                list.append(tablero[c][r])
                r += 1
                c += 1
                counter -= 1
                if list == P1:
                    print("\n EL JUGADOR 1 GANA!")
                    globals()["winner"]=1
                    return
                elif list == P2:
                    print("\n EL JUGADOR 2 GANA!")
                    globals()["winner"] = 1
                    return
    for columna in range(6,2,-1):
        for fila in range(3):
            counter = 4
            c = columna
            r = fila
            list = []
            while counter > 0:
                list.append(tablero[c][r])
                r += 1
                c -= 1
                counter -= 1
                if list == P1:
                    print("\n EL JUGADOR 1 GANA!")
                    globals()["winner"]=1
                    return
                elif list == P2:
                    print("\n EL JUGADOR 2 GANA!")
                    globals()["winner"]=1
                    return


"""
Ahora, voy a crear una lista de listas "Jugadas". Cada elemento de la lista corresponde a una columna,
por eso, hay un total de siete. A su vez, cada elemento es una lista que contiene en su interior
seis elementos: el número de filas del tablero.

Esta lista será el argumento que la función DibujarTablero() necesita para mostrar el tablero del juego.

"""

Jugadas = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ']]

DibujarTablero(Jugadas)  


"""
Una vez que tenemos todos nuestros ingredientes listos, escribimos un bucle extenso con más
bucles en su interior. También colocamos las funciones anteriores para verificar si algún 
jugador ganó. 

Si la partida se termina, el programa preguntará si quieren jugar otra vez.

"""

Player = 1
winner = 0
Row = -1

while winner == 0:
    
    print('\n Es el turno del jugador', Player)
    print('\n1|2|3|4|5|6|7')
    DibujarTablero(Jugadas)
    print('1|2|3|4|5|6|7')
    MoveColumn = int(input('\n Por favor, elegí una columna: ')) - 1
    if Player == 1:
        if Jugadas[MoveColumn][Row] == ' ':
            Jugadas[MoveColumn][Row] = 'X'
            Player = 2
        else:
            while(Jugadas[MoveColumn][Row] != ' '):
                Row = Row - 1
                if Row == -7:
                    Row = -1
                    break
            if Jugadas[MoveColumn][Row] == ' ':
                Jugadas[MoveColumn][Row] = 'X'
                Player = 2
                Row = -1
               
                
    else:
        if Jugadas[MoveColumn][Row] == ' ':
            Jugadas[MoveColumn][Row] = 'O'
            Player = 1
        else:
            while (Jugadas[MoveColumn][Row] != ' '):
                Row = Row - 1
                if Row == -7:
                    Row = -1
                    break
            if Jugadas[MoveColumn][Row] == ' ':
                Jugadas[MoveColumn][Row] = 'O'
                Player = 1
                Row = -1   
                 
   
    CheckVertical(Jugadas)
    CheckHorizontal(Jugadas)
    CheckDiag(Jugadas)
    if winner > 0:
        DibujarTablero(Jugadas)
        if input('¿Nueva partida?[sí]/n: ') == 'si' or 'sí':
            Jugadas = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ']]
            winner = 0
            PLayer=1
        else:
            print('Hasta pronto! :)')
