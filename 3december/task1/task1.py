import string

# determine priority as index + 1 of this string of letters
letters = string.ascii_lowercase + string.ascii_uppercase

# read matches as arrays of the two compartments
rucksacks = []

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if line != "":
            rucksacks.append([ line[:len(line)//2] , line[len(line)//2:] ] )

# calculate sum of priorities
sum = 0
for rucksack in rucksacks:
    # convert compartments to sets, make intersect of sets and convert to list to access
    sum += letters.index(list( set(rucksack[0]) & set(rucksack[1]) )[0]) + 1

print(sum)