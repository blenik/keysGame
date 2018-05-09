# the project is divided into sections.
# edit only your section!
# comment all yours code!

# section 0: global
import random
from InterfaceCreator import InterfaceCreator
from msvcrt import getch
from movement import player
import os
import time
from map import readingLevelsFromFileToArray
from map import printingTheMap
from fight import Fight_Class



def obslugaPunktow(dlaKogo): ## DZIAŁA TYLKO DLATEGO ŻE WSZYSTKO JEST LOKALNIE W JEDNYM SCOPE
## JEŻELI CHEMY TO NAPRAWIĆ TO ALBO Z GŁÓWNEJ PĘTLI TRZEBA ZROBIĆ KLASĘ 
## ALBO WALNĄĆ TO JAKO KOD DO PROGRAMU A NIE FUNKCJA
    if dlaKogo:
        interfacePrinter.points_increase(True) # zwieksz wynik w interfejsie
        gameStateDict['P1Points']=gameStateDict['P1Points']+1  # oraz stanie gry 
        if gameStateDict['P1Points']>7: # jak zdobedzie wiekszosc kluczy 
            interfacePrinter.score_increase(True) # zwieksz Score wyzeruj punkty
            gameStateDict['P1Points']=0
            gameStateDict['P2Points']=0
            gameStateDict['P1Score']=gameStateDict['P1Score']+1
            if gameStateDict['P1Score']>2: # jak wygra 3 rundy 
                clscr()
                interfacePrinter.print_interface()  # pokazuje interface
                print('***PLAYER1 WINS***')
                printingTheMap(lista)  # wczytywanie mapy
                return False # zakoncz gre
            else:
                clscr()
                interfacePrinter.print_interface()  # pokazuje interface
                print('***PLAYER1 GETS POINTS***')
                printingTheMap(lista)  # wczytywanie mapy
                time.sleep(5) # ustaw mape na nowo
                gracz_1.przestaw(1,20,lista)
                gracz_2.przestaw(20,20,lista)
                init_keys(lista)
        return True
    else:
        interfacePrinter.points_increase(False) # zwieksz wynik w interfejsie
        gameStateDict['P2Points']=gameStateDict['P2Points']+1 # oraz stanie gry 
        if gameStateDict['P2Points']>7: # jak zdobedzie wiekszosc kluczy 
            interfacePrinter.score_increase(False) # zwieksz Score wyzeruj punkty
            gameStateDict['P2Points']=0
            gameStateDict['P1Points']=0
            gameStateDict['P2Score']=gameStateDict['P2Score']+1
            if gameStateDict['P2Score']>2: # jak wygra 3 rundy 
                clscr()
                print('***Player2 WINS***')
                interfacePrinter.print_interface()  # pokazuje interface
                printingTheMap(lista)  # wczytywanie mapy
                return False # zakoncz gre
            else:
                clscr()
                interfacePrinter.print_interface()  # pokazuje interface
                print('***PLAYER2 GETS POINTS***')
                printingTheMap(lista)  # wczytywanie mapy
                time.sleep(5) # ustaw mape na nowo
                gracz_1.przestaw(1,20,lista)
                gracz_2.przestaw(20,20,lista)
                init_keys(lista)
        return True

# section 1: map
# wywalic do osobnego pliku
def respawn(Plansza):
    spawn = (Plansza[1][1], Plansza[1][20], Plansza[20][1], Plansza[20][20])
    spot = (random.choice(spawn))

    return spot

# section 4: randomization
# wywalic do osobnego pliku
def clscr():
    os.system('cls' if os.name=='nt' else 'clear')


def init_keys(Plansza):
    i = 0
    while i < 2:
        t = random.sample(range(1, 21), 2)
        if Plansza[1][t[0]] != " " or Plansza[1][t[1]] != " ":
            i = i
        else:
            Plansza[1][t[i]] = "k"
            i = i + 1

    i = 0
    j = 1
    while 3 * j < 21:
        if 3 * j == 6:
            j = j + 1
        while i < 2:
            t = random.sample(range(1, 21), 2)
            if Plansza[3 * j][t[0]] != " " or Plansza[3 * j][t[1]] != " ":
                i = i
            else:
                Plansza[3 * j][t[i]] = "k"
                i = i + 1

        i = 0
        j = j + 1

    Plansza[20][1] = "k"

k=Fight_Class()
PLANSZA_SIZE = 22
interfacePrinter = InterfaceCreator(PLANSZA_SIZE, "*")  # tworzy instancje creatora interfejsu
lista = list()
readingLevelsFromFileToArray(lista)
gracz_1 = player(1, 20, lista)
gracz_2 = player(20, 20, lista)
init_keys(lista)


interfacePrinter.print_interface()
printingTheMap(lista)

gameStateDict={'P1Points':0,'P2Points':0,'P1Score':0,'P2Score':0} #slownik ze stanem gry


playGame=True # zmienna zeby moznalo gre wylaczyc z innych miejsc
while playGame:

    clscr()
    interfacePrinter.print_interface()  # pokazuje interface
    printingTheMap(lista)  # wczytywanie mapy

    punktDlaP1 = False
    punktDlaP2 = False

    key = ord(getch())
    if key == 115:  # S move down
        print('down')
        punktDlaP1 = gracz_1.move_down(lista)
    elif key == 53:  # 5 move down
        print('down')
        punktDlaP2 = gracz_2.move_down(lista)

    elif key == 119:  # W move up
        print('up')
        punktDlaP1 = gracz_1.move_up(lista)
    elif key == 56:  # 8 move up
        print('up')
        punktDlaP2 = gracz_2.move_up(lista)

    elif key == 97:  # A move Left
        print('left')
        punktDlaP1 = gracz_1.move_left(lista)
    elif key == 52:  # A move Left
        print('left')
        punktDlaP2 = gracz_2.move_left(lista)

    elif key == 100:  # D move Right
        print('right')
        punktDlaP1 = gracz_1.move_right(lista)
    elif key == 54:  # 6 move Right
        print('right')
        punktDlaP2 = gracz_2.move_right(lista)
    if key == 27:  # ESC
        break

    if  punktDlaP1: # jezeli dostanie punkt
        playGame=obslugaPunktow(True)
                

    if punktDlaP2: # jezeli dostanie punkt
        playGame=obslugaPunktow(False)
    

    if k.collision(gracz_1.x, gracz_1.y, gracz_2.x, gracz_2.y):
        k.chars_randomization()
        # k.display_letters_toclick(k.randomcharsforP1_static, k.randomcharsforP2_static)
        while k.killStatePlayer1 == False or k.killStatePlayer2 == False:
            interfacePrinter.print_interface()  # pokazuje interface
            printingTheMap(lista)  # wczytywanie mapy
            k.fight_interface()
            key = getch().decode("utf-8")
            k.on_press_checkinputkey(key)
            if k.killStatePlayer1 == True or k.killStatePlayer2 == True:
                k.killStatePlayer1 = False
                k.killStatePlayer2 = False
                break
#while(True) ends

