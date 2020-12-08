import random
from random import randrange


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

# "Able was i, ere i saw elba" removing all the special caracters and lowercasing all the words
# the result is a palindrome


s = "Able was i, ere i saw elba".lower()
s = ''.join([string for string in s if string in 'abcdefghijklmnopqrstuwvxyz'])
print(s)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome(s))


# Print the palindromic triangle of size
for i in range(1,int(input())+1):
    print((111111111//(10**(9-i)))**2)

# Read in two integers, a and b. that prints a//b, a%b as tuple

def divmood(a,b):
    return (a//b, a%b)

a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmood(a,b))




def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#  NE NJE TREKENDESH KENDEREJTE NDERTOHET MESORJA BM MBU HIPOTENUZEN CA, GJENI KENDIN MBC

import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')

# jepet nje string nga useri, printo cifte te renditura qe permbajne karakterin
# dhe sa here ndodhet karkateri ne string

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])