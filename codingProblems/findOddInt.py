from collections import Counter

inp = [1, 2, 3, 2, 3]

def find_it(arr):

    occurences = {}
    for a in arr:
        occurences[a] = occurences.get(a, 0) + 1

    for key in occurences:
        if occurences[key] % 2 != 0:
            return key
    
def find_linear(arr):

    return [x for x in arr if arr.count(x) % 2 != 0][0]

print(find_it(inp))
print(find_linear(inp))
