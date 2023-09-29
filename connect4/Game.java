package connect4;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import java.util.Optional;

/**
 * A game of Connect 4. Consists of a board and whose turn it is (or the winner,
 * if any).
 *
 * <p>
 * Methods on {@link Game} can change the board and the {@link Game}'s
 * {@link Status Status}.
 */
public class Game {
    /**
     * Height of a Connect 4 board.
     */
    public static final int HEIGHT = 6;
    /**
     * Width of a Connect 4 board.
     */
    public static final int WIDTH = 7;

    private Status status;
    // Elements are nullable.
    private Player[][] board;

    /**
     * Return the current {@link Status Status} of the {@link Game}.
     *
     * <p>
     * The {@link Status Status} of a {@link Game} consists of whose turn it is (if
     * the game hasn't ended); or, if the game has ended, the winner (if any).
     *
     * @return the {@link Status Status} of this {@link Game}
     *
     * @see Status
     */
    public Status getStatus() {
        return status;
    }

    /**
     * Returns the {@link Player} whose turn it is to move, if the game has not
     * ended.
     *
     * @apiNote This is a convenience function. You can also pattern match on
     *          {@link getStatus}'s return value to ask whose turn it is; the
     *          benefit is that this handles the case where the game has already
     *          ended.
     *
     * @return {@link Player} whose turn it is, if the game has not ended
     */
    public Optional<Player> getTurn() {
        if (status instanceof Status.Turn status) {
            return Optional.of(status.player());
        } else {
            return Optional.empty();
        }
    }

    /**
     * Returns the result of the {@link Game}, if it has ended.
     *
     * @apiNote This is a convenience function. You can also use {@link getStatus}
     *          to check the result of the {@link Game} while handling all cases.
     *
     * @return result of the {@link Game}, if it has ended
     */
    public Optional<GameResult> getGameResult() {
        if (status instanceof Status.Ended status) {
            return Optional.of(status.result());
        } else {
            return Optional.empty();
        }
    }

    /**
     * Get which player's chip, if any, occupies the square located at the given row
     * and column.
     *
     * <p>
     * If the square is empty, this method returns {@code Optional.empty()}.
     *
     * <p>
     * {@code row} and {@code col} must be within the bounds of the Connect 4 board:
     * {@code 0 <= row < HEIGHT} and {@code 0 <= col < WIDTH}.
     *
     * @param row Row of board. The top row is index 0.
     * @param col Column of board. The leftmost column is index 0.
     * @return {@link Player} who occupies the given square, if any.
     */
    public Optional<Player> getSquare(int row, int col) {
        return Optional.ofNullable(board[row][col]);
    }

    /**
     * Return an array representing the Connect 4 board for this
     * {@link Game}.
     *
     * <p>
     * If {@code board} is the return value of this function, the element at
     * {@code board[row][col]} is equal to {@code getSquare(row, col)}.
     *
     * <p>
     * The returned array is a new array. Writing to it does not affect this
     * {@link Game}.
     *
     * @return array representing the Connect 4 board
     */
    public Optional<Player>[][] getBoard() {
        @SuppressWarnings("unchecked")
        Optional<Player>[][] array = new Optional[HEIGHT][WIDTH];
        for (int row = 0; row < HEIGHT; row++) {
            for (int col = 0; col < WIDTH; col++) {
                array[row][col] = getSquare(row, col);
            }
        }
        return array;
    }

    /**
     * Construct a new {@link Game} with an empty board, with
     * {@code startingPlayer} moving first.
     *
     * @param startingPlayer {@link Player} who moves first in the returned
     *                       {@code Game}
     */
    public Game(Player startingPlayer) {
        board = new Player[HEIGHT][WIDTH];
        status = new Status.Turn(startingPlayer);
    }

    /**
     * Create a deep copy of {@code game}.
     *
     * @param game {@link Game} to copy
     */
    public Game(Game game) {
        status = game.status;
        board = new Player[HEIGHT][WIDTH];
        for (int row = 0; row < HEIGHT; row++) {
            for (int col = 0; col < WIDTH; col++) {
                board[row][col] = game.board[row][col];
            }
        }
    }

