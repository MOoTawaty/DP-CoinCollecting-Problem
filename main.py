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

    # this is a trying example with specific board values & the maximum coins picked is 5
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

        for i in range(self.row):  # 5 rows
            print(self.gameBoard[i])
        print('\n')

    def game_algorithm(self):
        board_copy = self.gameBoard
        for i in range(self.row):  # 5 rows
            for j in range(self.column):  # 6 column
                if i == 0 and j == 0:
                    board_copy[i][j] = 0 + board_copy[i][j]
                elif i == 0:
                    board_copy[i][j] = max(0, board_copy[i][j - 1]) + board_copy[i][j]
                elif j == 0:
                    board_copy[i][j] = max(board_copy[i - 1][j], 0) + board_copy[i][j]
                else:
                    board_copy[i][j] = max(board_copy[i - 1][j], board_copy[i][j - 1]) + board_copy[i][j]
            # print(board_copy[i])

        return board_copy[self.row - 1][self.column - 1]


player = CoinCollecting(5, 6)
# player.initialize_TheBoard()
player.trying()
print("the maximum number of coins picked:", player.game_algorithm())

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
