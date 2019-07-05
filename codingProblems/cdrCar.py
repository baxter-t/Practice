'''
	cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns 
	the first and last element of that pair. For example, car(cons(3, 4)) 
	returns 3, and cdr(cons(3, 4)) returns 4.
'''

def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

def car(c):
	return c(lambda x, y: x)

def cdr(c):
	return c(lambda x, y: y)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
