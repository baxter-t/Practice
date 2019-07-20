#ifndef __TILE_H
#define __TILE_H

#include "tile.h"

#define TSIZE 5

typedef struct Tiles {
    int tileCount;
    int currentTileNo;

    char ***tileDeck;
} Tiles;

// Output the tile options
void outputTileOptions(char **tile);

// Initialise the tile manager
Tiles initialiseTiles(void);

// output the tile options
void outputTileOptions(char **tile);

#endif
