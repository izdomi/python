#Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it
# and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller
# than that number given by the user.

num_of_ele = int(input("Enter the number of elements: "))
lst = []
for element in range(num_of_ele):
    element = int(input("Elements of the list: "))
    lst.append(element)
less_that_5 = [element for element in lst if element < 5]
print(less_that_5)
num = int(input("Create a list with elements less that: "))
less_that_num = [element for element in lst if element < num]
print(less_that_num)
