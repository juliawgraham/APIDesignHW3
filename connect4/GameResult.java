package connect4;

import java.util.Optional;

/**
 * The result of a {@link Game}: a {@code RED} win, {@code YELLOW} win, or draw.
 */
public enum GameResult {
    /**
     * Represents a {@code RED} win.
     */
    RED_WIN {
        @Override
        public Optional<Player> winner() {
            return Optional.of(Player.RED);
        }
    },
    /**
     * Represents a {@code YELLOW} win.
     */
    YELLOW_WIN {
        @Override
        public Optional<Player> winner() {
            return Optional.of(Player.YELLOW);
        }
    },
    /**
     * Represents a draw.
     */
    DRAW {
        @Override
        public Optional<Player> winner() {
            return Optional.empty();
        }
    };

    /**
     * Get the winner for this {@link GameResult}, if any.
     *
     * <p>
     * If this result is a {@code RED} or {@code YELLOW} win, return the winning
     * player. If this result is a draw, return {@code Optional.empty()}.
     *
     * @return Player who won, if any
     */
    public Optional<Player> winner() {
        throw new AssertionError("Must override");
    }

    /**
     * Create a new {@link GameResult}, representing the given player's win.
     *
     * @param player winning player
     * @return {@link GameResult} representing {@code player}'s win
     */
    public static GameResult fromWinner(Player player) {
        return switch (player) {
            case RED -> RED_WIN;
            case YELLOW -> YELLOW_WIN;
        };
    }
}
