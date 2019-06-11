'''
	Given an array of strings, reverse them and their order in such a way that 
	their length stays the same as the length of the original inputs
'''

def reverse(a):
	all = "".join(a)[::-1]
	print(all)

	result = []
	for x in a :
		result.append(all[:len(x)])
		all = all[len(x):]

	return result

print(reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]))
