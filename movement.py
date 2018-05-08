from pynput import keyboard
#import modulu odczytujacego ruch z klawaiatury


#klasa ustawia i sprawdza pozycjie gracza-powoduje ruch, dodaje punkty\wynik
class player(object):

    #konstruktor, inicjalizuje pozycjie
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

        self.punkty = 0
        self.wynik = 0

    # przestawia - TO DO- usuwanie poprzedniej pozycji postaci
    def przestaw(self, x,y):
        self.x = x
        self.y = y
    #ruch w gore, jesli pole puste lub klucz, jesli klucz + punkt
    def move_up(self, plansza):
        if plansza[self.x -1][self.y ] == "k":
            self.punkty += 1
            zwracam = True
        else:
            zwracam = False

        if plansza[self.x -1][self.y ] == " " or plansza[self.x -1][self.y ] == "k":
            plansza[self.x][self.y] = " "
            plansza[self.x -1][self.y] ="p"
            self.x -= 1
        return  zwracam

    # ruch w dol, jesli pole puste lub klucz, jesli klucz + punkt
    def move_down(self, plansza):
        if plansza[self.x +1][self.y ] == "k":
            self.punkty += 1
            zwracam = True
        else:
            zwracam = False

        if plansza[self.x +1][self.y] == " " or plansza[self.x +1][self.y ] == "k":
            plansza[self.x][self.y] = " "
            plansza[self.x + 1][self.y] = "p"
            self.x += 1
        return zwracam

    # ruch w prawo, jesli pole puste lub klucz, jesli klucz + punkt
    def move_right(self, plansza):
        if plansza[self.x][self.y +1] == "k":
            self.punkty += 1
            zwracam = True
        else:
            zwracam = False
        if plansza[self.x][self.y +1] == " " or plansza[self.x ][self.y +1] == "k":
            plansza[self.x][self.y] = " "
            plansza[self.x][self.y +1] = "p"
            self.y += 1
        return zwracam

    # ruch w lewo, jesli pole puste lub klucz, jesli klucz + punkt
    def move_left(self, plansza):
        if plansza[self.x ][self.y -1] == "k":
            self.punkty += 1
            zwracam = True
        else:
            zwracam = False
        if plansza[self.x ][self.y -1] == " " or plansza[self.x ][self.y -1] == "k":
            plansza[self.x][self.y] = " "
            plansza[self.x][self.y -1] = "p"
            self.y -= 1
        return zwracam






