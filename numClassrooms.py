'''
	Given an array of time intervals for class room lectures, find the minimum
	number of rooms required
'''

def numRooms(arr):
	print(arr)
	classes = [[arr[0]]]

	for x in range(1, len(arr)):
		# Check the end is before the current start
		found = False
		for i, room in enumerate(classes):
			if room[0][0] > arr[x][1]:
				classes[i] = [arr[x]] + room
				found = True
			elif room[-1][1] < arr[x][0]:
				classes[i].append(arr[x])
				found = True
		
		if not found:
			classes.append([arr[x]])

	print(classes)
	return len(classes)

print(numRooms([(30,75), (0, 50), (60,150)]))