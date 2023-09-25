from enum import Enum

class GameState(Enum):
    def __str__(self):
        return str(self.value)
    
    TURN_PLAYER_1 = 'Player 1\'s turn'
    TURN_PLAYER_2 = 'Player 2\'s turn'
    TIE = 'The game has ended in a tie'
    WIN_PLAYER_1 = 'Player 1 wins'
    WIN_PLAYER_2 = 'Player 2 wins'