# read from file
with open("input.txt") as file:
	lines = file.readlines()
	ln = 0
	position = []
	movesstrings = []
	while ln < len(lines):
		strip = lines[ln].replace("\n", "")
		if strip != "":
			if strip[0:4] == "move":
				movesstrings.append(strip)
			else:
				position.append(strip)
		ln += 1

# get stacks
stacks = []
for i in range(1, len(position[0]), 4):
	stack = []
	for pos in position:
		if pos[i] != " ":
			stack.append(pos[i])
	stacks.append(stack[:-1])

# get moves
moves = []
for move in movesstrings:
	moves.append([ int(move.split(" ")[1]), int(move.split(" ")[3]), int(move.split(" ")[5])])

# print(stacks)
# print(moves)

# apply moves
for move in moves:
	for i in range(move[0]):
		print(move[2], move[1])
		stacks[move[2] - 1].insert(0, stacks[move[1] - 1].pop(0))

# print stack tops
for stack in stacks:
	print(stack[0], end="")

print("")