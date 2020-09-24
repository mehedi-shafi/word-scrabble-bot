# Taken from https://github.com/Utkarsh1308/Scrabble-Cheater

import pathfinder
from utils import timeit

class ScrabbleSolver:
    def __init__(self, dictFileLocation=f'scrabble/sowpods.txt'):
        self.dictFileLocation = dictFileLocation
        print(f'Initializing ScrabbleSolver')
        self.constructLibrary()

    def constructLibrary(self):
        print(f'Loading dictionary: {self.dictFileLocation}')
        with open(self.dictFileLocation, 'r') as f:
            sowpods = f.readlines()
        self.words = [x.strip() for x in sowpods]
        print('Dictionary loaded')

    def isSubset(self, word, rack):        
        letterList = rack.copy()
        # print(letterList)
        pos1 = 0
        stillOK = True
        while pos1 < len(word) and stillOK:
            # print(letterList)

            pos2 = 0
            found = False
            while pos2 < len(letterList) and not found:
                if letterList[pos2] is None:
                    pos2 += 1
                    continue
                if word[pos1] == letterList[pos2].character:
                    found = True
                else:
                    pos2 += 1
            if found:
                letterList[pos2] = None
            else:
                stillOK = False
            pos1 += 1
        return stillOK

    @timeit
    def validateByLocation(self, board, valid_words):
        paths = {}
        for word in valid_words:
            path = pathfinder.validateWord(board, word)
            if path:
                paths[word] = path
        return paths

    @timeit
    def getValidWords(self, rack):
        valid_words = []
        for word in self.words:
            # print(f'{word}: {self.IsSubset(word, rack)}')
            if self.isSubset(word, rack):
                valid_words.append(word)
        return self.getSorted(valid_words)

    def getSorted(self, words):
        # for now its just length based
        return sorted(words, key=len, reverse=True)

if __name__ == '__main__':
    solver = ScrabbleSolver()
    result = solver.getValidWords('eeetres')
    print(len(result))