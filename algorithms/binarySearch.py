'''
	Binary Search

	Time Complexity: O(logN)
'''

arr = [1, 2, 3, 4, 5, 5, 5, 6, 12, 144, 555]

def binarySearch(arr, element):
	
	while len(arr) > 1:
		middle = int(len(arr) / 2)
		if arr[middle] == element:
			return True
		elif arr[middle] < element:
			arr = arr[middle:]
		else:
			arr = arr[:middle]

	return False

print(binarySearch(arr, 10))