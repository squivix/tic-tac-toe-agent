class OptimalPlayer:
    def __init__(self, play_as):
        self.play_as = play_as

    def get_next_move(self, state):
        if self.play_as == "X":
            opponent = "O"
        else:
            opponent = "X"

        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if state[i][j] == "":
                    state[i][j] = self.play_as
                    score = self.minimax(state, 0, False, opponent)
                    state[i][j] = ""

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def minimax(self, state, depth, is_maximizing, opponent):
        scores = {
            self.play_as: 1,
            opponent: -1,
            "tie": 0
        }

        winner = self.check_winner(state)
        if winner is not None:
            return scores[winner]

        if is_maximizing:
            max_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == "":
                        state[i][j] = self.play_as
                        score = self.minimax(state, depth + 1, False, opponent)
                        state[i][j] = ""
                        max_score = max(max_score, score)
            return max_score
        else:
            min_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == "":
                        state[i][j] = opponent
                        score = self.minimax(state, depth + 1, True, opponent)
                        state[i][j] = ""
                        min_score = min(min_score, score)
            return min_score

    def check_winner(self, state):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] != "":
                return state[i][0]
            if state[0][i] == state[1][i] == state[2][i] != "":
                return state[0][i]
        if state[0][0] == state[1][1] == state[2][2] != "":
            return state[0][0]
        if state[0][2] == state[1][1] == state[2][0] != "":
            return state[0][2]

        # Check for a tie
        if all(state[i][j] != "" for i in range(3) for j in range(3)):
            return "tie"

        return None
