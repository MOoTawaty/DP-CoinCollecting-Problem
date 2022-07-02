import random


class CoinCollecting:
    # gameBoard = [][]

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gameBoard = [[0] * self.column for i in range(self.row)]     #[ [None] * 5 for i1 in range(6) ]
        print(self.gameBoard)

    def initialize_TheBoard(self):
        random_List = random.sample(range(1, 31), 15)
        # The relationship between number of matrix cell and its row & column
        for i in random_List:
            ch = int(i / self.column)  # 5
            if i % self.column == 0:
                row = ch - 1
            else:
                row = ch
            column = i - row * self.column - 1
            self.gameBoard[row][column] = 1

        print(self.gameBoard[0])
        print(self.gameBoard[1])
        print(self.gameBoard[2])
        print(self.gameBoard[3])
        print(self.gameBoard[4])
        print("Random list:", random_List)


player = CoinCollecting(5, 6)
player.initialize_TheBoard()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
