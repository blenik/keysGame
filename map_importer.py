# coding=utf-8
import os
import sys

# funkcja odczytujaca plik z mapa i wpisanie jej do macierzy 'lista'
def readingLevelsFromFileToArray(lista):
    if os.path.exists('Level_1_Template.txt'):
        with open('Level_1_Template.txt', 'r') as file:
            try:
                boardgame = file.read().splitlines()
                file.close()
                for line in boardgame:
                    lista.append([c for _, c in enumerate(line)])
            except IOError:
                print("Could not read file:", 'Level_1_Template.txt')
                sys.exit()
    else:
        print("There is not any file with map!")
    return lista


# funkcja wyswietlajaca mape
def printingTheMap(map):
    for row in map:
        print(''.join([str(elem) for elem in row]))