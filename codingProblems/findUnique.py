def find_uniq(arr) :
	first = arr[0]
	matching = [x for x in arr if x != first]
	return matching[0] if len(matching) == 1 else first

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))

print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))
