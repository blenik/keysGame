
# funkcja odczytujaca plik z mapa i wpisanie jej do macierzy 'lista'
def readingLevelsFromFileToArray(lista):
    file = open('Level_1_Template.txt', 'r')  # 'r' - plik tylko do odczytu
    boardgame = file.read().splitlines()
    file.close()
    for line in boardgame:
        lista.append([c for _, c in enumerate(line)])
    return lista


# funkcja wyswietlajaca mape
def printingTheMap(map):
    for row in map:
        print(''.join([str(elem) for elem in row]))
