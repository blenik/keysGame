#the project is divided into sections. 
#edit only your section!
#comment all yours code!

#section 0: global
from InterfaceCreator import InterfaceCreator
PLANSZA_SIZE=22


#section 1: map

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



#section 2: fight




#section 3: moving




#section 4: randomization




#section 5: rendering




#section 6: interface


interfacePrinter=InterfaceCreator(PLANSZA_SIZE,"*") # tworzy instancje creatora interfejsu 
# dalej trzeba by sie bawic nim w miejscu gdzie sa dodawane punkty i wynik 
# i printowac w miejscu drukowaniu mapy
interfacePrinter.print_interface()
