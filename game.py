#the project is divided into sections. 
#edit only your section!
#comment all yours code!

#section 0: global
from InterfaceCreator import InterfaceCreator
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




#section 4: randomization




#section 5: rendering




#section 6: interface


interfacePrinter=InterfaceCreator(PLANSZA_SIZE,"*") # tworzy instancje creatora interfejsu 
# dalej trzeba by sie bawic nim w miejscu gdzie sa dodawane punkty i wynik 
# i printowac w miejscu drukowaniu mapy
interfacePrinter.print_interface()
