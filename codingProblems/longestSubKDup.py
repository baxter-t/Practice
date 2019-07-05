'''
	Given an integer k and string s, find the length of the longest substring 
	that contains at most k distinct characters
'''
def noDuplicates(strng):
	result = ""
	for x in strng:
		if x not in result :
			result += x
	return result

def longest(k, strng):
	start = 0
	longest = ""
	for x in range(0, len(strng)):
		i = len(longest)
		while i < len(strng) - x + 1:
			print(noDuplicates(strng[x:x + i]))
			if len(noDuplicates(strng[x:x + i])) <= k:
				if len(strng[x:x + i]) > len(longest):
					longest = strng[x:x+i]
			i += 1

	return longest



print(longest(2, "abcba"))