import java.util.Optional;
import java.util.Scanner;

import connect4.Game;
import connect4.GameResult;
import connect4.Player;
import connect4.Game.Status;

public class CLI {
    
    private void drawBoard(Optional<Player>[][] board) {
        // this is definitely not the prettiest code out there
        // feel free to rewrite this if you want
        
        for (Optional<Player>[] row : board) {
            for (int col_index = 0; col_index < row.length; col_index++) {
                if (col_index == 0) {
                    System.out.print("|_ ");
                }
                else {
                    System.out.print(" _|_ ");
                }
                     
                if (row[col_index].isPresent()) {
                    if (row[col_index].get() == Player.RED) {
                        System.out.print("R");
                    }
                    else if (row[col_index].get() == Player.YELLOW) {
                        System.out.print("Y");
                    }
                }
                else {
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
            }
            else if (turnStatus.player() == Player.YELLOW) {
                System.out.println("Yellow's turn");
            }
        }

        // status can also indicate whether the game has ended
        // code here for printing red win/yellow win/tie
    }


    /* Assignment:
    Write code that uses that API, producing a simple text-based client 
    that allows one human player to play against an automatic computer opponent. 
    The computer opponent does not need to be good at the game; 
    it may, for instance, randomly play a checker in a valid column at each turn.
    */
    public static void main(String args[]) {
    
        CLI cli = new CLI();

        Scanner scanner = new Scanner(System.in);

        // while loop probably somewhere here like how you did it in Python
        // honestly, probably very similar code to what we did for our API
        // except that for this assignment, we will have a computer 
        // who will use .getPossibleMoves() and then make a random valid move

        // the documentation is kind of a lot but in essence, they have a 
        // very similar design to us

        Game game = new Game(Player.RED);
        cli.printStatus(game.getStatus());

        cli.drawBoard(game.getBoard());

        System.out.println(game.getTurn());

        // pretty sure you have to do something like 
        // game.move(game.getTurn(), col)



    }
}


/*
Notes
- why does move take in the player? Perhaps it would be more connivent if move 
just took in col and made the move for the current player automatically? 
An exception is thrown if the player is moving out of turn so I don't see why
this needs to be a parameter as you would always just put in the current player.

- is it worth for move to be more specific about why an IllegalStateException 
was thrown? So specifying that the the column is full, the game is over, etc.?
Possibly through the use of custom errors? Not sure if the user really needs this info tho.

- perhaps be more clear in the documentation what a board is comprised of.
the return type implies it is a 2d array of Players and getSquare() mentions that
an empty cell is Optional.empty(), but it might be clearer if this information
was explicit within getBoard()'s definition

*/

