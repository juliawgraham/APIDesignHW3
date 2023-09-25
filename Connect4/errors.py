class ColumnFullError(Exception):
    "Raised when the move is attempting to place a checker in a full column"
    pass

class GameOverError(Exception):
    "Raised when the game is over and no more moves can be made"
    pass