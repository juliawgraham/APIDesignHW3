from enum import Enum

class CellState(Enum):
    def __str__(self):
        return str(self.value)
    
    EMPTY = ' '
    PLAYER_1_CHECKER = '1'
    PLAYER_2_CHECKER = '2'