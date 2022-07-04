import random


class CoinCollecting:
    # gameBoard = [][]

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gameBoard = [[0] * self.column for i in range(self.row)]  # [ [None] * 5 for i1 in range(6) ]
        # print(self.gameBoard)

    def initialize_TheBoard(self):
        random_List = random.sample(range(1, 31), 9)
        # The relationship between number of matrix cell and its row & column
        for i in random_List:
            row = int(i / self.column)  # 5
            if i % self.column == 0:
                row = row - 1
            column = i - row * self.column - 1
            self.gameBoard[row][column] = 1

        print(self.gameBoard[0])
        print(self.gameBoard[1])
        print(self.gameBoard[2])
        print(self.gameBoard[3])
        print(self.gameBoard[4])
        print("Random list:", random_List)

    def trying(self):
        self.gameBoard[0][4] = 1
        self.gameBoard[1][1] = 1
        self.gameBoard[1][3] = 1
        self.gameBoard[2][3] = 1
        self.gameBoard[2][5] = 1
        self.gameBoard[3][2] = 1
        self.gameBoard[3][5] = 1
        self.gameBoard[4][0] = 1
        self.gameBoard[4][4] = 1

        print(self.gameBoard[0])
        print(self.gameBoard[1])
        print(self.gameBoard[2])
        print(self.gameBoard[3])
        print(self.gameBoard[4])





player = CoinCollecting(5, 6)
# player.initialize_TheBoard()
player.trying()
#player.game_algorithm()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
