# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("The number: "))
print([i for i in range(1,num) if num % i == 0])
# print(lst)