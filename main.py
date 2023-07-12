from tictactoe import TicTacToe

game = TicTacToe()

game.display_grid()

while game.game_on:
    game.make_a_move()
    game.display_grid()
    game.check_for_winner()
    game.check_draw()
    game.switch_player()
