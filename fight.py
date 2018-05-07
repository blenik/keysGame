# coding=utf-8
"""
########################################################################################
#                                                                                      #
#                                                                                      #
#                                                                                      #
#                                   MODUL: FIGHT                                       #
#                                                                                      #
#                                                                                      #
#                                  author: xxx                                         #
#                                                                                      #
#                                                                                      #
########################################################################################

"""

from pynput import keyboard
import random
import os
import math


"""
Funkcja collision przyjmuje parametry odpowiedzialne za wspolrzedne jednego i drugiego gracza gdzie:
x1,y1 = wspolrzedna x i y gracza nr 1
x2,y2 = wspolrzedna x i y gracza nr 2

Jezeli dwaj gracze sa od siebie oddaleni na 1 kratke funkcja zwraca wartosc True

Funkcje nalezy zaimplementowac w glownej petly gry
"""
def collision(x1, y1, x2, y2):
    if (math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) == 1: # obliczanie odleglosci miedzy dwoma playerami
        return True


"""
Funckja randomcharsforP1 losuje znaki z x c dla gracza 1 i je zwraca
Funkcja uzywana w klasie Variable, znaki przypisane na stale podczas walki do zmiennych randomcharsforP1_static
"""

def randomcharsforP1():

    chars1 = ['z', 'x', 'c'] # litery z ktorych program losuje
    stry = ""
    charsForPlayer1 = []
    i = len(chars1)
    while i > 0:
        w = random.randint(0, 2)
        if chars1[w] not in charsForPlayer1:
            charsForPlayer1.append(chars1[w]) # jezeli danej litery nie ma jeszcze w nowej liscie to dodaj
            stry += chars1[w]
            i -= 1
    return charsForPlayer1

"""
Funckja randomcharsforP1 losuje znaki b n m dla gracza 2
Uzywana w klasie Variable, znaki przypisane na stale podczas walki do zmiennych randomcharsforP2_static
"""

def randomcharsforP2():

    chars2 = ['b', 'n', 'm']
    charsForPlayer2 = []
    i = len(chars2)
    while i > 0:
        w = random.randint(0, 2)
        if chars2[w] not in charsForPlayer2:
            charsForPlayer2.append(chars2[w])
            i -= 1
    return charsForPlayer2

"""
   Clasa variable przechowuje zmienne:
   Dla randomcharsforP1_static i randomcharsforP2_static przypisujemy wylosowany zestaw znakow.
   Flaga killState1/2 mówi nam kiedy ktos kogos zabil. W glownej petli jezeli flaga ktoregos z graczy zmieni sie na True nalezy usunac klucz z konta jednego gracza i umiescic losowo na mapie.
   Zmienne var_countP1 i var_countP2 przechowuja informacje ile poprawnych znakow zostalo wcisnietych.

"""
class Variable:
    randomcharsforP1_static = randomcharsforP1()
    randomcharsforP2_static = randomcharsforP2()
    killStatePlayer1 = False
    killStatePlayer2 = False
    var_countP1 = 0 # ilosc poprawnie wcisnietych klawiszy gracza 1
    var_countP2 = 0 # ilosc poprawnie wcisnietych klawiszy gracza 2
    player1Points = 3
    player2Points = 3

"""
Funkcja on_press_checkinputkey przechwytuje klawisze w momencie wystapienia kolizji (funkcja collision)
Nastepnie sprawdza jaki klawisz zostal wcisniety i porownuje z wylosowanymi znakami ktore znajduja sie w klasie Variable
Funkcja wypisuje rowniez informacje kiedy nastapuje walka oraz jaka sekwencje klawiszy nalezy wcisnac by pokonac drugiego gracza.


"""

