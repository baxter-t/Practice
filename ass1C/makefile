CFLAGS = -Wall -g -pedantic -std=c99 -Wall

game: game.o tile.o
	gcc $(CFLAGS) -o game game.c tile.c

tile: tile.o
	gcc $(CFLAGS) -o tile tile.c
