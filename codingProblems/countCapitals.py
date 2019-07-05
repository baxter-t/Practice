'''
	Write a one liner that will count the nymber of capital letters ina file
	Your code should work even if the file is too big to fit in memory
'''

def count_capitals(fname) :
	count = 0

	with open(fname, 'r') as f:
		return sum(1 if c.isupper() else 0 for line in f for c in line)

        

print(count_capitals("testFile"))
