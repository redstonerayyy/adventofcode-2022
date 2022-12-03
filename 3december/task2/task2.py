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
            # no splitting of parts needed anymore
            rucksacks.append(line)

# make elve groups
elvegroups = []

for i in range(0, len(rucksacks), 3):
    group = []
    for j in range(3):
        group.append(rucksacks[i + j])
    elvegroups.append(group)
    group = []

print(elvegroups)

# calculate sum of priorities
sum = 0
for elvegroup in elvegroups:
    # convert compartments to sets, make intersect of sets and convert to list to access
    sum += letters.index(list( set(elvegroup[0]) & set(elvegroup[1]) & set(elvegroup[2]) )[0]) + 1

print(sum)