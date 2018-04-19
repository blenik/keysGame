from pynput import keyboard




class player(object):

    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_x

        punkty = 0
        wynik = 0

    def move_up(self, map):
        if map[self.x -1][self.y ] == "k" :
            self.x -= 1
            self.punkty += 1
        elif map[self.x -1][self.y ] == " " :
            self.x -= 1

    def move_down(self, map):
        if map[self.x -1][self.y ] == "k" :
            self.x -= 1
            self.punkty += 1
        if map[self.x +1] [self.y]  == " ":
            self.x += 1

    def move_right(self, map):
        if map[self.x -1][self.y ] == "k" :
            self.x -= 1
            self.punkty += 1
        if map[self.x ] [self.y +1] == " ":
            self.y += 1

    def move_left(self, map):
        if map[self.x -1][self.y ] == "k" :
            self.x -= 1
            self.punkty += 1
        if map[self.x ] [self.y -1] == " ":
            self.y -= 1







