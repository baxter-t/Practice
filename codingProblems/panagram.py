'''
	A pangram is a sentence that contains every single letter of the alphabet 
	at least once. For example, the sentence "The quick brown fox jumps over 
	the lazy dog" is a pangram, because it uses the letters A-Z at least once 
	(case is irrelevant).

	Given a string, detect whether or not it is a pangram. Return True if it 
	is, False if not. Ignore numbers and punctuation.
'''

def isPangram(s):
    s = s.lower()

    s = "".join([x for x in s if x.isalpha()])
    print(s)

    return len(set(s)) == 26

pangram = "The quick, brown fox jumps over the lazy dog!"
print(isPangram(pangram))
