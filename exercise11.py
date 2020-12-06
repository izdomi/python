# Ask the user for a number and determine whether the number is prime or not. You can (and should!)
# use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


def prime(num):
    divisor = [i for i in range(1,num + 1) if num % i == 0]
    if divisor == [1, num]:
        print("PRIME!")
    else:
        print("NOT PRIME!")
a = int(input())
print(prime(a))