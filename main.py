import random
from random import randrange
import math

def find_squeare(x):
    g = random.choice(range(1 ,x))
    while g *g != x:
        g = (g + x / g) / 2
        if x == g * g:
            return g

print(find_squeare(16))

def findSqrt(nr):
    g = round(nr/ randrange(1,nr))
    while nr!= g*g:
        print(g*g, (g+nr/g)/2)
        if (nr==math.ceil(g*g)):
            return g
        else:
            g = (g+nr/g)/2

print(findSqrt(8))

# "Able was i, ere i saw elba" removing all the special caracters and lowercasing all the words the result is a palindrome


s = "Able was i, ere i saw elba".lower()
s = ''.join([string for string in s if string in 'abcdefghijklmnopqrstuwvxyz'])
print(s)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome(s))