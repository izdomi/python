# Ask the user for a string and print out whether this string is a palindrome or not.

string = input("the word: ")
i = 0
while i in range(len(string)-1):
    if string[i] != string[len(string)-1-i]:
        print("The word is not a palindrome!")
        break
    else:
        print("The word is a palindrome!")
        break