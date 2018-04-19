#the project is divided into sections. 
#edit only your section!
#comment all yours code!

#section 0: global
import random
from InterfaceCreator import InterfaceCreator
from msvcrt import getch
from movement_2 import player
import movement_2
PLANSZA_SIZE=22



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
printingTheMap(lista)


FileBoard = open('Level_1_Template.txt', 'r')
BoardGameArray = FileBoard.read().splitlines()

lista=list()

for linia in BoardGameArray:
    lista.append([c for _,c in enumerate(linia)])
init_keys(lista)
for row in lista:
    print(''.join([str(elem) for elem in row]))



#section 2: fight




#section 3: moving
gracz_1 = player(1, 21)
gracz_2 = player(21, 21)

while true:
    #if key == 27:  # ESC
       # break
    #elif key == 13:  # Enter
      #  print('selected')
    #elif key == 32:  # Space
     #   print('jump')
    #elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
       # key = ord(getch())
    if key == 115:  # S move down
        print('down')
        gracz_1.move_down(lista)
    elif key == 53:  # 5 move down
        print('down')
        gracz_2.move_down_down(lista)

    elif key == 119:  # W move up
        print('up')
        gracz_1.move_up(lista)
    elif key == 56:  # 8 move up
        print('up')
        gracz_2.move_up(lista)

    elif key == 97:  # A move Left
        print('left')
        gracz_1.move_left(lista)
    elif key == 52:  # A move Left
        print('left')
        gracz_2.move_left(lista)

    elif key == 100:  # D move Right
        print('right')
        gracz_1.move.right(lista)
    elif key == 54:  # 6 move Right
        print('right')
        gracz_2.move.right(lista)







#section 5: rendering




#section 6: interface


interfacePrinter=InterfaceCreator(PLANSZA_SIZE,"*") # tworzy instancje creatora interfejsu 
# dalej trzeba by sie bawic nim w miejscu gdzie sa dodawane punkty i wynik 
# i printowac w miejscu drukowaniu mapy
interfacePrinter.print_interface()
