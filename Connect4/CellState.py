from enum import Enum

class CellState(Enum):
    def __str__(self):
        """
        When printing the enum, will print the enum's value.
        """
        return str(self.value)
    
    EMPTY = ' '
    CHECKER_PLAYER_1 = '1'
    CHECKER_PLAYER_2 = '2'