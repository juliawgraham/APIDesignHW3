import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

import connect4.Game;
import connect4.GameResult;
import connect4.Player;
import connect4.Game.Status;

public class CLI {

    private void drawBoard(Optional<Player>[][] board) {

        for (Optional<Player>[] row : board) {
            for (int col_index = 0; col_index < row.length; col_index++) {
                if (col_index == 0) {
                    System.out.print("|_ ");
                } else {
                    System.out.print(" _|_ ");
                }

                if (row[col_index].isPresent()) {
                    if (row[col_index].get() == Player.RED) {
                        System.out.print("R");
                    } else if (row[col_index].get() == Player.YELLOW) {
                        System.out.print("Y");
                    }
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println(" _|");
        }
    }

    private void printStatus(Status status) {
        if (status instanceof Status.Turn turnStatus) {
            if (turnStatus.player() == Player.RED) {
                System.out.println("Red's turn");
            } else if (turnStatus.player() == Player.YELLOW) {
                System.out.println("Yellow's turn");
            }
        }
    }

    private Player getPlayerColor() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Would you like to play as red or yellow? (r/y)");
            String color = scanner.nextLine();
            if (color.equals("r")) {
                return Player.RED;
            } else if (color.equals("y")) {
                return Player.YELLOW;
            } else {
                System.out.println("Invalid input. Please try again.");
            }
        }
    }

    private int getComputerMove(Game game) {
        // check all the valid moves
        // pick a random one
        // return it

        Set<Integer> possibleMoves = game.getPossibleMoves();

        // Convert the Set to a List
        List<Integer> movesList = new ArrayList<>(possibleMoves);

        // Generate a random index within the bounds of the List
        Random random = new Random();
        int randomIndex = random.nextInt(movesList.size());

        // Get the random number from the List
        int randomValue = movesList.get(randomIndex);
        return randomValue;
    }

    private int getPlayerMove(Game game) {
        // ask the player where they want to play
        // check if it's a valid move
        // return it

        Set<Integer> possibleMoves = game.getPossibleMoves();

        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter a column to play valid columns are " + possibleMoves);
            int col;
            try {
                col = scanner.nextInt();

                if (!possibleMoves.contains(col)) {
                    System.out.println("Illegal move. Please try again.");
                } else {
                    return col;
                }
            } catch (Exception e) {
                System.out.println("Invalid input. Please try again.");
                continue;
            }

        }
    }

    public static void main(String args[]) {

        CLI cli = new CLI();

        Player playerColor = cli.getPlayerColor();

        Game game = new Game(playerColor);

        while (game.getStatus() instanceof Status.Turn) {
            cli.drawBoard(game.getBoard());
            cli.printStatus(game.getStatus());

            int col;

            if (game.getTurn().get() == playerColor) {
                col = cli.getPlayerMove(game);
            } else {
                col = cli.getComputerMove(game);
            }

            game.move(game.getTurn().get(), col);

        }
        System.out.println(game.getGameResult().get());

        System.out.println("Game over!");
        System.out.println("Final board:");

        cli.drawBoard(game.getBoard());

    }
}
