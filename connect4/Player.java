package connect4;

/**
 * One of the two players in Connect 4.
 */
public enum Player {
    /**
     * {@link Player} who uses the red chips, in Connect 4.
     */
    RED,
    /**
     * {@link Player} who uses the yellow chips, in Connect 4.
     */
    YELLOW;

    /**
     * Get this {@link Player}'s opponent.
     *
     * <p>
     * {@code RED}'s opponent is {@code YELLOW} and vice versa.
     *
     * @return this {@link Player}'s opponent
     */
    public Player opponent() {
        return switch (this) {
            case RED -> YELLOW;
            case YELLOW -> RED;
        };
    }
}
