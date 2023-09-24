from errors import ColumnFullError, GameOverError
from Checker import Checker
from GameState import GameState

class Connect4:
    _game_state = GameState.TURN_PLAYER_1
    _current_player = 1
    _board = []
    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6 
    WIN_LENGTH = 4

    def __init__(self):
        self.clear_board()

    def current_player(self):
        return self._current_player
    
    def __current_player_checker(self):
        if self._current_player == 1:
            return Checker.YELLOW
        else:
            return Checker.RED
    
    def __current_player_win_game_state(self):
        if self._current_player == 1:
            return GameState.WIN_PLAYER_1
        else:
            return GameState.WIN_PLAYER_2
    
    def __switch_current_player(self):
        if self._current_player == 1:
            self._current_player = 2
            self._game_state = GameState.TURN_PLAYER_2
        else:
            self._current_player = 1
            self._game_state = GameState.TURN_PLAYER_1
    
    def __is_game_in_progress(self):
        return GameState.TURN_PLAYER_1 or GameState.TURN_PLAYER_2
    
    # ????
    def game_state(self):
        return self._game_state
    
    def board(self):
        return self._board
    
    def clear_board(self):
        for _ in range(self.BOARD_HEIGHT):
            self._board.append([Checker.EMPTY] * self.BOARD_WIDTH)

    def is_valid_move(self, col):
        col_index = col - 1
        try:
            if not self.__is_game_in_progress():
                raise GameOverError
            elif (col < 1 or col > self.BOARD_WIDTH):
                raise ValueError
            elif not any([row[col_index] is Checker.EMPTY for row in self._board]):
                raise ColumnFullError
            return True
        
        except GameOverError:
            print("The game is over and no more moves can be made")
        except ValueError:
            print(f"Column {col} is out of range of the board\'s size: 1-{self.BOARD_WIDTH}")
        except ColumnFullError:
            print(f"Column {col} already has {self.BOARD_HEIGHT} checkers and can\'t accept any more")
    
    def __update_game_state(self, row_index, col_index):
        # check tie
        if not any([any([checker is Checker.EMPTY for checker in row]) for row in self._board]):
            game._game_state = GameState.TIE
            return
        
        # check horizontal win
        # self.BOARD_WIDTH - self.WIN_LENGTH + 1 = 7 - 4 + 1 = 4 --> [0-3]
        for i in range(self.BOARD_WIDTH - self.WIN_LENGTH + 1):
            if all([checker is self.__current_player_checker() for checker in self._board[i, i+self.WIN_LENGTH]]):
                game._game_state = self.__current_player_win_game_state()
                return
        
        # check vertical win
        # for i in range(self.BOARD_HEIGHT - self.WIN_LENGTH + 1):
        #     if all([True for row in self._board if row[col_index] is self.__current_player_checker()]):
        #         game._game_state = self.__current_player_win_game_state()
        #         return
            
        # check positive diagonal win

        # check negative diagonal win

    def move(self, col):
        col_index = col - 1
        # check if the move is valid
        # if the move is not valid, an error is thrown
        game.is_valid_move(col)

        # find the row where the checker will drop to
        row_index = max(row_index for row_index, row in enumerate(self._board) if row[col_index] is Checker.EMPTY)
        
        # update the board with the new piece
        self._board[row_index][col_index] = self.__current_player_checker()
        
        # update the game state based on the move made
        self.__update_game_state(row_index, col_index)

        # if the game is in progress, switch to the next player
        if self.__is_game_in_progress():
            self.__switch_current_player()
        
        return self._game_state

def make_move(game, col):
    print(f"current player: {game.current_player()}")
    game_state = game.move(col)
    print('\n'.join([' | '.join([checker.value for checker in row]) for row in game.board()]))
    print(game_state.value)
    print()

game = Connect4()

make_move(game, 1)
make_move(game, 1)
make_move(game, 3)

