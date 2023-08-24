import random

from utils import get_possible_moves


class RandomPlayer:
    def __init__(self, play_as):
        self.play_as = play_as

    def get_next_move(self, state):
        possible_moves = get_possible_moves(state, self.play_as)
        if len(possible_moves) > 1:
            return random.choice(possible_moves)
