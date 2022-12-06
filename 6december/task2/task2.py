# read file as string

with open("input.txt") as file:
    data = file.read()

leng = 14
for i in range(len(data) - leng):
    part = data[i: i + leng]
    if not any(part.count(l) > 1 for l in part):
        print(i + leng)
        print(part)
        break