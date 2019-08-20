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
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (this.board[i][j]) {
                    System.out.print("# ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    public boolean checkMove(int x, int y, int rotation, boolean tile[][]) {

        if (rotation % 90 != 0) {
            // Bad rotation
            return false;
        }

        // Rotate the tile
        while (rotation != 0) {
            // Rotate the tile
            rotation -= 90;
        }


        for (int row = 0; row < TILESIZE; row++) {
            for (int col = 0; col < TILESIZE; col++) {
                // Calculate the adjusted position
                int adX = row - 2 + x;
                int adY = col - 2 + y;

                if (tile[row][col]) {
                    if (this.board[adX][adY]) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public void placeTile(int x, int y, int rotation, boolean tile[][]) {
        // Tiles are 5x5, x and y Correspond to the middle (2, 2)
        // Rotation is in multiples of 90 degrees and clockwise
        // Assumes move has already been checked

        // Rotate the tile
        while (rotation != 0) {
            rotation -= 90;
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
