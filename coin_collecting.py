import random


class CoinCollecting:

    # initializing 3 attributes for the game
    def __init__(self, row, column):
        self.row = row
        self.column = column
        # constructing empty game board
        self.gameBoard = [[0] * self.column for i in range(self.row)]  # [ [None] * 5 for i1 in range(6) ]

    # initialize the game board with random values
    def initialize_TheBoard(self):
        numOfCells = self.row * self.column
        random_List = random.sample(range(1, numOfCells + 1), int(numOfCells / 2))
        # The relationship between number of matrix cell and its row & column
        for i in random_List:
            row = int(i / self.column)  # 5
            if i % self.column == 0:
                row = row - 1
            column = i - row * self.column - 1
            self.gameBoard[row][column] = 1

        # printing the game board
        for i in range(self.row):  # 5 rows
            print(self.gameBoard[i])
        print()
