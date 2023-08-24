import random

from TicTacToeAgent import TicTacToeAgent
from constants import GameResult
from utils import eval_state, get_winner, get_resulting_state, print_game_state


def main():
    start_state = [['', '', ''],
                   ['', '', ''],
                   ['', '', '']]
    agent1 = TicTacToeAgent("agent1", "X", 0.1, 0.5)
    agent2 = TicTacToeAgent("agent2", "O", 0.1, 0.5)

    games_count = 1000
    results_count = {agent1.name: 0, agent2.name: 0, GameResult.DRAW.value: 0}

    for i in range(games_count):
        previous_state = None
        game_state = start_state
        winner = get_winner(game_state, agent1, agent2)

        turn_counter = 0
        first_turn = random.randint(0, 1)
        while winner is None:
            player = agent1 if turn_counter % 2 == first_turn else agent2
            player_move = player.play_one_turn(game_state, previous_state)
            previous_state = game_state
            game_state = get_resulting_state(game_state, player_move, player.play_as)
            winner = get_winner(game_state, agent1, agent2)
            turn_counter += 1

        results_count[winner] += 1

        print(f"game {i + 1:5}, winner: {winner}")

    for result, frequency in results_count.items():
        percentage = frequency / games_count
        print(f"{result:10} {percentage:6.2%}: {'*' * int(percentage * 100)}")

    # input("Let's play against the winner of these two agents!")
    computer_opponent = agent1 if results_count[agent1.name] > results_count[agent2.name] else agent2
    winner = None
    game_state = start_state
    previous_state = None

    turn_counter = 0
    human_play_as = "X" if computer_opponent.play_as == "O" else "O"
    while winner is None:
        if turn_counter % 2 == 0:
            print("Computer trun")
            move = computer_opponent.play_one_turn(game_state, previous_state)
            play_as = computer_opponent.play_as
        else:
            print("Human turn")
            coord = input("coordinates: ")
            move = int(coord[1]), int(coord[0])
            while game_state[move[0]][move[1]] != "":
                print("space filled")
                coord = input("coordinates: ")
                move = int(coord[1]), int(coord[0])
            play_as = human_play_as
        previous_state = game_state
        game_state = get_resulting_state(game_state, move, play_as)
        winner = get_winner(game_state, agent1, agent2)
        turn_counter += 1

        print_game_state(game_state)
        print()

    print(eval_state(game_state, human_play_as))


if __name__ == '__main__':
    main()
