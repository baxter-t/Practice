'''
	Given an array, return an array such that every element is product of all the
	numbers in the array asside from the one at position i
'''

def listTotal(arr):
	total = 1

	for x in arr:
		total *= x

	return total

def withDivisionArrayProduct(arr):
	total = listTotal(arr)
	
	return [int(total/x) for x in arr]

def arrayProduct(arr):
	results = []

	for x in range(len(arr)):
		element = arr.pop(x)
		results.append(listTotal(arr))
		arr.insert(x, element)

	return results


a = [1, 2, 3, 4, 5]
print(arrayProduct(a))
print(withDivisionArrayProduct(a))
