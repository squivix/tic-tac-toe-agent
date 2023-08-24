from enum import Enum

BOARD_LENGTH = 3
VALID_MARKS = ["X", "O"]
VALID_STATE_ELEMENTS = VALID_MARKS + [""]


class GameResult(Enum):
    WIN = "Win"
    LOSS = "Loss"
    DRAW = "Draw"
    INCOMPLETE = "Incomplete"

    def __str__(self) -> str:
        return self.value
