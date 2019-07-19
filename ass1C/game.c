#include <stdio.h>
#include <stdlib.h>

#define TSIZE 5

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

    char **board;
} GameState;

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

    return;
}

void outputBoard(GameState *game) {
    for (int x = 0; x < game->boardHeight; x++) {
        for (int y = 0; y < game->boardWidth; y++) {
            printf("%c  ", game->board[x][y]);
        }

        printf("\n");
    }
}

int main(int argc, char **argv) {
    GameState game;
    game.boardWidth = 10;
    game.boardHeight = 10;

    setBoard(&game);

    outputBoard(&game);
}
