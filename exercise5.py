# Take two lists,
# and write a program that returns a list that contains only the elements that are common between the lists.
# Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python

lst1 = []
lst2 = []

num1 = int(input("length of list 1: "))
for i in range(num1):
    element1 = int(input("Element for list 1: "))
    lst1.append(element1)

num2 = int(input("length of list 2: "))
for j in range(num2):
    element2 = int(input("Element for list 2: "))
    lst2.append(element2)

if num1 < num2:
    common = [i for i in lst1 if i in lst2]
else:
    common = [j for j in lst2 if j in lst1]
print(common)
