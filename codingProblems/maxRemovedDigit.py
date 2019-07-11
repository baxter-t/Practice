'''
    Given an integer n, find the maximal number you can obtain by deleting 
    exactly one digit of the given number.
'''

def delete_digit(n):
    num = str(n)

    return max((int(num[:x] + num[x + 1:]) for x in range(len(num))))


print(delete_digit(152))
