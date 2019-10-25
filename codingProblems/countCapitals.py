'''
	Write a one liner that will count the nymber of capital letters ina file
	Your code should work even if the file is too big to fit in memory
'''

def count_capitals(fname) :
	with open(fname, 'r') as f:
                return len[x if x.isupper() else "" for line in f for x in line]

        

print(count_capitals("testFile"))
