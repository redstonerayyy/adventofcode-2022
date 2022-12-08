# read file
with open("input.txt") as file:
	lines = [line.replace("\n", "") for line in file.readlines() if line.replace("\n", "") != ""]
	grid = []
	for line in lines:
		grid.append([int(num) for num in line])

# check if tree is visible
def checktree(y, x):
	tree = grid[y][x]
	visible = False
	# left
	if all([grid[y][i] < tree for i in range(0, x)]):
		visible = True

	# right
	if all([grid[y][i] < tree for i in range(x + 1, len(grid[y]))]):
		visible = True

	# top
	if all([grid[i][x] < tree for i in range(0, y)]):
		visible = True
	
	# bottom
	if all([grid[i][x] < tree for i in range(y + 1, len(grid))]):
		visible = True

	return visible

# get visible trees
visible = len(grid) * 2 + len(grid[0]) * 2 - 4

for y in range(1, len(grid) - 1): # exclude outer trees
	for x in range(1, len(grid[y]) - 1): # exclude outer trees
		if checktree(y, x):
			visible += 1

print(visible)