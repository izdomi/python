# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
random_num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
guess = 0
count = 0
while guess != random_num and guess != 'exit':
    guess = input("Guess a number from 1 to 9: ")
    if guess == 'exit':
        print(f"The number is {random_num} ")
        break
    guess = int(guess)
    count += 1
    if guess < random_num:
        print("Too low!")
    elif guess > random_num:
        print("Too high!")
    else:
        print("Correct!")
        print(f"You tried {count} times!")
