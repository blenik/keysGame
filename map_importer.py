# coding=utf-8
import os
import sys


# funkcja odczytujaca plik z mapa i wpisanie jej do macierzy 'lista'
def readLevelsFromFileToArray(lista, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                lines = file.read().splitlines()
                file.close()
                for line in lines:
                    lista.append([c for _, c in enumerate(line)])
            except IOError:
                print("Could not read file:", filename)
                sys.exit()
    else:
        print("There is not any file with map!")
    return lista


# funkcja wyswietlajaca mape
def printTheMap(map):
    for row in map:
        print(''.join([str(elem) for elem in row]))