def on_press_checkinputkey(key):

    try: k = key.char
    except: k = key.name
    if k is Variable.randomcharsforP1_static[Variable.var_countP1] and Variable.killStatePlayer2 == False:  # sprawdzanie czy wcisniety klawisz jest taki jaki znajduje sie w liscie wczesniej wylosowanych znakow (w klasie Variable)
        Variable.randomcharsforP1_static[Variable.var_countP1] = str.capitalize(Variable.randomcharsforP1_static[Variable.var_countP1]) # Jezeli przycis zgadza sie z wylosowanym wczesniej to zmienia sie jego wielkosc na wielka litere
        os.system("cls") # czyszczenie ekranu
        print("WALKA!!!")
        print("=================================")
        print(display_letters_toclick(Variable.randomcharsforP1_static, Variable.randomcharsforP2_static)) #wyswietlenie informacji o walce i jaka ma byc sekwencja klawiszy dla jednego i drugiego gracza
        print("=================================\n")
        Variable.var_countP1 += 1 # policzenie czy ktos wcisnal odpowiedni klawisz
    if Variable.var_countP1 == 3: # jezeli ilosc poprawnie wcisnietych klawisz rowne jest 3 nastepuje zabicie przeciwnego gracza
        print('Player1 killed Player2\n')
        Variable.var_countP1=0 # zerowanie poprawnie wcisnietych znakow gracza 1
        Variable.killStatePlayer2 = True # zmiana flagi zabicia drugiego graczaxbb
        listener.stop() # zatrzymanie nasluchiwania klawiszy

    try: k = key.char
    except: k = key.name
    if k is Variable.randomcharsforP2_static[Variable.var_countP2] and Variable.killStatePlayer1==False:
        Variable.randomcharsforP2_static[Variable.var_countP2] = str.capitalize(Variable.randomcharsforP2_static[Variable.var_countP2])
        os.system("cls")
        print("WALKA!!!")
        print("=================================")
        print(display_letters_toclick(Variable.randomcharsforP1_static, Variable.randomcharsforP2_static))
        print("=================================\n")
        Variable.var_countP2 += 1
    if Variable.var_countP2 == 3:
        print('Player2 killed Player1\n')
        Variable.var_countP2 = 0
        Variable.killStatePlayer1 = True
        listener.stop()


"""


Funckja display_letters_toclick wyswietla w odpowiedniej kolejnosci informacje w zwiazku z sekwencja wcisniecia klawiszy
Przyjmuje parametry z klasy Variable, zamienia na stringi i dolacza do glownego stringa.
Uzyta jest w funkcji on_press_checkinputkey


"""

def display_letters_toclick(var1, var2):

    lettersString = "Player 1: " # glowny string funkcji

    for i in var1:
        lettersString += i      # doklejanie liter ktore maja zostac wyswietlone dla gracza 1
        lettersString += " "
    lettersString += "\tPlayer 2: "

    for i in var2:
        lettersString += i # doklejanie liter ktore maja zostac wyswietlone dla gracza 2
        lettersString += " "
    return lettersString # zwracanie stringa z sekwencja klawiszy


# def show_scores_after_fight():
#     if Variable.killStatePlayer1==True:
#         Variable.player1Points -= 1
#         display_letters_toclick(str(Variable.player1Points), str(Variable.player2Points))
#         #SpawnKey()
#         Variable.killStatePlayer1 = False
#     elif Variable.killStatePlayer2==True:
#         Variable.player2Points -= 1
#         display_letters_toclick(str(Variable.player1Points), str(Variable.player2Points))
#         #SpawnKey()
#         Variable.killStatePlayer2 = False
#
#
# if collision(1,2,1,3):
#     print("WALKA!!!")
#     print("=======================================")
#     print(display_letters_toclick(Variable.randomcharsforP1_static, Variable.randomcharsforP2_static))
#     print("=======================================\n")
#     show_scores_after_fight()


"""
Nasluchiwanie wcisniecia klawisza i przeslanie informacji do funkcj in_press_checkinputkey podczas wcisniecia klawisza
"""
listener = keyboard.Listener(on_press=on_press_checkinputkey)
listener.start()
listener.join()

"""
W razie niejasnosci kontakt wskazany
"""