# -*- coding: utf-8 -*-
"""
Project #2: Hangman

For this assignment, we want to play hangman in 2-player mode. 
The game should start by prompting player 1 to pick a word. 
Then the screen should clear itself so that player 2 can't see the word.

After the screen is clear, the "gallows" and the empty letter spaces should be drawn, 
and player 2 should be allowed to guess letters until they either win, or lose. 
As they choose correct letters, the letters should appear on the screen in place of the blank space. 
As they choose wrong letters, the "man" himself should come end up being drawn, piece by piece.
"""

# We import some helpful libraries
import time
import re       # this one will help to create some good lists
import getpass  # this one will hide the word written by the first player
import random


# I use the same board from the previous project with some little changes for ths version
def Hangman(tablero):
    print('_'*8)
    for fila in range(6):
        #practical_fila=int(fila/2)
        for columna in range(8):
            #practical_columna=int(columna/2)
            if columna!=7:
                print(tablero[columna][fila],end='')
            else:
                print(tablero[columna][fila])
            
            
                
    print('^'*8)
    
tablero = [['|','|','|','|','|','|','|'],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' '],['|',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]


# this function will help us to define whether we win or loose
def Chekeo(a):
    if '_' not in a:
        print('SALVADO!!')
        time.sleep(2)
        print('\n Gracias por salvar a nuestro amigo')
        time.sleep(2)
        new_party=input('¿Jugamos otra vez?: ')
        if new_party=='si' or new_party=='sí':
            globals()['player']=0
            globals()['tablero']=[['|','|','|','|','|','|','|'],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' '],['|',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
            return True
        else:
            print('\n Hasta pronto!')
            globals()['player']=3
            return False
    else:
        if contador==6:
            print('AHORCADO!!')
            time.sleep(2)
            print('PERDISTE :(')
            time.sleep(2)
            new_party=input('¿Jugamos otra vez?: ')
            if new_party=='si' or new_party=='sí':
                globals()['player']=0
                globals()['tablero']=[['|','|','|','|','|','|','|'],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
                        [' ',' ',' ',' ',' ',' ',' '],['|',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
                        [' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
                return 
            else:
                print('\n Hasta pronto!')
                globals()['player']=3
                return


# this is the only dict in the script. It contains some words to play along if someone choose the single mode
cartas={'fácil':['tonto','flor','mujer','cosa','partido','ciudad','historia','agua','ejemplo','ley','guerra','mano','sociedad',
                 'gente','problema','información','siglo','derecho','compras','barbijo','cajero','computadora','coche','cama','volar','película'
                'reina','cuaderno'],
        'medio':['interesate','disciplina','metastasis','alveolar','ideolecto','verbosemantica','parafasia','interestelar'
                'conjuncion','subordinada','subjuntivo','astragalo','inmunodeprimido','cardiovascular','gangrena','acincope',
                'minimalismo'],
        'difícil':['mamporrero','omeprazol','barbian','sapenco','vituperio','nefelibata',
                  'electroencefalografista','agapachar','zangolotear','ataraxia','cagaprisas'
                  'euroescepticismo','limerencia','sempiterno','casquivana','sopenco']}

player=0
bienvenida='''
*******************************************
*   BIENVENIDXS AL JUEGO DEL AHORCADO     *
*                                         *
*******************************************
'''
autor='''
************************
*  HECHO CON AMOR POR  *
*        NACHO         *
* **********************
'''
# with this big loop the game stars!!
while player==0:
    print(bienvenida)
    time.sleep(2)
    print(autor)
    time.sleep(3)
    contador=-1
    letras_usadas=[]
    hombre= r"O||//\\"
    cantidad_de_jugadores=input('¿Cuantxs jugadores van a jugar?\n [unx] [dos] ')
    if cantidad_de_jugadores=='2' or cantidad_de_jugadores=='dos':
        time.sleep(1)
        palabra=getpass.getpass(prompt='Dime la palabra: ')
        print(chr(27) + "[2J") 
        palabra_up=palabra.upper()
        palabra_lista=re.findall(r"\w",palabra_up)
        guess_lista=[]
        for letra in palabra_lista:
            guess_lista.append('_')
        player=2
        print('Salva a nuestro amigo!')
        time.sleep(1)
        while player==2:  
            guess=input('\n Dime una letra: ')
            guess_up=guess.upper()
            if guess_up in palabra_lista:
                while guess_up in palabra_lista:
                    guess_index=palabra_lista.index(guess_up)
                    guess_lista[guess_index]=guess_up
                    palabra_lista[guess_index]='_'
                Hangman(tablero)
                for i in guess_lista:
                    print(i,end=' ')
                print('\n')
                print('Estas letras no están en la palabra:',letras_usadas)
                Chekeo(guess_lista)
            
            else:
                if contador<7:
                    contador+=1
                    error=hombre[contador]
                    if contador==0:
                        tablero[4][1]=error
                    if contador==1:
                        tablero[4][2]=error
                    if contador==2:
                        tablero[4][3]=error
                    if contador==3:
                        tablero[3][2]=error
                    if contador==4:
                        tablero[3][4]=error
                    if contador==5:
                        tablero[5][4]=error
                    if contador==6:
                        tablero[5][2]=error
                letras_usadas.append(guess_up)
                Hangman(tablero)
                for i in guess_lista:
                    print(i,end=' ')
                print('\n')
                print('Estas letras no están en la palabra:',letras_usadas)
                Chekeo(guess_lista)
    else:
        player=1
        time.sleep(1)
        dificultad=input('¿Qué modo deseas jugar? \n [fácil] [medio] [difícil]: ')
        if dificultad=='facil':
            dificultad="fácil"
        if dificultad=="dificil":
            dificultad='difícil'
        palabra_pre=cartas[dificultad]
        palabra=random.choice(palabra_pre)
        palabra_up=palabra.upper()
        palabra_lista=re.findall(r"\w",palabra_up)
        guess_lista=[]
        for letra in palabra_lista:
            guess_lista.append('_')
        while player==1:
            guess=input('Dime una letra: ')
            guess_up=guess.upper()
            if guess_up in palabra_lista:
                while guess_up in palabra_lista:
                    guess_index=palabra_lista.index(guess_up)
                    guess_lista[guess_index]=guess_up
                    palabra_lista[guess_index]='_'
                Hangman(tablero)
                for i in guess_lista:
                    print(i,end=' ')
                print('\n')
                print('Estas letras no están en la palabra:',letras_usadas)
                Chekeo(guess_lista)
            
            else:
                if contador<7:
                    contador+=1
                    error=hombre[contador]
                    if contador==0:
                        tablero[4][1]=error
                    if contador==1:
                        tablero[4][2]=error
                    if contador==2:
                        tablero[4][3]=error
                    if contador==3:
                        tablero[3][2]=error
                    if contador==4:
                        tablero[3][4]=error
                    if contador==5:
                        tablero[5][4]=error
                    if contador==6:
                        tablero[5][2]=error
                letras_usadas.append(guess_up)
                Hangman(tablero)
                for i in guess_lista:
                    print(i,end=' ')
                print('\n')
                print('Estas letras no están en la palabra:',letras_usadas)
                Chekeo(guess_lista)
        
 



