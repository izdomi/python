# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that
# many copies of the previous message.
# Print out that many copies of the previous message on separate lines.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num = int(input("How many times do you want the message to repeat? "))
year = 2020 + (100 - age)
for i in range(num):
    print(f"Your name is {name} \n"
          f"You are {age} years old \n"
          f"You will be 100 year old at {year}")