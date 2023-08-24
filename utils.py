from copy import deepcopy

from constants import VALID_MARKS, BOARD_LENGTH, VALID_STATE_ELEMENTS, GameResult


def eval_state(state: list, playing_as: str):
    if playing_as not in VALID_MARKS:
        raise ValueError(f"playing_as must be one of {VALID_MARKS}")
    winner = calculate_winner(state)
    if winner is None:
        flat_state = [item for sublist in state for item in sublist]
        if "" in flat_state:
            return GameResult.INCOMPLETE
        else:
            return GameResult.DRAW
    elif winner == playing_as:
        return GameResult.WIN
    else:
        return GameResult.LOSS


def get_winner(state, player_1, player_2):
    player_1_res = eval_state(state, player_1.play_as)
    if player_1_res == GameResult.WIN:
        return player_1.name
    elif player_1_res == GameResult.LOSS:
        return player_2.name
    elif player_1_res == GameResult.DRAW:
        return GameResult.DRAW.value
    else:
        return None


def print_game_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            mark = " " if state[i][j] == "" else state[i][j]

            if j != len(state[i]) - 1:
                print(mark, end=" | ")
            else:
                print(mark)
        if i != len(state) - 1:
            print("---" * len(state[i]))


def calculate_winner(state: list):
    if len(state) != BOARD_LENGTH:
        raise ValueError("invalid state")
    winner = None
    mark_count = {key: 0 for key in VALID_MARKS}

    def update_winner(current_winner, new_winner):
        if new_winner in VALID_MARKS:
            if current_winner is not None and current_winner != new_winner:
                raise ValueError("invalid state: multiple winners")
            return new_winner
        return current_winner

    last_index = BOARD_LENGTH - 1
    diag_1_same = state[0][0]
    diag_2_same = state[0][last_index]

    for i in range(BOARD_LENGTH):
        if len(state[i]) != BOARD_LENGTH:
            raise ValueError("invalid state: board not square")
        row_same = state[i][0]
        col_same = state[0][i]
        for j in range(BOARD_LENGTH):
            if state[i][j] not in VALID_STATE_ELEMENTS:
                raise ValueError(f"invalid state: invalid mark ({state[i][j]}) expected one of {VALID_STATE_ELEMENTS}")
            if state[i][j] in mark_count:
                mark_count[state[i][j]] += 1
            if j != BOARD_LENGTH - 1:
                if state[i][j] != state[i][j + 1]:
                    row_same = None
                if state[j][i] != state[j + 1][i]:
                    col_same = None

        winner = update_winner(winner, row_same)
        winner = update_winner(winner, col_same)

        if i != BOARD_LENGTH - 1:
            if state[i][i] != state[i + 1][i + 1]:
                diag_1_same = None
            if state[i][last_index - i] != state[(i + 1)][last_index - (i + 1)]:
                diag_2_same = None

    winner = update_winner(winner, diag_1_same)
    winner = update_winner(winner, diag_2_same)
    if abs(mark_count[VALID_MARKS[0]] - mark_count[VALID_MARKS[1]]) > 1:
        raise ValueError("invalid state: turns not equal")
    return winner


def serialize_state(state):
    return "".join(["-" if item == "" else item for sublist in state for item in sublist])


def get_resulting_state(current_state, move, playing_as):
    x, y = move
    resulting_state = deepcopy(current_state)
    resulting_state[x][y] = playing_as
    return resulting_state


def get_possible_moves(state, playing_as):
    possible_next_moves = []
    res = eval_state(state, playing_as)
    if res == GameResult.INCOMPLETE:
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "":
                    possible_next_moves.append((i, j))
    return possible_next_moves
