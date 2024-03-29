'''
	Given an array of integers, find the first missing positive integer in 
	linear time and constant space. In other words, find the lowest positive 
	integer that does not exist in the array. The array can contain duplicates 
	and negative numbers as well.
'''

def missingInt(arr):

	for i in range(len(arr) - 1):
		if arr[i] + 1 != arr[i + 1] and arr[i] + 1 != 0:
			return arr[i] + 1

	return arr[-1] + 1

print(missingInt([1, 2, 0]))