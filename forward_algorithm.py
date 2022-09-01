import game_algorithm


class ForwardGameAlgorithm(game_algorithm.Game):

    def forward_game_algorithm(self):

        # this algorithm follows the dynamic programing principle
        # for the coin_collecting problem
        for i in range(self.row):  # 5 rows
            for j in range(self.column):  # 6 column
                if i == 0 and j == 0:
                    self.gameBoard[i][j] = 0 + self.gameBoard[i][j]
                elif i == 0:
                    self.gameBoard[i][j] = max(0, self.gameBoard[i][j - 1]) + self.gameBoard[i][j]
                elif j == 0:
                    self.gameBoard[i][j] = max(self.gameBoard[i - 1][j], 0) + self.gameBoard[i][j]
                else:
                    self.gameBoard[i][j] = max(self.gameBoard[i - 1][j], self.gameBoard[i][j - 1]) + self.gameBoard[i][
                        j]
            print(self.gameBoard[i])
        # getting the maximum value picked from the initialized values
        maxCoinPicked = self.gameBoard[self.row - 1][self.column - 1]
        return maxCoinPicked
