'''
	Write a function fib() that takes an interger n and returns the nth fibonacci
	number
'''

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else :
		return fib(n - 1) + fib(n - 2)


for n in range(10):
	print(fib(n))
