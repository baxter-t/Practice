public class Board {

    private int width;
    private int height;
    private boolean[][] board;
    private static final int TILESIZE = 5;

    public Board(int width, int height) {
        this.width = width;
        this.height = height;
        this.board = new boolean[height][width];

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                this.board[i][j] = false;
            }
        }
    }

    public void printBoard() {
        System.out.print("     ");
        for (int i = 0; i < width; i++) {
            System.out.printf("%d  ", i);
        }
        System.out.println();
        for (int i = 0; i < height; i++) {
            System.out.printf("%d    ", i);
            for (int j = 0; j < width; j++) {
                if (this.board[i][j]) {
                    System.out.print("#  ");
                } else {
                    System.out.print(".  ");
                }
            }
            System.out.println();
        }
    }

    public boolean checkPossible(Tile tile) {
        int[] move = new int[3];

        for (int rot = 0; rot < 360; rot += 90) {
            for (int row = -2; row < height + 1; row++) {
                for (int col = -2; col < width + 1; col++) {
                    move[0] = row;
                    move[1] = col;
                    move[2] = rot;

                    if (checkMove(move, tile))
                        return true;
                }
            }
        }
        return false;
    }

    public int clearCompletes() {
        boolean complete;
        int completeCount = 0;
        for (int i = 0; i < height; i++) {
            // Check every column
            complete = true;
            for (int j = 0; j < width; j++) {
                if (!board[i][j]) {
                    complete = false;
                }
            }

            if (complete) {
                // Clear that row
                System.out.printf("Clearing row: %d%n", i);
                completeCount++;
                for (int j = 0; j < width; j++) {
                    board[i][j] = false;
                }
            }
        }

        for (int i = 0; i < width; i++) {
            complete = true;
            for (int j = 0; j < height; j++) {
                if (!board[i][j]) {
                    complete = false;
                }
            }

            if (complete) {
                System.out.printf("Clearing column: %d%n", i);
                // Clear that row
                completeCount++;
                for (int j = 0; j < height; j++) {
                    board[i][j] = false;
                }
            }
        }

        return completeCount;
    }

    public boolean checkMove(int[] move, Tile toPlace) {

        int x = move[0];
        int y = move[1];
        int rotation = move[2];
        boolean[][] tile = new boolean[TILESIZE][TILESIZE];

        try {
            tile = toPlace.getTile(rotation);
        } catch (Exception e) {

        }

        for (int row = 0; row < TILESIZE; row++) {
            for (int col = 0; col < TILESIZE; col++) {
                // Calculate the adjusted position
                int adX = row - 2 + x;
                int adY = col - 2 + y;

                if (tile[row][col]) {
                    if (adX < 0 || adY < 0 || adX > height - 1 || adY > width - 1) {
                        return false;
                    }
                    if (this.board[adX][adY]) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public void placeTile(int[] move, Tile toPlace) {
        // Tiles are 5x5, x and y Correspond to the middle (2, 2)
        // Rotation is in multiples of 90 degrees and clockwise
        // Assumes move has already been checked

        int x = move[0];
        int y = move[1];
        int rotation = move[2];
        boolean[][] tile = new boolean[TILESIZE][TILESIZE];

        try {
            tile = toPlace.getTile(rotation);
        } catch (Exception e) {

        }

        for (int row = 0; row < TILESIZE; row++) {
            for (int col = 0; col < TILESIZE; col++) {
                // Calculate the adjusted position
                int adX = row - 2 + x;
                int adY = col - 2 + y;

                if (tile[row][col]) {
                    this.board[adX][adY] = true;
                }
            }
        }
    }

    public boolean[][] getBoard() {
        return this.board;
    }
}
