import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
	lines = [line.replace("\n", "").split(" -> ") for line in file.readlines() if line.replace("\n", "") != ""]
	stone = []
	ymin = 1000 # definitely higher than some value
	ymax = 0
	xmin = 1000 # definitely higher than some value
	xmax = 0
	for line in lines:
		for point in range(len(line) - 1):
			p1 = [int(i) for i in line[point].split(",")]
			p2 = [int(i) for i in line[point + 1].split(",")]
			# find min/max
			for p in [p1, p2]:
				if p[0] > xmax:
					xmax = p[0]
				if p[0] < xmin:
					xmin = p[0]
				if p[1] > ymax:
					ymax = p[1]
				if p[1] < ymin:
					ymin = p[1]
			# add both points and between to stone cordinate list
			if p1[0] == p2[0]: # same x cords
				if p1[1] > p2[1]: # check from where to start the loop
					for y in range(p2[1], p1[1] + 1):
						stone.append([p1[0], y])
				else:
					for y in range(p1[1], p2[1] + 1):
						stone.append([p1[0], y])

			else: # same y cords
				if p1[0] > p2[0]: # check from where to start the loop
					for x in range(p2[0], p1[0] + 1):
						stone.append([x, p1[1]])
				else:
					for x in range(p1[0], p2[0] + 1):
						stone.append([x, p1[1]])

# print(stone)
print(xmin, xmax)
print(ymin, ymax)

# create cave list full of air
# x cord needs to be scaled
# y should start from 0
cave = []
for y in range(0, ymax + 1):
	cave.append([])
	for x in range(0, xmax - xmin + 1):
		cave[y].append(".")

# add stones into cave
for s in stone:
	# print(s[1] - ymin, s[0] - xmin)
	cave[s[1]][s[0] - xmin] = "#"

# add pouring point
cave[0][500 - xmin] = "+"

# start pouring
cametorest = 0
sand = [500, 0]
while True:
	print(cametorest)
	# down 
	if sand[1] < len(cave):
		print([sand[1] + 1, sand[0] - xmin]) 
		if cave[sand[1] + 1][sand[0] - xmin] == ".":
			sand = [sand[1] + 1, sand[0]]
			continue
		elif cave[sand[1] + 1][sand[0] - xmin] == "o" or cave[sand[1] + 1][sand[0] - xmin] == "#":
			continue

	# down left
	if sand[1] < len(cave) and (sand[0] - xmin - 1) >= 0: 
		if cave[sand[1] + 1][sand[0] - xmin - 1] == ".":
			sand = [sand[1] + 1, sand[0] - 1]
			continue
		elif cave[sand[1] + 1][sand[0] - xmin - 1] == "o" or cave[sand[1] + 1][sand[0] - xmin - 1] == "#":
			continue

	# down right
	if sand[1] < len(cave) and sand[0] - xmin + 1 < len(cave[0]): 
		if cave[sand[1] + 1][sand[0] - xmin + 1] == ".": # down right
			sand = [sand[1] + 1, sand[0] + 1]
			continue
		elif cave[sand[1] + 1][sand[0] - xmin + 1] == "o" or cave[sand[1] + 1][sand[0] - xmin + 1] == "#":
			cave[sand[1]][sand[0]] == "o"
			cametorest += 1
			sand = [500, 0]
			continue
	
	break # reached out of bounds

# print cave
for row in cave:
	for part in row:
		print(part, end="")
	print("")