'''
    Find the product of nth fibonacci numbers
'''

def nthFib(n):
    if n == 0 or n == 1:
        return n

    return nthFib(n-1) + nthFib(n-2)

def prodFib(prod):
    n = 2
    product = nthFib(n) * nthFib(n - 1)
    while product <= prod:
        if product == prod:
            return True
        n += 1

        product = nthFib(n) * nthFib(n - 1)

    return False

print(prodFib(5895))
