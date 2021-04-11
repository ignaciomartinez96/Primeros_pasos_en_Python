'''
Project #3: Pick a Card Game!


Details:
 
Everyone has their favorite card game. What's yours? For this assignment, 
choose a card game (other than Blackjack), and turn it into a Python program. 
It doesn't matter if it's a 1-player game, or a 2 player game, or more! That's totally up to you. 
A few requirements:

It's got to be a card game (no board games, etc)
When the game starts up, you should ask for the players' names. 
And after they enter their names, your game should refer to them by name only. 
("It's John's turn" instead of "It's player 1's turn). 
'''






from random import shuffle, choice
from time import sleep


def CrearMazo():
    

    diamantes=['A♦️','2♦️','3♦️','4♦️','5♦️','6♦️','7♦️','8♦️',
              '9♦️','10♦️','J♦️','Q♦️','K♦️']
    treboles=['A♣️','2♣️','3♣️','4♣️','5♣️','6♣️','7♣️','8♣️',
              '9♣️','10♣️','J♣️','Q♣️','K♣️']
    picas=['A♠️','2♠️','3♠️','4♠️','5♠️','6♠️','7♠️','8♠️',
              '9♠️','10♠️','J♠️','Q♠️','K♠️']
    corazones=['A♥️','2♥️','3♥️','4♥️','5♥️','6♥️','7♥️','8♥️',
              '9♥️','10♥️','J♥️','Q♥️','K♥️']


    mazo=[]

    for d in diamantes:
        mazo.append(d)
    for t in treboles:
        mazo.append(t)
    for p in picas:
        mazo.append(p)
    for c in corazones:
        mazo.append(c)


    return mazo


class Player:
    def __init__(self,name,mano):
        self.name=name
        self.mano=mano

    def Win(self):
        if self.mano==[]:
            globals()['ganador_final']=self.name


mazo=CrearMazo()
ganador_final=''
bienvenida='''
***************************
*  BIENVENIDXS AL JUEGO   *
*          DEL            *
*       DESCONFÍO         *
***************************
'''
while(ganador_final==''):
    
    
    mazo_jugado=[]
    shuffle(mazo)

    primera_mano=[]    
    segunda_mano=[]
    turno_counter=1

    
    for card in range(26):
        primera_mano.append(mazo.pop())
    for card in range(26):
        segunda_mano.append(mazo.pop())
    print(bienvenida)
    sleep(2)
    nombre_uno=input('Nombre del primer jugador: ')
    nombre_dos=input('Nombre del segundo jugador: ')
    jugador_uno=Player(nombre_uno,primera_mano)
    jugador_dos=Player(nombre_dos,segunda_mano)

   
    
    while(ganador_final==''):
        
        if turno_counter==1:
            if len(mazo_jugado)>=1:
                turno='Es el turno de: '+jugador_uno.name
                print(turno)
                desconfianza=input("¿Desconfiás?: " )
                if desconfianza=='sí' or desconfianza=='si':
                    print(mazo_jugado[-1])
                    pregunta=input("¿Mintió?: ")
                    if pregunta=='sí' or pregunta=='si':
                        for c in range(len(mazo_jugado)):
                            jugador_dos.mano.append(mazo_jugado.pop())
                            
                    else:
                        for c in range(len(mazo_jugado)):
                            jugador_uno.mano.append(mazo_jugado.pop())
                            
                else:
                    print(jugador_uno.mano)
                    jugada=input('¿Qué carta vas a jugar?: ')
                    mentira=input('Decí qué palo jugás: ')
                    print(chr(27) + "[2J")
                    jugador_uno.mano.remove(jugada)
                    mazo_jugado.append(jugada)
                    turno_counter+=1
            else:
                turno='Es el turno de: '+jugador_uno.name
                print(turno)
                print(jugador_uno.mano)
                jugada=input('¿Qué carta vas a jugar?: ')
                mentira=input('Decí qué palo jugás: ')
                print(chr(27) + "[2J")
                jugador_uno.mano.remove(jugada)
                mazo_jugado.append(jugada)
                turno_counter+=1
        jugador_uno.Win()    
        
        if turno_counter==2:
            print(jugador_uno.name,'ha dicho:',mentira)
            sleep(2)
            turno='Es el turno de: '+jugador_dos.name
            print(turno)
            desconfianza=input("¿Desconfiás?: " )
            if desconfianza=='sí' or desconfianza=='si':
                print(mazo_jugado[-1])
                pregunta=input("¿Mintió?: ")
                if pregunta=='sí' or pregunta=='si':
                    for c in range(len(mazo_jugado)):
                        jugador_uno.mano.append(mazo_jugado.pop())
                       
                else:
                    for c in range(len(mazo_jugado)):
                        jugador_dos.mano.append(mazo_jugado.pop())
                        
            print(jugador_dos.mano)
            jugada=input('¿Qué carta vas a jugar?: ')
            mentira=input('Decí qué palo jugás: ')
            print(chr(27) + "[2J")
            jugador_dos.mano.remove(jugada)
            mazo_jugado.append(jugada)
            turno_counter-=1
            print(jugador_dos.name,'ha dicho:',mentira)
            sleep(2)
        
        
        jugador_dos.Win()
        
        if ganador_final!='':
            print('Acaba de ganar: '+ganador_final)
            sleep(2)
            print('Felicitaciones!!')
            
        
        