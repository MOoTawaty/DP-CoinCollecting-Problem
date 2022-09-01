import backward_algorithm
import demo_example
import forward_algorithm
import game_algorithm



# the main function of the system.
if __name__ == '__main__':
    # initializing player data "empty board"
    player = game_algorithm.Game(5, 6)

    # initialize the demo board to the game
    demo = demo_example.Demo(player.gameBoard)
    gameBoard = demo.demo()

    # sending demo board to be processed
    player.demo_data(gameBoard)

    # forward move
    f_algo = forward_algorithm.ForwardGameAlgorithm
    f_algo.forward_game_algorithm(player)

    print()

    # backward move
    b_algo = backward_algorithm.BackwardGameAlgorithm
    b_algo.backward_game_algorithm(player)

    # player.initialize_TheBoard()
