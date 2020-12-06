#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user.
#Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

odd_or_even = int(input("Enter the number: "))

if odd_or_even % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
if odd_or_even % 4 == 0:
    print("The number is a multiple of 4.")
else:
    print("The number is not a multiple of 4.")

num = int(input("The divisor: "))
check = int(input("The number to check: "))

if check % num == 0:
    print(f"{check} is a multiple of {num}.")
else:
    print("The number don't divide evenly.")