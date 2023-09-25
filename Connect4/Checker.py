from enum import Enum

class Checker(Enum):
    def __str__(self):
        return str(self.value)
    
    EMPTY = ' '
    YELLOW = 'Y'
    RED = 'R'