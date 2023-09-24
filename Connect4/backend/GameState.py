from enum import Enum

class GameState(Enum):
    IN_PROGRESS = 'the game is in progress'
    TIE = 'the game has ended in a tie'
    WIN_PLAYER_1 = 'player 1 win\'s'
    WIN_PLAYER_2 = 'player 2 win\'s'