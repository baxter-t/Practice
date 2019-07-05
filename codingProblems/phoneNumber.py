'''
	Write a function that accepts an array of 10 integers (between 0 and 9), 
	that returns a string of those numbers in the form of a phone number.
'''

def create_phone_number(n) :
	n = [str(x) for x in n]
	return "({}) {}-{}".format("".join(n[:3]), "".join(n[3:6]), "".join(n[6:]))


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))