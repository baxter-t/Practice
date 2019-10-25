'''
	Write a function dirReduc which will take an array of strings and returns 
	an array of strings with the needless directions removed (W<->E or S<->N 
	side by side).
'''

DIRECTIONS = {
    "NORTH": (0, 1),
    (0, 1): "NORTH",
    "SOUTH": (0, -1),
    (0, -1): "SOUTH",
    "EAST": (1, 0),
    (1, 0): "EAST",
    "WEST": (-1, 0),
    (-1, 0): "WEST"
}


def dirReduc(arr):
    mapped = [DIRECTIONS[x] for x in arr]
    resultant = []

    for i, x in enumerate(mapped):
        if i == len(mapped) - 1:
            break

        if x[0] + mapped[i + 1][0] != 0 or x[1] + mapped[i + 1][1] != 0:
            resultant.append(x)

    mapped = [DIRECTIONS[x] for x in resultant]

    return mapped if len(mapped) == len(arr) else dirReduc(mapped)


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))
