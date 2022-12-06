# read file as string

with open("input.txt") as file:
    data = file.read()

for i in range(len(data) - 4):
    part = data[i: i + 4]
    if not any(part.count(l) > 1 for l in part):
        print(i + 4)
        break