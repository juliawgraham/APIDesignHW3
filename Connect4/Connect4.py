from CellState import CellState
from GameState import GameState
from errors import ColumnFullError, ColumnOutOfRangeError, GameOverError, InvalidPlayerTurnError

class Connect4:
    """
    The Connect4 class provides users the ability to play games of Connect 4 
    following the `standard connect 4 rules <https://en.wikipedia.org/wiki/Connect_Four>`_.
    """
    _game_state = GameState.TURN_PLAYER_1
    _current_player = 1
    _board = []
    _BOARD_WIDTH = 7
    _BOARD_HEIGHT = 6 
    _WIN_LENGTH = 4

    def __init__(self, first_player_turn: GameState = GameState.TURN_PLAYER_1):
        """
        The constructor creates an instance of the Connect4 class, 
        initializes an empty board, and sets the player to play first.

        :param GameState - optional first_player_turn: enum of :data:`GameState.GameState.TURN_PLAYER_1` or :data:`GameState.GameState.TURN_PLAYER_1`, which represents the player to play first. By default, player 1 plays first.
        :raises InvalidPlayerTurnError: The inputted first player turn is not valid.
        """
        self.__reset_game(first_player_turn)

    def __reset_game(self, first_player_turn: GameState = GameState.TURN_PLAYER_1):
        """        
        Reset the game by clearing the board and setting a new first player.

        :param GameState - optional first_player_turn: enum of :data:`GameState.GameState.TURN_PLAYER_1` or :data:`GameState.GameState.TURN_PLAYER_1`, which represents the player to play first. By default, player 1 plays first.
        :raises InvalidPlayerTurnError: The inputted first player turn is not valid.
        """
        if not (first_player_turn is GameState.TURN_PLAYER_1 or first_player_turn is GameState.TURN_PLAYER_1):
            raise InvalidPlayerTurnError()
        
        self._game_state = first_player_turn
        if first_player_turn is GameState.TURN_PLAYER_1:
            self._current_player = 1
        else:
            self._current_player = 2

        self._board = []
        
        for _ in range(self._BOARD_HEIGHT):
            self._board.append([CellState.EMPTY] * self._BOARD_WIDTH)

    def current_player(self):
        """
        Get the current player, as in the player whose turn it currently is.
        
        If the game is over, the current player will be the player who made the last move
        since there are no more valid turns left in the game.

        :returns: The current player, which is either player 1 or player 2.
        :rtype: int of value `1` or `2`.
        """
        return self._current_player
    
    def __current_player_cell_state(self):
        """
        Get the cell state associated with the current player.
        """
        if self._current_player == 1:
            return CellState.CHECKER_PLAYER_1
        else:
            return CellState.CHECKER_PLAYER_2
    
    def __current_player_win_game_state(self):
        """
        Get the winning game state associated with the current player.
        """
        if self._current_player == 1:
            return GameState.WIN_PLAYER_1
        else:
            return GameState.WIN_PLAYER_2
    
    def __switch_current_player(self):
        """
        Switch the current player, which switches the current player int and the turn game state.
        """
        if self._current_player == 1:
            self._current_player = 2
            self._game_state = GameState.TURN_PLAYER_2
        else:
            self._current_player = 1
            self._game_state = GameState.TURN_PLAYER_1
    
    def __is_game_in_progress(self):
        """
        Check if the game is in progress.
        """
        return (self._game_state is GameState.TURN_PLAYER_1) or (self._game_state is GameState.TURN_PLAYER_2)
    
    def current_game_state(self):
        """
        Get the current game state.

        :returns: The current game state.
        :rtype: :mod:`GameState`
        """
        return self._game_state
    
    def board(self):
        """
        Get the current board, which is a 2-dimensional list of :mod:`CellState`\'s.

        :returns: The current board of size 6 x 7. Position [0,0] is the top left of the board. 
        :rtype: List[List[:mod:`CellState`]]
        """
        return self._board

    def is_valid_move(self, col: int):
        """
        Check if dropping the checker into the given column is a valid move or not.
        If the move is invalid, an exception is raised that specifies why the move was invalid.

        :param int col: The column, from 1 to 7, where the checker should be dropped into.
        :returns: True if the move is valid.
        :rtype: bool
        :raises TypeError: The inputted column is not an int.
        :raises GameOverError: The game is over.
        :raises ColumnOutOfRangeError: The inputted column is not between 1 and 7.
        :raises ColumnFullError: The column is full of checkers.
        """
        
        try:
            col = int(col)
        except:
            raise TypeError("The inputted column must be an int")

        col_index = col - 1
        if not self.__is_game_in_progress():
            raise GameOverError
        elif (col < 1 or col > self._BOARD_WIDTH):
            raise ColumnOutOfRangeError(col, self._BOARD_WIDTH)
        elif not any([row[col_index] is CellState.EMPTY for row in self._board]):
            raise ColumnFullError(col, self._BOARD_HEIGHT)
        else:
            return True
    
    def find_all_valid_moves(self):
        """
        Find all valid moves for the current player.

        :returns: A list of all columns, from 1-7, where a checker can be dropped into to make a valid move. If no valid moves can be made, the list is empty.
        :rtype: List[int]
        """

        result = []
        
        for col_index in range(self._BOARD_WIDTH):
            try:
                if self.is_valid_move(col_index+1):
                    result.append(col_index+1)
            except (GameOverError, ColumnFullError):
                pass
        
        return result

    def __update_game_state(self):
        """
        Update the game state after checking the entire board for a tie/win.
        """        
        # check tie
        if not any([any([cell_state is CellState.EMPTY for cell_state in row]) for row in self._board]):
            self._game_state = GameState.TIE
            return
        
        # check horizontal win
        for i in range(self._BOARD_HEIGHT):
            # self._BOARD_WIDTH - self._WIN_LENGTH + 1 = 7 - 4 + 1 = 4 --> [0-3]
            for j in range(self._BOARD_WIDTH - self._WIN_LENGTH + 1):
                if all([cell_state is self.__current_player_cell_state() for cell_state in self._board[i][j:j+self._WIN_LENGTH]]):
                    self._game_state = self.__current_player_win_game_state()
                    return
        
        # check vertical win
        for i in range(self._BOARD_HEIGHT - self._WIN_LENGTH + 1):
            for j in range(self._BOARD_WIDTH):
                if all([row[j] is self.__current_player_cell_state() for row in self._board[i:i+self._WIN_LENGTH]]):
                    self._game_state = self.__current_player_win_game_state()
                    return
            
        # check diagonal win
        for i in range(0, self._BOARD_HEIGHT - self._WIN_LENGTH + 1):
            for j in range(0, self._BOARD_WIDTH - self._WIN_LENGTH + 1):
                # if self._board[i+3][j] is self._board[i+2][j+1] is self._board[i+1][j+2] is self._board[i][j+3] or \
                # check positive diagonal win v
                if all([self._board[i+index][j+(self._WIN_LENGTH - 1 - index)] is self.__current_player_cell_state() for index in range(self._WIN_LENGTH)]) or \
                   all([self._board[i+index][j+index] is self.__current_player_cell_state() for index in range(self._WIN_LENGTH)]):
                  # check negative diagonal win ^
                    self._game_state = self.__current_player_win_game_state()
                    return

    def drop_checker(self, col: int):
        """
        Drop a checker for the current player into the given column.

        :param int col: The column, from 1 to 7, where the checker should be dropped into.
        :returns: The :mod:`GameState` after the move is completed.
        :rtype: :mod:`GameState`
        :raises GameOverError: The game is over.
        :raises ColumnOutOfRangeError: The inputted column is not between 1 and 7.
        :raises ColumnFullError: The column is full of checkers.

        **Example:**

        The following example shows how to play a game of connect 4 starting with player 1.
        Player 1 makes a move in column 1 (in position [5,0]) and Player 2 makes a move in column 3 (in position [5,2]).

        .. code-block:: python
            
            game = Connect4()
            print(game.current_game_state())    # prints `Player 1's turn`
            print(game.drop_checker(1))         # prints `Player 2's turn`
            print(game.drop_checker(3))         # prints `Player 1's turn`

        """

        # check if the move is valid
        # if the move is not valid, an error is thrown
        self.is_valid_move(col)

        col_index = col - 1

        # find the row where the checker will drop to
        row_index = max(row_index for row_index, row in enumerate(self._board) if row[col_index] is CellState.EMPTY)
        
        # update the board with the new piece
        self._board[row_index][col_index] = self.__current_player_cell_state()
        
        # check for a tie/win and update the game state accordingly
        self.__update_game_state()

        # if the game is still in progress, switch to the next player
        if self.__is_game_in_progress():
            self.__switch_current_player()
        
        return self._game_state


game = Connect4()
game.drop_checker("Hello")