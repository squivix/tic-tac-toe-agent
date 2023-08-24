from GreedyPlayer import GreedyPlayer
from TicTacToeAgent import TicTacToeAgent
from constants import GameResult


def main():
    start_state = [['', '', ''],
                   ['', '', ''],
                   ['', '', '']]
    agent = TicTacToeAgent("X", 0.1, 0.5)
    games_count = 1000
    opponent = GreedyPlayer("O")
    results_count = {member: 0 for member in GameResult}
    for i in range(games_count):
        result = agent.play(start_state, opponent)
        results_count[result] += 1
        print(f"game {i + 1}, result: {result}")
    print(agent.value_function)
    for result, frequency in results_count.items():
        percentage = frequency / games_count
        print(f"{result:10} {percentage:6.2%}: {'*' * int(percentage * 100)}")


if __name__ == '__main__':
    main()
