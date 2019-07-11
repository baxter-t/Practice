'''
    Remake of CSSE2310 Assignment 1 in python
'''


TILESIZE = 5
tiles = [
    [
        ['!', '!', '!', ',', ','],
        ['!', '!', '!', ',', ','],
        [',', ',', ',', ',', ','],
        [',', ',', ',', ',', ','],
        [',', ',', ',', ',', ','],
    ]
]

class Game(object):
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [["."] * cols] * rows
        self.currentTile = 0

    def outputBoard(self):
        for r in range(self.rows):
            print("  ".join(self.board[r]))

    def getNextTile(self):
        if self.currentTile == len(tiles):
            self.currentTile = 0

        current = tiles[self.currentTile]

        self.currentTile += 1

        return current

    def rotateTile(self, tile):
        rotated = []
        
        for x in range(TILESIZE):
            rotated.append([row[4 - x] for row in tile])

        return rotated



    def outputTileOptions(self, tile):
        output = [""] * TILESIZE

        for x in range(4):
            tile = self.rotateTile(tile)
            for y in range(TILESIZE):
                output[y] += "  ".join(tile[y])

            if x < 3:
                for y in range(TILESIZE):
                    output[y] += "  |  "

        for x in range(TILESIZE):
            print(output[x])


    def takeInput


def main():
    game = Game(10, 10)
    game.outputBoard()

    game.outputTileOptions(game.getNextTile())

main()

