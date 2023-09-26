import sys
import os

# Get the parent directory of the current script (Connect4CLI.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir + "\\Connect4")

from Connect4 import GameState
import errors
from Connect4 import Connect4

def draw_board(board):
    """
    Draws the board to the console.
    :param board: The game board to draw.
    """
    for row in board:
        for index, cell in enumerate(row):
            if (index == 0):
                print("|_", end=' ')
            else:
                print("_|_", end=' ')
            print(cell, end=' ')
        print("_|")


def play(game):
    """
    Plays the game.
    :param game: The game object.
    """
    while True:
        # ask player for input
        print("Enter a column number to drop a checker into: ")
        column = int(input())

        try:
            state = game.drop_checker(column)
            print(state)

            if state == GameState.WIN_PLAYER_1 or state == GameState.WIN_PLAYER_2 or state == GameState.TIE:
                break
        except (errors.ColumnOutOfRangeError, errors.ColumnFullError, errors.GameOverError) as error:
            print(error)
            continue

        draw_board(game.board())
        continue


print("Welcome to Connect 4!")
print("---------------------")

while True:

    # initialize game
    game = Connect4()

    print("Player 1 is Yellow")
    print("Player 2 is Red")
    print(game.current_game_state())
    draw_board(game.board())

    # play in two human players mode
    play(game)

    print("Game over.")
    print("Final board:")
    draw_board(game.board())

    print("Start a new game? (y/n):")
    response = input()
    if response != 'y':
        break
