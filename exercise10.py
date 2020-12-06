# Take two lists
# and write a program that returns a list that contains only the elements that are common between the lists
# Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.
# Extra:
# Randomly generate two lists to test this

import random
list1 = random.sample(range(1,15), 10)
list2 = random.sample(range(1,30), 8)
common = [i for i in list1 if i in list2]
print(f'list1 = {list1} \nlist2 = {list2}')
print(common)