# read pairs as list to list

pairs = []

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if line != "":
            parts = line.split(",")
            p1 = [i for i in range(int(parts[0].split("-")[0]), int(parts[0].split("-")[1]) + 1)]
            p2 = [i for i in range(int(parts[1].split("-")[0]), int(parts[1].split("-")[1]) + 1)]
            pairs.append([p1, p2])

# convert to sets and check if intersect is empty
sum = 0

for p in pairs:
    if set(p[0]) & set(p[1]):
        sum += 1
print(sum)