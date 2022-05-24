from packages.game import Game

if __name__ == '__main__':
    game : Game = Game(board =  [4, 3], snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]], depth = 3)

    game.run_board_tests()
    game.run_snake_tests()
    game.run_depth_tests()

    game.create_board_matrix()
    game.search_paths()

    print(game.n_paths)