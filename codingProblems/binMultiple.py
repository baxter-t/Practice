inp = '110'

def binToInt(inp):
    reversd = inp[::-1]

    total = 0

    for i, k in enumerate(reversd):
        total += (2 ** i) * int(k)

    return total

def binMultiple(b, m):
    return binToInt(b) % m == 0

print(binToInt(inp))

print(binMultiple(inp, 3))
print(binMultiple(inp, 4))
