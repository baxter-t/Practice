'''
	Your challenge is to create a function that takes any number and returns
	the number that it is a factorial of. So, if your function receives 120, 
	it should return "5!" (as a string).
'''

def reverse_factorial(num):
	total = 1
	count = 1
	while total <= num :
		if total == num:
			return "" + str(count) + "!"
		count += 1
		total *= count
		

	return "None" 

print(reverse_factorial(120))
print(reverse_factorial(3628800))
print(reverse_factorial(150))