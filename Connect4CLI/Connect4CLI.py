import sys
sys.path.append('c:\\Users\\Elvis Iraguha\\Documents\\Fall 2023\\17-480,780\\hw3\\APIDesignHW3\\Connect4')

from Connect4 import Connect4
# from Connect4 import CellState

def draw_board(board):
    for row in board:
        for index, cell in enumerate(row):
            if (index == 0): print("|_", end=' ')
            elif (index == 6): print("_|", end=' ')
            else: print("_|_", end=' ')
            print(cell, end=' ')
        print()


game = Connect4()
game.drop_checker(3)

draw_board(game.board())