import backward_algorithm
import demo_example
import forward_algorithm
import game_algorithm


# the main function of the system.
if __name__ == '__main__':
    # create empty board row*column
    row, column = 6, 6
    player = game_algorithm.Game(row, column)

    # initialize the board cells randomly
    player.initialize_TheBoard()

    # # this is a demo example to check the algorithm with row*col 5*6
    # # apply the demo board to the game
    # demo = demo_example.Demo(player.gameBoard)
    # gameBoard = demo.demo()
    # # sending demo board to be processed
    # player.demo_data(gameBoard)

    # getting maximum Coins Picked
    f_algo = forward_algorithm.ForwardGameAlgorithm
    maxCoinPicked = f_algo.max_coin_picked(player)
    print("maximum Coins Picked: ", maxCoinPicked, '\n')

    # getting path in stars
    print("path in stars: ")
    b_algo = backward_algorithm.BackwardGameAlgorithm
    b_algo.path(player)



