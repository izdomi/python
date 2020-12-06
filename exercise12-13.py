#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.

def new_list(lst):
    a = [lst[0],lst[-1]]
    print(a)
b = [1,2,3,4,5]
print(new_list(b))

# EXERCISE 13
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
# numbers in the sequence to generate.

def fibonnaci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
sequence = int(input("number of sequences:"))
print(fibonnaci(sequence))