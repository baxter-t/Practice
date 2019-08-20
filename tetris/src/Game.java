public class Game {

    private int width;
    private int height;
    private Board board;
    private static final int TILESIZE = 5;

    public Game(int width, int height, String tileFile) {
        this.width = width;
        this.height = height;
        this.board = new Board(width, height);
    }

    public static boolean[][] generateTile(String tile) {
        // Tile should be in the format of a 25 char long string
        // of 1s and 0s that represent where the tile is
        int place = 0;
        boolean[][] newTile = new boolean[5][5];

        for (int i = 0; i < TILESIZE; i++) {
            for (int j = 0; j < TILESIZE; j++) {
                if (tile.charAt(place++) == '1') {
                    newTile[i][j] = true;
                } else {
                    newTile[i][j] = false;
                }
            }
        }

        return newTile;
    }

    public static void main(String args[]) {
        boolean[][] tile = Game.generateTile("1000010000100001000010000");

        for (int i = 0; i < TILESIZE; i++) {
            for (int j = 0; j < TILESIZE; j++) {
                if (tile[i][j]) {
                    System.out.print("* ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }
}
