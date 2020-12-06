# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One file
# has a list of all prime numbers under 1000, and the other file has a list of happy numbers up to 1000.
#

commonlist = []
primlist = []
happylist = []
with open('prime-numbers.txt') as f:
    line = f.readline()
    for i in f:
        primlist.append(int(i))
with open('happy-numbers.txt') as file:
    line = file.readline()
    for i in file:
        happylist.append(int(i))
commonlist = [i for i in primlist if i in happylist]
print(commonlist)

def file_to_convert_into_list(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        for line in f:
            list_to_return.append(int(line))
    return list_to_return
primeslist = file_to_convert_into_list('prime-numbers.txt')
happyestlist = file_to_convert_into_list('happy-numbers.txt')
commonlist = [i for i in primlist if i in happylist]
print(commonlist)
