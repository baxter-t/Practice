'''
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

e.g.
[
  '  *  ', 
  ' *** ', 
  '*****'
]
'''

def padding(width, n) :

	return int((width - n) / 2)

def tower_builder(n) :
	width = 2 * (n - 1) + 1
	floors = [" " * padding(width, x) + "*" * x + " " * padding(width, x) for x in range(1, n * 2) if x%2 == 1]

	return floors


print(tower_builder(5))