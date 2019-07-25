#include <stdio.h>
#include <stdlib.h>
#include "tile.h"
#include "util.h"

char tile[TSIZE][TSIZE] = {
    {'!', '!', '!', ',', ','},
    {'!', '!', ',', ',', ','},
    {',', ',', ',', ',', ','},
    {',', ',', ',', ',', ','},
    {',', ',', ',', ',', ','},
};

typedef struct GameState {
    int boardWidth;
    int boardHeight;

    // Players
    int currentPlayer;

    Tiles tileManager;

    char **board;
} GameState;

typedef struct PlayerMove {
    int row;
    int col;
    int rotation;
} PlayerMove;

void setBoard(GameState *game) {
    game->board = malloc(game->boardHeight * sizeof(char *));

    for (int x = 0; x < game->boardHeight; x++) {
        game->board[x] = malloc(game->boardWidth * sizeof(char *));
    }

    for (int x = 0; x < game->boardHeight; x++) {
        for (int y = 0; y < game->boardWidth; y++) {
            game->board[x][y] = '.';
        }
    }
}

void outputBoard(GameState *game) {
    for (int x = 0; x < game->boardHeight; x++) {
        for (int y = 0; y < game->boardWidth; y++) {
            printf("%c  ", game->board[x][y]);
        }

        printf("\n");
    }
}

PlayerMove promptUser(int playerNo) {
    PlayerMove move = {
        .row = 0,
        .col = 0,
        .rotation = 0,
    };

    if (playerNo) {
        printf("Player *] ");
    } else {
        printf("Player #] ");
    }

    char *playerIn;
    if (readLine(stdin, &playerIn, 0) <= 0) {
        printf("Error reading from stdin\n");
        exit(0);
    } else {
        printf("%s\n", playerIn);
    }

    // Parse inputted
    int row,
        col, rotation;
    if (sscanf(playerIn, "%d %d %d ", &row, &col, &rotation) != 3) {
        // Invalid
        printf("Invalid Input.\n");
        exit(0);
    } else {
        move.row = row;
        move.col = col;
        move.rotation = rotation;
    }

    // Verify valid rotation
    if (move.rotation % 90 != 0 || move.rotation > 261) {
        printf("Invalid rotation\n");
        exit(0);
    }

    return move;
}
// Return: 1 if valid, 0 otherwise
int checkMove(GameState *game, PlayerMove *move) {
    // The tile being checked is the currentTileNo tile
    char **tile = game->tileManager.tileDeck[game->tileManager.currentTileNo];

    // Should rotate tile according to move here
    int rotations = move->rotation;
    while (rotations != 0) {
        tile = rotateTile(tile);
        rotations -= 90;
    }

    // the row and column corresponds to the middle (2,2) in the tile 2d array
    for (int row = 0; row < TSIZE; row++) {
        for (int col = 0; col < TSIZE; col++) {
            printf("row: %d col:%d\n", row, col);
            // the board's row and column is the tile's - 2

            // Only check if its a part of the tile
            if (tile[row][col] == '!') {
                // Make sure its in the bounds of the game board
                int xPos = row - 2 + move->row;
                int yPos = col - 2 + move->col;

                if (xPos < 0 || yPos < 0 || xPos >= game->boardHeight || yPos >= game->boardWidth) {
                    return 0;
                } else {
                    if (game->board[xPos][yPos] != '.') {
                        return 0;
                    }
                }
            }
        }
    }

    // Gets to the end every was valid
    return 1;
}

// Assumes that the move is valid
void placeTile(GameState *game, PlayerMove *move) {
    // Get tile and rotate
    char **tile = game->tileManager.tileDeck[game->tileManager.currentTileNo];
    int rotations = move->rotation;
    while (rotations != 0) {
        tile = rotateTile(tile);
        rotations -= 90;
    }

    for (int row = 0; row < TSIZE; row++) {
        for (int col = 0; col < TSIZE; col++) {
            // Calculate position
            int xPos = row - 2 + move->row;
            int yPos = col - 2 + move->col;

            // Place
            if (tile[row][col] == '!') {
                // player one
                if (game->currentPlayer) {
                    game->board[xPos][yPos] = '*';
                } else {
                    game->board[xPos][yPos] = '#';
                }
            }
        }
    }
}

int playGame(GameState *game) {
    // Display board
    outputBoard(game);

    outputTileOptions(game->tileManager.tileDeck[game->tileManager.currentTileNo]);

    PlayerMove move = promptUser(0);

    printf("Result: %d\n", checkMove(game, &move));

    placeTile(game, &move);

    outputBoard(game);

    return 0;
}

int main(int argc, char **argv) {
    GameState game;
    game.boardWidth = 10;
    game.boardHeight = 10;
    game.tileManager = initialiseTiles();
    game.currentPlayer = 0;

    setBoard(&game);

    playGame(&game);
}
