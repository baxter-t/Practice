from collections import Counter

inp = [1, 2, 3, 2, 3]

def find_it(arr):

    occurences = {}
    for a in arr:
        occurences[a] = occurences.get(a, 0) + 1

    for key in occurences:
        if occurences[key] % 2 != 0:
            return key
    

print(find_it(inp))
