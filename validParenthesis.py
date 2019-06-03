'''
	Write a function called that takes a string of parentheses, and determines 
	if the order of the parentheses is valid. The function should return true 
	if the string is valid, and false if it's invalid
'''

def valid_parentheses(string) :
	count = 0
	for x in string :
		if x == "(" :
			count = count + 1 
		elif x == ")":
			count = count - 1 

		if count < 0 : return False

	return count == 0