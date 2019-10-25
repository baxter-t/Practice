'''
	Given an array of integers and a number k, compute the maximum values of each
	subarray of length k
'''

def maxSub(arr, k):
	sub = []
	for i in range(len(arr) - k + 1):
		sub = arr[i : i  + k]
		if len(sub) == k:
			print(max(sub))


maxSub([10, 5, 2, 7, 8, 7], 3)
