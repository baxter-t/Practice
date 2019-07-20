CFLAGS = -Wall -g -pedantic -std=c99 -Wall 

game: game.o tile.o util.o
	gcc $(CFLAGS) -o game game.c tile.c util.c

tile: tile.o
	gcc $(CFLAGS) -o tile tile.c

util: util.o
	gcc $(CFLAGS) -o util util.c
