'''
	Write a function that will find all the anagrams of a word from a 
	list. You will be given two inputs a word and an array with words. 
	You should return an array of all the anagrams or an empty array if 
	there are none. For example:
'''
def anagrams(word, words) :
	return list(filter(lambda x: sorted(word) == sorted(x), words))

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))