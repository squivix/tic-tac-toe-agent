import random


class GreedyPlayer:
    def __init__(self, play_as):
        self.play_as = play_as

    def get_next_move(self, state):
        empty_spots = [(i, j) for i in range(3) for j in range(3) if state[i][j] == ""]

        # Check if we can win in the next move
        for row in range(3):
            for col in range(3):
                if state[row][col] == "":
                    state[row][col] = self.play_as
                    if self._check_winner(state, self.play_as):
                        return row, col
                    state[row][col] = ""  # Reset the spot

        # Check if the opponent can win in the next move and block them
        opponent = "O" if self.play_as == "X" else "X"
        for row in range(3):
            for col in range(3):
                if state[row][col] == "":
                    state[row][col] = opponent
                    if self._check_winner(state, opponent):
                        return row, col
                    state[row][col] = ""  # Reset the spot

        # Choose a random empty spot
        if len(empty_spots) > 0:
            return random.choice(empty_spots)

    def _check_winner(self, state, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(state[i][j] == player for j in range(3)) or all(state[j][i] == player for j in range(3)):
                return True
        if all(state[i][i] == player for i in range(3)) or all(state[i][2 - i] == player for i in range(3)):
            return True
        return False
