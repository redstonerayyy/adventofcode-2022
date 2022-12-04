# read pairs as list to list

pairs = []

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if line != "":
            parts = line.split(",")
            p1 = [int(parts[0].split("-")[0]), int(parts[0].split("-")[1])]
            p2 = [int(parts[1].split("-")[0]), int(parts[1].split("-")[1])]
            pairs.append([p1, p2])

sum = 0
# check if starting number is bigger or euqal and ending number smaller or equal
for pair in pairs:
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        sum += 1
    elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
        sum += 1

print(sum)