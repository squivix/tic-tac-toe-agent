import itertools
import random

from constants import VALID_MARKS, BOARD_LENGTH, VALID_STATE_ELEMENTS, GameResult
from utils import eval_state, serialize_state, get_possible_moves, get_resulting_state


class TicTacToeAgent:
    def __init__(self, name: str, play_as: str, start_explore_rate: float, step_size: float):
        if play_as not in VALID_MARKS:
            raise ValueError(f"play_as must be one of {VALID_MARKS}")
        self.play_as = play_as
        self.name = name
        self.value_function = dict()
        self.explore_rate = start_explore_rate
        self.step_size = step_size

        for combination in itertools.product(VALID_STATE_ELEMENTS, repeat=BOARD_LENGTH ** 2):
            state = [list(combination[BOARD_LENGTH * i:BOARD_LENGTH * i + BOARD_LENGTH]) for i in range(BOARD_LENGTH)]
            try:
                result = eval_state(state, play_as)

                if result == GameResult.WIN:
                    self.value_function[serialize_state(state)] = 1.0
                else:
                    self.value_function[serialize_state(state)] = 0
            except ValueError:
                continue

    def play_one_turn(self, state, previous_state):
        game_res = eval_state(state, self.play_as)
        if game_res != GameResult.INCOMPLETE:
            return

        possible_moves = get_possible_moves(state, self.play_as)
        if random.random() <= self.explore_rate:
            agent_move = random.choice(possible_moves)
        else:
            optimal_move = possible_moves[0]
            max_value = self.value_function.get(
                serialize_state(get_resulting_state(state, optimal_move, self.play_as)), 0.5)

            for possible_move in possible_moves:
                value = self.value_function.get(
                    serialize_state(get_resulting_state(state, possible_move, self.play_as)), 0.5)
                if value > max_value:
                    max_value = value
                    optimal_move = possible_move
            agent_move = optimal_move

        # agent turn
        state = get_resulting_state(state, agent_move, self.play_as)
        if previous_state is not None:
            previous_value = self.value_function.get(serialize_state(previous_state), 0.5)
            current_value = self.value_function.get(serialize_state(state), 0.5)

            self.value_function[serialize_state(previous_state)] = previous_value + self.step_size * (current_value - previous_value)
        return agent_move
