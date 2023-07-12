import numpy as np
from player import Player


class TicTacToe:
    def __init__(self):
        self.grid = np.full((3, 3), 0)
        self.player1 = Player(input("Enter you player name : "), "X", 1)
        self.player2 = Player(input("Enter you player name : "), "0", -1)
        self.value_to_str = {
            0: "",
            self.player1.value: self.player1.letter,
            self.player2.value: self.player2.letter
        }
        self.game_on = True
        self.current_player = self.player1

    def display_grid(self):
        print(np.vectorize(self.value_to_str.get)(self.grid))

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def make_a_move(self):
        while True:
            targeted_row = enter_choice(0, self.current_player)
            targeted_col = enter_choice(1, self.current_player)
            if self.grid[targeted_row, targeted_col] == 0:
                self.grid[targeted_row, targeted_col] = self.current_player.value
                break
            print("This cell has already been played.")

    def check_for_winner(self):
        checks = [
            np.sum(self.grid[:, 0]),
            np.sum(self.grid[:, 1]),
            np.sum(self.grid[:, 2]),
            np.sum(self.grid[0, :]),
            np.sum(self.grid[1, :]),
            np.sum(self.grid[2, :]),
            np.trace(self.grid),
            np.trace(np.fliplr(self.grid))
        ]
        if max(checks) == 3 or min(checks) == -3:
            print(f"{self.current_player.name} is the winner !")
            self.game_on = False
            return True
        return False

    def check_draw(self):
        if output := (0 not in self.grid):
            print("It's a draw !")
            self.game_on = False
        return output


def enter_choice(axis, player):
    if axis == 0:
        query = f"{player.name}, please select a row : "
    else:
        query = "Now, select a column : "
    while True:
        value = input(query)
        if value in ["0", "1", "2"]:
            break
        print("You must select a value between 0 and 2.")
    return int(value)

