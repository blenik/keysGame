# coding=utf-8
"""
########################################################################################
#                                                                                      #
#                                                                                      #
#                                                                                      #
#                                   MODUL: Fight_Class                                       #
#                                                                                      #
#                                                                                      #
#                                  author: xxx                                         #
#                                                                                      #
#                                                                                      #
########################################################################################
"""

"""
Pobieram z paczki pynput nasluchiwanie klawiszy
"""


import random
import os
import math
from msvcrt import getch


class Fight_Class(object):

    """
    Flaga killState1/2 mówi nam kiedy ktos kogos zabil. W glownej petli, jezeli flaga ktoregos z graczy zmieni sie na True,
    nalezy usunac klucz z konta jednego gracza i umiescic losowo na mapie.
    Zmienne var_countP1 i var_countP2 przechowuja informacje ile poprawnych znakow zostalo wcisnietych.
    Zmienne randomcharsforP1/P2_static przechowuja wylosowane wczesniej znaki
    """

    killStatePlayer1 = False
    killStatePlayer2 = False
    var_countP1 = 0  # ilosc poprawnie wcisnietych klawiszy gracza 1
    var_countP2 = 0  # ilosc poprawnie wcisnietych klawiszy gracza 2
    randomcharsforP1_static = []
    randomcharsforP2_static = []

    """
        Dla randomcharsforP1_static i randomcharsforP2_static przypisujemy wylosowany zestaw znakow. Ze wzgledu na to iż muszą byc
        rozne w momencie kolejnych walk nalezy je wywolywac przy kolejnych kolizjach (aby za kazdym razem znaki do wprowadzenia
        byly inne)
    """

    def chars_randomization(self):
        self.randomcharsforP1_static = self.randomcharsforP1()
        self.randomcharsforP2_static = self.randomcharsforP2()

    """
    Funkcja on_press_checkinputkey przechwytuje klawisze w momencie wystapienia kolizji (funkcja collision)
    Nastepnie sprawdza jaki klawisz zostal wcisniety i porownuje z wylosowanymi znakami ktore znajduja sie w zmiennych randomcharsforP1/P2_static
    """

    def on_press_checkinputkey(self, key):

        k = key
        if k is self.randomcharsforP1_static[self.var_countP1] and self.killStatePlayer2 == False and self.killStatePlayer2 == False:  # sprawdzanie czy wcisniety klawisz jest taki jaki znajduje sie w liscie wczesniej wylosowanych znakow (w klasie Variable)
            self.randomcharsforP1_static[self.var_countP1] = str.capitalize(self.randomcharsforP1_static[self.var_countP1])  # Jezeli przycis zgadza sie z wylosowanym wczesniej to zmienia sie jego wielkosc na wielka litere

            os.system("cls")  # czyszczenie ekranu

            # os.system("cls")  # czyszczenie ekranu

            # print("WALKA!!!")
            # print("=================================")
            # print(Fight_Class().display_letters_toclick(Fight_Class().randomcharsforP1_static, Fight_Class().randomcharsforP2_static))  # wyswietlenie informacji o walce i jaka ma byc sekwencja klawiszy dla jednego i drugiego gracza
            # print("=================================\n")
            self.var_countP1 += 1  # policzenie czy ktos wcisnal odpowiedni klawisz
        if self.var_countP1 == 3:  # jezeli ilosc poprawnie wcisnietych klawisz rowne jest 3 nastepuje zabicie przeciwnego gracza
            print('Player1 killed Player2\n')
            self.var_countP1 = 0  # zerowanie poprawnie wcisnietych znakow gracza 1
            self.killStatePlayer2 = True  # zmiana flagi zabicia drugiego gracza
            print(str(self.killStatePlayer2))
            return 1

        if k is self.randomcharsforP2_static[self.var_countP2] and self.killStatePlayer1 == False and self.killStatePlayer2 == False:
            self.randomcharsforP2_static[self.var_countP2] = str.capitalize(self.randomcharsforP2_static[self.var_countP2])

            os.system("cls")

            # os.system("cls")

            # print("WALKA!!!")
            # print("=================================")
            # print(Fight_Class().display_letters_toclick(Fight_Class().randomcharsforP1_static, Fight_Class().randomcharsforP2_static))
            # print("=================================\n")
            self.var_countP2 += 1
        if self.var_countP2 == 3:
            os.system("cls")
            print('Player2 killed Player1\n')
            self.var_countP2 = 0
            self.killStatePlayer1 = True  # zmiana flagi zabicia pierwszego gracza
            print(str(self.killStatePlayer1))
            return 1

    """
    Funkcja collision przyjmuje parametry odpowiedzialne za wspolrzedne jednego i drugiego gracza gdzie:
    x1,y1 = wspolrzedna x i y gracza nr 1
    x2,y2 = wspolrzedna x i y gracza nr 2
    Jezeli dwaj gracze sa od siebie oddaleni na 1 kratke funkcja zwraca wartosc True
    Funkcje nalezy zaimplementowac w glownej petly gry
    """

    def collision(self, x1, y1, x2, y2):
        if (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) <= 1:  # obliczanie odleglosci miedzy dwoma playerami
            return True

    """
    Funckja randomcharsforP1 losuje znaki z x c dla gracza 1 i je zwraca
    Funkcja uzywana w klasie Variable, znaki przypisane na stale podczas walki do zmiennych randomcharsforP1_static
    """

    def randomcharsforP1(self):

        chars1 = ['z', 'x', 'c']  # litery z ktorych program losuje
        charsForPlayer1 = []
        i = len(chars1)
        while i > 0:
            w = random.randint(0, 2)
            if chars1[w] not in charsForPlayer1:
                charsForPlayer1.append(chars1[w])  # jezeli danej litery nie ma jeszcze w nowej liscie to dodaj
                i -= 1
        return charsForPlayer1

    def randomcharsforP2(self):

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
    Funckja display_letters_toclick wyswietla w odpowiedniej kolejnosci informacje w zwiazku z sekwencja wcisniecia klawiszy
    Przyjmuje parametry z klasy Variable, zamienia na stringi i dolacza do glownego stringa.
    Uzyta jest w funkcji on_press_checkinputkey
    """

    def display_letters_toclick(self, var1, var2):

        lettersString = "Player 1: "  # glowny string funkcji

        for i in var1:
            lettersString += i  # doklejanie liter ktore maja zostac wyswietlone dla gracza 1
            lettersString += " "
        lettersString += "\tPlayer 2: "

        for i in var2:
            lettersString += i  # doklejanie liter ktore maja zostac wyswietlone dla gracza 2
            lettersString += " "
        return lettersString  # zwracanie stringa z sekwencja klawiszy



k=Fight_Class()
k.chars_randomization()

while True:
    if k.collision(1,1,1,2):

        print("WALKA!!!")
        print("=======================================")
        print(k.display_letters_toclick(k.randomcharsforP1_static, k.randomcharsforP2_static))
        print("=======================================\n")
        key = getch().decode("utf-8")
        k.on_press_checkinputkey(key)



    def fight_interface(self):

             print("WALKA!!!")
             print("=======================================")
             print(self.display_letters_toclick(self.randomcharsforP1_static, self.randomcharsforP2_static))
             print("=======================================\n")


# k=Fight_Class()
# k.chars_randomization()
#
# while True:
#     if k.collision(1,1,1,2):
#
#         k.fight_interface()
#         key = getch().decode("utf-8")
#         k.on_press_checkinputkey(key)

