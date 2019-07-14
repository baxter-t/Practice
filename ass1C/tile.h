#ifndef __TILE_H
#define __TILE_H

#include "tile.h"

typedef struct Tiles {
	int tileCount;
	int currentTileNo;

	char ***tiles;
};

// Output the tile options
void outputTileOptions(char **tile);

#endif
