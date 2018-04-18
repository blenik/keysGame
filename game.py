#the project is divided into sections. 
#edit only your section!
#comment all yours code!

#section 0: global
from InterfaceCreator import InterfaceCreator
from movement_2 import player
PLANSZA_SIZE=22




#section 1: map

# odczytanie pliku z mapa
file = open('Level_1_Template.txt', 'r')
BoardGameList = file.read().splitlines()
file.close()

# lista - jest macierza mapy
lista=list()
for line in BoardGameList:
    lista.append([c for _,c in enumerate(line)])

# wyswietlenie mapy
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






#section 4: randomization




#section 5: rendering




#section 6: interface


interfacePrinter=InterfaceCreator(PLANSZA_SIZE,"*") # tworzy instancje creatora interfejsu 
# dalej trzeba by sie bawic nim w miejscu gdzie sa dodawane punkty i wynik 
# i printowac w miejscu drukowaniu mapy
interfacePrinter.print_interface()
