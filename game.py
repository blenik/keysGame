#the project is divided into sections. 
#edit only your section!
#comment all yours code!

#section 0: global
import random
from InterfaceCreator import InterfaceCreator
PLANSZA_SIZE=22


# section 4: randomization
def init_keys(Plansza):
    i = 0
    while i < 3:
        t = random.sample(range(1, 21), 3)
        Plansza[1][t[i]] = "k"
        i = i + 1

    i = 0
    j = 1
    while 3 * j < 21:
        while i < 3:
            t = random.sample(range(1, 21), 3)
            if Plansza[3 * j][t[0]] == "#" or Plansza[3 * j][t[1]] == "#" or Plansza[3 * j][t[2]] == "#":
                i=i
            else:
                Plansza[3 * j][t[i]] = "k"
                i=i+1

        i = 0
        j = j + 1


#section 1: map

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





#section 5: rendering




#section 6: interface


interfacePrinter=InterfaceCreator(PLANSZA_SIZE,"*") # tworzy instancje creatora interfejsu 
# dalej trzeba by sie bawic nim w miejscu gdzie sa dodawane punkty i wynik 
# i printowac w miejscu drukowaniu mapy
interfacePrinter.print_interface()