    /**
     * Check if the game has ended (4-in-a-row or draw) and update {@code status}
     * accordingly.
     */
    private void checkGameEnd() {
        /**
         * Represents a horizontal, vertical, or diagonal line of four squares.
         */
        class Line {
            int row;
            int col;
            int rowDelta;
            int colDelta;

            Line(int row, int col, int rowDelta, int colDelta) {
                this.row = row;
                this.col = col;
                this.rowDelta = rowDelta;
                this.colDelta = colDelta;
            }

            Stream<Optional<Player>> squares() {
                return IntStream.range(0, 4).mapToObj((i) -> getSquare(row + i * rowDelta, col + i * colDelta));
            }

            Optional<Player> winningLineForPlayer() {
                List<Optional<Player>> squares = squares().collect(Collectors.toUnmodifiableList());
                for (Player player : Player.values()) {
                    if (squares.stream().allMatch((x) -> x.equals(Optional.of(player)))) {
                        return Optional.of(player);
                    }
                }
                return Optional.empty();
            }
        }

        Stream.Builder<Line> lines = Stream.builder();
        // horizontal checks
        for (int col = 0; col < WIDTH - 4; col++) {
            for (int row = 0; row < HEIGHT; row++) {
                lines.add(new Line(row, col, 0, 1));
            }
        }
        // vertical checks
        for (int col = 0; col < WIDTH; col++) {
            for (int row = 0; row < HEIGHT - 4; row++) {
                lines.add(new Line(row, col, 1, 0));
            }
        }
        // down right checks
        for (int col = 0; col < WIDTH - 4; col++) {
            for (int row = 0; row < HEIGHT - 4; row++) {
                lines.add(new Line(row, col, 1, 1));
            }
        }
        // down left checks
        for (int col = 0; col < WIDTH - 4; col++) {
            for (int row = 4; row < HEIGHT; row++) {
                lines.add(new Line(row, col, -1, 1));
            }
        }
        // Find a winning player. The first result is enough
        Optional<Player> winningPlayer = lines.build().flatMap((line) -> line.winningLineForPlayer().stream())
                .findFirst();
        if (winningPlayer.isPresent()) {
            status = new Status.Ended(GameResult.fromWinner(winningPlayer.get()));
            return;
        }

        // check for full board
        for (int col = 0; col < WIDTH; col++) {
            for (int row = 0; row < HEIGHT; row++) {
                if (board[row][col] == null) {
                    return;
                }
            }
        }
        status = new Status.Ended(GameResult.DRAW);
    }

    private Optional<Integer> highestAvailableSpace(int col) {
        for (int openRow = HEIGHT - 1; openRow >= 0; openRow--) {
            if (board[openRow][col] == null) {
                return Optional.of(openRow);
            }
        }
        return Optional.empty();
    }

    /**
     * Update the board in response to a player placing a chip into {@code col},
     * 0-indexed.
     *
     * <p>
     * If the move cannot be made, throws an exception and does not mutate the
     * board.
     *
     * <p>
     * Preconditions for a successful move:
     * <ul>
     * <li>{@code status.equals(new Status.Turn(player))}
     * <li>{@code getPossibleMoves().contains(col)}
     * </ul>
     *
     * @throws IllegalArgumentException if {@code col} is out of bounds
     * @throws IllegalStateException    if the player cannot legally move in
     *                                  {@code col}, due to game over or trying to
     *                                  play out of turn, or because that column is
     *                                  full
     *
     * @param player {@link Player} making this move
     * @param col    0-indexed column
     */
    public void move(Player player, int col) {
        if (col < 0 || col >= WIDTH) {
            throw new IllegalArgumentException();
        }

        Player currentPlayer;
        if (status instanceof Status.Turn statusTurn) {
            currentPlayer = statusTurn.player();
        } else {
            throw new IllegalStateException();
        }

        if (currentPlayer != player) {
            throw new IllegalStateException();
        }

        int openRow = highestAvailableSpace(col).orElseThrow(IllegalStateException::new);

        board[openRow][col] = currentPlayer;
        status = new Status.Turn(currentPlayer.opponent());
        checkGameEnd();
    }

    /**
     * Returns the set of all columns (0-indexed) that are valid
     * moves for either player.
     *
     * @return {@link Set} of all valid moves
     */
    public Set<Integer> getPossibleMoves() {
        Set<Integer> openCols = new HashSet<>();
        for (int col = 0; col < WIDTH; col++) {
            if (board[0][col] == null) {
                openCols.add(col);
            }
        }
        return openCols;
    }

    /**
     * Represents the status of a {@link Game}. It can be some {@link Player}'s
     * turn,
     * or a {@link GameResult} if the game has ended.
     */
    public static sealed interface Status permits Status.Turn, Status.Ended {
        /**
         * Possible status of a {@link Game}; represents that it's some {@link Player}'s
         * turn.
         *
         * @param player {@link Player} whose turn it is
         */
        public record Turn(Player player) implements Status {
        }

        /**
         * Possible status of a {@link Game}; represents that the {@code Game} has ended
         * with a result.
         *
         * @param result result of the {@link Game}
         */
        public record Ended(GameResult result) implements Status {
        }
    }
}
