import sys
sys.path.append('c:\\Users\\Elvis Iraguha\\Documents\\Fall 2023\\17-480,780\\hw3\\APIDesignHW3\\Connect4')

from Connect4 import GameState
from Connect4 import Connect4

def draw_board(board):
    for row in board:
        for index, cell in enumerate(row):
            if (index == 0):
                print("|_", end=' ')
            else:
                print("_|_", end=' ')
            print(cell, end=' ')
        print("_|")


def is_game_in_progress(state):
    if state == GameState.WIN_PLAYER_1:
        print("Player 1 wins!")
        return False
    elif state == GameState.WIN_PLAYER_2:
        print("Player 2 wins!")
        return False
    elif state == GameState.TIE:
        print("The game has ended in a tie.")
        return False
    return True


def input_column():
    while True:
        print("Enter a column number to drop a checker into: ")
        column = input()

        try:
            column = int(column)
            if (column < 1 or column > 7):
                print("Column number must be between 1 and 7.")
                continue
        except:
            print("Column number must be an integer.")
            continue

        return column

def valid_move(game, column):
    valid_moves = game.find_all_valid_moves()
    if column in valid_moves:
        return True
    else:
        return False

def play(game, computer=False):
    while True:
        print("It is Player " + str(game.current_player()) + "'s turn.")

        # ask player for input
        column = input_column()

        if not valid_move(game, column):
            print("Invalid move. Please try again.")
            continue

        # check if the game is still in progress or over
        state = game.drop_checker(column)
        if not is_game_in_progress(state):
            break

        draw_board(game.board())
        continue


def game_mode():
    while True:
        print("Two human players mode(h) or human vs computer mode(c)? (h/c):")
        mode = input()
        if mode == 'h':
            print("Human vs. human mode selected.")
            return "h"
        elif mode == 'c':
            print("Human vs. computer mode selected.")
            return "c"
        else:
            print("Invalid mode selected.")
            continue


print("Welcome to Connect 4!")
print("---------------------")

while True:
    game = Connect4()

    # get the game mode
    mode = game_mode()

    print("Player 1 is Yellow")
    print("Player 2 is Red")
    draw_board(game.board())

    # play in two human players mode
    if mode == 'h':
        play(game)

    # play in human vs computer mode
    elif mode == 'c':
        play(game, True)

    print("Game over.")
    print("Final board:")
    draw_board(game.board())

    print("Start a new game? (y/n):")
    response = input()
    if response != 'y':
        break
