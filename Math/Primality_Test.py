#Using Miller-Rabin primality test

import random

def binpower(base, e, mod):
    result = 1
    base %= mod
    while e:
        if e & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        e >>= 1
    return result

def check_composite(n, a, d, s):
    x = binpower(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for r in range(1, s):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True

def MillerRabin(n, iter=5):
    if n < 4:
        return n == 2 or n == 3

    s = 0
    d = n - 1
    while d & 1 == 0:
        d >>= 1
        s += 1

    for i in range(iter):
        a = 2 + random.randint(0, n - 3)
        if check_composite(n, a, d, s):
            return False
    return True

num = int(input("Input a odd number: "))

if MillerRabin(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number')