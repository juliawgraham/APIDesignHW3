from enum import Enum

class CellState(Enum):
    def __str__(self):
        """
        When printing the enum, will print the enum's value.
        """
        return str(self.value)
    
    EMPTY = ' '
    PLAYER_1_CHECKER = '1'
    PLAYER_2_CHECKER = '2'