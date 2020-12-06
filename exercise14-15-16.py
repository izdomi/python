#Write a program (function!) that takes a list and returns a new list that contains all the elements of
# the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_duplicates1(lists):
    for i in lists:
        if lists.count(i) > 1:
            for i in lists:
                while lists.count(i) != 1:
                    lists.remove(i)
            return lists

a = [1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 6, 6, 7, 7, 7, 7]
print(remove_duplicates1(a))

def remove_duplicates2(lists):
    return set(lists)

a = [1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 6, 6, 7, 7, 7, 7]
print(remove_duplicates2(a))

#EXERCISE 15

#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#   My name is Michele
# Then I would see the string:
#   Michele is name My

def reverese_word_order(sentence):
    revers = sentence.split(' ')
    return ' '.join(revers[::-1])

sent = input('The sentence: ')
print(reverese_word_order(sent))

#EXERCISE 16

#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import string
import random

def password(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

