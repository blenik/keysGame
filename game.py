#the project is divided into sections.
#edit only your section!
#comment all yours code!

#section 0: global
import random
from InterfaceCreator import InterfaceCreator
from msvcrt import getch
from movement import player
import os
import fight

PLANSZA_SIZE=22
interfacePrinter=InterfaceCreator(PLANSZA_SIZE,"*") # tworzy instancje creatora interfejsu

#section 1: map

def respawn():

    spawn=(Plansza[1][1], Plansza[1][20], Plansza[20][1], Plansza[20][20])
    spot=(random.choice(spawn))

    return spot

# section 4: randomization
def init_keys(Plansza):
    i = 0
    while i < 2:
        t = random.sample(range(1, 21), 2)
        if Plansza[1][t[0]]!=" " or Plansza[1][t[1]]!=" ":
            i=i
        else:
            Plansza[1][t[i]] = "k"
            i = i + 1

    i = 0
    j = 1
    while 3 * j < 21:
        if 3*j==6:
            j=j+1
        while i < 2:
            t = random.sample(range(1, 21), 2)
            if Plansza[3 * j][t[0]] != " " or Plansza[3 * j][t[1]] != " ":
                i=i
            else:
                Plansza[3 * j][t[i]] = "k"
                i=i+1

        i = 0
        j = j + 1


    Plansza[20][1]="k"


lista = list()

# funkcja odczytujaca plik z mapa i wpisanie jej do macierzy 'lista'
def readingLevelsFromFileToArray(lista):
    file = open('Level_1_Template.txt', 'r')
    boardgame = file.read().splitlines()
    file.close()
    for line in boardgame:
        lista.append([c for _, c in enumerate(line)])
    return lista

# funkcja wyswietlajaca mape
def printingTheMap(map):
    for row in map:
        print(''.join([str(elem) for elem in row]))

# wywolanie funkcji
readingLevelsFromFileToArray(lista)
#printingTheMap(lista)
gracz_1=player(1,20)
gracz_2=player(20,20)

def cls():
    os.system('cls')


#section 2: fight




#section 3: moving
# pętla odpowiedzialna za oczekiwanie na wcisnięcie klawisza,
while True:
    #if key == 27:  # ESC
       # break
    zmiennaP1=False
    zmiennaP2=False
    #elif key == 13:  # Enter
      #  print('selected')
    #elif key == 32:  # Space
     #   print('jump')
    #elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
    key = ord(getch())
    if key == 115:  # S move down
        print('down')
        zmiennaP1=gracz_1.move_down(lista)
    elif key == 53:  # 5 move down
        print('down')
        zmiennaP2 =gracz_2.move_down(lista)

    elif key == 119:  # W move up
        print('up')
        zmiennaP1 =gracz_1.move_up(lista)
    elif key == 56:  # 8 move up
        print('up')
        zmiennaP2 =gracz_2.move_up(lista)

    elif key == 97:  # A move Left
        print('left')
        zmiennaP1 =gracz_1.move_left(lista)
    elif key == 52:  # A move Left
        print('left')
        zmiennaP2 =gracz_2.move_left(lista)

    elif key == 100:  # D move Right
        print('right')
        zmiennaP1 =gracz_1.move_right(lista)
    elif key == 54:  # 6 move Right
        print('right')
        zmiennaP2 =gracz_2.move_right(lista)
    if key == 27:  # ESC
        break

    if zmiennaP1:
        interfacePrinter.points_increase(True)
    if zmiennaP2:
        interfacePrinter.points_increase(False)
    cls()  #czyszczenie ekranu
    printingTheMap(lista)   # wczytywanie mapy
    interfacePrinter.print_interface()  # pokazuje interface


#section 5: rendering




#section 6: interface

