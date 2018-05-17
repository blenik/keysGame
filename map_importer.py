# coding=utf-8
import os
import sys


class MapImporter(object):

# funkcja odczytujaca plik z mapa i wpisanie jej do macierzy 'list'
    def readLevelsFromFileToArray(self, list, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as fileStream:
                try:
                    self.readLinesFromFileStream(list, fileStream)
                    fileStream.close()
                except IOError:
                    print("Could not read file:", filename)
                    sys.exit()
        else:
            print("There is not any file with map!")
        return list

    def readLinesFromFileStream(self, list, fileStream):
        lines = fileStream.read().splitlines()
        for line in lines:
            list.append([c for _, c in enumerate(line)])
        return list

    # funkcja wyswietlajaca mape
    def printTheMap(self, map):
        for row in map:
            print(''.join([str(elem) for elem in row]))
