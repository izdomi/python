# Write a function that takes an ordered list of numbers and another number.
# The function decides whether or not the given number is inside the list and returns an appropriate boolean.
# Extras:
# Use binary search.

def find_the_number(number,ord_list):
    while True:
        if len(ord_list)//2 < 1:
            return False
        if number == ord_list[len(ord_list)//2]:
            return True
        elif number < ord_list[len(ord_list)//2]:
            ord_list = ord_list[:len(ord_list)//2]
        else:
            ord_list = ord_list[len(ord_list)//2:]

if __name__=="__main__":
    lists = [1,2,3,4,5,6,7]
    print(find_the_number(1,lists))



