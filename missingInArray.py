'''
	Find the missing number in a given integer array from 1 to 100
'''

def findMissing(arr):
	for x in range(1, 101):
		if x not in arr :
			return x