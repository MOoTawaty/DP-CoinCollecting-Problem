import random


class CoinCollecting:
    # gameBoard = [][]

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gameBoard = [[0] * self.column] * self.row
        print(self.gameBoard)

    def initializeTheBoard(self):
        print(self.row*self.column/2)
        randomList = random.sample(range(0, 30), 15)
        print("Random list:", randomList)



player = CoinCollecting(5, 6)
player.initializeTheBoard()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
