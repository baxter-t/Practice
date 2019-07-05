'''
	Given a dictionary of words and a string of those words with no spaces
	return a list that is the original sentence
'''

def toStng(dictionary, strng):
	index = 0
	result = []
	while len(strng) > 0:
		if strng[:index] in dictionary:
			result.append(strng[:index])
			strng = strng[index:]
			index = 0
		index += 1
	return result

strngTest = "thequickbrownfox"
dicTest = ['quick', 'brown', 'the', 'fox']

# this is a comment


print(toStng(dicTest, strngTest))
