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

// Ensure the given move is valid
// Return: 1 if valid, 0 otherwise
int checkMove(GameState *game, PlayerMove *move) {
 	


}

int playGame(GameState *game) {
    // Display board
    outputBoard(game);

    outputTileOptions(game->tileManager.tileDeck[game->tileManager.currentTileNo]);

    PlayerMove move = promptUser(0);

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
