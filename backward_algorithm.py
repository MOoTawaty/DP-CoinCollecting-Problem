import game_algorithm


class BackwardGameAlgorithm(game_algorithm.Game):

    def path(self):

        # to accessing the values in the board in reverse mode
        row = self.row - 1  # 4
        column = self.column - 1  # 5

        # playing the first and last values in the board
        self.gameBoard[row][column] = '*'

        # finish when i=1 as first rew already assigned
        while row >= 1:
            if column != 0 and (self.gameBoard[row][column - 1] > self.gameBoard[row - 1][column]):  # leftward
                # moving to the left
                self.gameBoard[row][column - 1] = '*'
                column = column - 1
            else:
                # moving to the up
                self.gameBoard[row - 1][column] = '*'  # upward
                row = row - 1

        # the remaining cells path of the first row
        column = column - 1
        while column >= 0:
            self.gameBoard[0][column] = '*'
            column = column - 1

        return self.gameBoard
