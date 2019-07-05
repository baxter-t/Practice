'''
	Implement a function that finds the difference between two lists
'''

def array_diff(a, b) :
	return [x for x in a if x not in b]