import java.util.ArrayList;
import java.util.Scanner;

public class Game {

    private int width;
    private int height;
    private Board board;
    private static final int TILESIZE = 5;
    private ArrayList<Tile> tiles;
    private int currentTile;
    private int score;

    public Game(int width, int height, String tileFile) {
        this.width = width;
        this.height = height;
        this.board = new Board(width, height);
        this.tiles = new ArrayList<>();
    }

    private void addTile(String tile) {
        Tile newTile = new Tile(tile);
        this.tiles.add(newTile);
    }

    private void loadTiles() {
        addTile("1111100000000000000000000");
        addTile("1000010000100001000010000");
        addTile("1100011100000000000000000");
        addTile("0000010000011100000010000");
    }

    private int[] getMove() {
        Scanner in = new Scanner(System.in);
        int[] move = new int[3];
        System.out.println("Please enter your move.");

        System.out.print("Row: ");
        move[0] = in.nextInt();

        System.out.print("Col: ");
        move[1] = in.nextInt();

        System.out.print("Rotations: ");
        move[2] = in.nextInt();

        return move;
    }

    private void gameLoop() {
        int turns = 0;

        while (turns < 3) {
            // Print the board
            this.board.printBoard();
            System.out.println();
            // Print the tile
            this.tiles.get(currentTile).printTile();
            System.out.println();

            boolean valid = false;
            while (!valid) {
                // Ask for the move
                int[] move = getMove();

                // Check move
                if (board.checkMove(move, tiles.get(currentTile))) {
                    board.placeTile(move, tiles.get(currentTile));
                    currentTile++;
                    currentTile = currentTile % tiles.size();
                    turns++;
                    valid = true;
                } else {
                    System.out.println("Invalid Move, Try again.");
                }
            }
        }

    }

    public static void main(String args[]) {
        Game game = new Game(10, 10, "tiles");
        game.loadTiles();
        game.gameLoop();

    }
}
