'''
	Given a list of numbers and a number k, return whether any two numbers 
	from the list add up to k
'''

def listSum(k, arr):
	for x in arr:
		if k - x in arr:
			return True

	return False

print(listSum(40, [10, 15, 3, 7]))
