#include "tile.h"
#include <stdio.h>
#include <stdlib.h>

char TILE[TSIZE][TSIZE] = {
    {'!', '!', ',', ',', ','},
    {'!', '!', ',', ',', ','},
    {'!', ',', ',', ',', ','},
    {',', ',', ',', ',', ','},
    {',', ',', ',', ',', ','},
};

void outputTile(char **tile) {
    for (int x = 0; x < TSIZE; x++) {
        for (int y = 0; y < TSIZE; y++) {
            printf("%c  ", tile[x][y]);
        }
        printf("\n");
    }
    return;
}

char **rotateTile(char **tile) {
    char **rotated = malloc(TSIZE * sizeof(char *));
    for (int i = 0; i < TSIZE; i++) {
        rotated[i] = malloc(TSIZE * sizeof(char *));
    }

    for (int y = 0; y < TSIZE; y++) {
        for (int x = 0; x < TSIZE; x++) {
            rotated[x][y] = tile[TSIZE - y - 1][x];
        }
    }

    return rotated;
}

void outputTileOptions(char **tile) {
    // Tile size for each row
    char **tileOptions = malloc(TSIZE * sizeof(char *));

    for (int i = 0; i < TSIZE; i++) {
        // 5 char, two spaces between, 15 per tile times four
        // 2 extra between tiles
        tileOptions[i] = malloc(sizeof(char *) * 20);
    }

    int counter = 0;
    while (counter < 4) {
        // Output then rotate
        for (int y = 0; y < TSIZE; y++) {
            for (int x = 0; x < TSIZE; x++) {
                tileOptions[y][5 * counter + x] = tile[y][x];
            }
        }

        tile = rotateTile(tile);
        counter++;
    }

    // Output the options
    for (int y = 0; y < TSIZE; y++) {
        int tCount = 0;

        while (tCount < 4) {
            for (int x = 0; x < TSIZE; x++) {
                printf("%c  ", tileOptions[y][x + tCount * 5]);
            }
            printf("   ");
            tCount++;
        }
        printf("\n");
    }

    return;
}

char ***getTiles(void) {
    // At the moment just get the one tile
    int noOfTiles = 1;

    char ***tiles = malloc(sizeof(char *) * noOfTiles);
    for (int i = 0; i < noOfTiles; i++) {
        tiles[i] = malloc(sizeof(char *) * TSIZE);
        for (int j = 0; j < TSIZE; j++) {
            tiles[i][j] = malloc(sizeof(char *) * TSIZE);
        }
    }
    for (int i = 0; i < TSIZE; i++) {
        for (int j = 0; j < TSIZE; j++) {
            tiles[0][i][j] = TILE[i][j];
        }
    }
    return tiles;
}

Tiles initialiseTiles(void) {
    Tiles tiles;
    tiles.tileCount = 1;
    tiles.currentTileNo = 0;

    tiles.tileDeck = getTiles();

    return tiles;
}
