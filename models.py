from utils import getCenter

class Letter:
    position = (0, 0)
    def __init__(self, character, location, score=1, multiplier=None):
        self.character = character
        self.location = location
        self.score = score
        self.multiplier = multiplier

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
        self.center = getCenter(*value)

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, value):
        value = value.replace('\n', '')
        value = value.upper()
        self._character = value

    def __str__(self):
        return self.character

    def __repr__(self):
        return f'Letter({self.character!r}, {self.location!r}, {self.center!r}, {self.score!r}, {self.multiplier!r})'

class Board:
    def __init__(self, letters):
        self.letters = letters
        self.makeBoard()

    def makeBoard(self):
        if len(self.letters) < 16:
            raise ValueError("16 boxes must be present")
        self.board = []
        rowSorted = sorted(self.letters, key=lambda x: x.center[1])
        for i in range(4):
            row = sorted(rowSorted[i*4:i*4+4], key=lambda x: x.center[0])
            for j in range(4):
                # assign position the individual letters. 
                row[j].position = (i, j)
            self.board.append(row)
        self.makeAdjacencyList()

    def getInstances(self, letter):
        return [x for x in self.letters if x.character == letter]

    def makeAdjacencyList(self):
        adjacencyList = {}
        for i in range(4):
            for j in range(4):
                letter = self.board[i][j]
                if letter not in adjacencyList:
                    adjacencyList[letter] = []
                if i != 0:
                    if j != 0:
                        adjacencyList[letter].append(self.board[i - 1][j - 1])
                    adjacencyList[letter].append(self.board[i - 1][j])
                    if j != 3:
                        adjacencyList[letter].append(self.board[i - 1][j + 1])
                if j != 0:
                    adjacencyList[letter].append(self.board[i][j - 1])
                if j != 3:
                    adjacencyList[letter].append(self.board[i][j + 1])        
                if i != 3:
                    if j != 0:
                        adjacencyList[letter].append(self.board[i + 1][j - 1])
                    adjacencyList[letter].append(self.board[i + 1][j])
                    if j != 3:
                        adjacencyList[letter].append(self.board[i + 1][j + 1])
        self.adjacencyList = adjacencyList

    def printAdjacencyList(self):
        for x in self.adjacencyList:
            chars = [_.character for _ in self.adjacencyList[x]]
            print(x.character, ':', chars)

    def getAdjacent(self, letter):
        return self.adjacencyList[letter]

    def __str__(self):
        string = ''
        for i in range(4):
            for _ in self.board[i]:
                string += _.character + '\t'
            string += '\n'
        return string
    



if __name__ == '__main__':
    import pickle
    with open('sample_board.dat', 'rb') as file:
        sample_board = pickle.load(file)
    sample_board.printAdjacencyList()