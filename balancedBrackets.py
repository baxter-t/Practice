'''
    Given a string of round, curly and square open brackets, return
    whether the brackets are balanced
'''

def balanced(strng):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']

    for x in strng:
        if x in opening:
            stack.append(x)
        else :
            if closing.index(x) != opening.index(stack.pop()):
                return False

    return True

print(balanced("()")


