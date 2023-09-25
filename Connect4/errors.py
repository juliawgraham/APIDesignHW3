class ColumnFullError(Exception):
    "Raised when the move is attempting to place a checker in a full column."

    def __init__(self, col, height):
        """
        :param int col: The column associated with the error.
        :param int height: The height of the board.
        """
        message = f"Column {col} already has {height} checkers and can\'t accept any more"
        super().__init__(message)
    
    pass

class ColumnOutOfRangeError(Exception):
    "Raised when the move is attempting to place a checker in a column that is out of range of the board."

    def __init__(self, col, width):
        """
        :param int col: The column associated with the error.
        :param int width: The width of the board.
        """
        message = f"Column {col} is out of range of the board\'s size of 1-{width}"
        super().__init__(message)
    
    pass

class GameOverError(Exception):
    "Raised when the game is over and no more moves can be made."

    def __init__(self):
        message = "The game is over and no more moves can be made"
        super().__init__(message)
    
    pass

class InvalidPlayerTurnError(Exception):
    "Raised when the player turn inputted is invalid."

    def __init__(self):
        message = f"The inputted player turn is invalid."
        super().__init__(message)
    
    pass