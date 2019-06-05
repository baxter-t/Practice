'''
	Write a function dirReduc which will take an array of strings and returns 
	an array of strings with the needless directions removed (W<->E or S<->N 
	side by side).
'''

def mapDirections(strng):
	if strng == "NORTH":
		return (0, 1)
	if strng == "SOUTH":
		return (0, -1)
	if strng == "EAST":
		return (1, 0)
	if strng == "WEST":
		return (-1, 0)
	if strng == (0, 1):
		return "NORTH"
	if strng == (0, -1):
		return "SOUTH"
	if strng == (1, 0):
		return "EAST"
	if strng == (-1, 0):
		return "WEST"

def dirReduc(arr) :
	mapped = [mapDirections(x) for x in arr]

	for x in range(len(mapped) - 1):
		if mapped[x] != 0:
			if tuple(map(lambda x, y: x + y, mapped[x], mapped[x + 1])) == (0,0) :
				mapped[x] = mapped[x + 1] = 0

	mapped = list(filter(lambda x: x != 0, mapped))
	mapped = [mapDirections(x) for x in mapped]

	return mapped if len(mapped) == len(arr) else dirReduc(mapped)


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))