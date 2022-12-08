# read file
with open("input.txt") as file:
	lines = [line.replace("\n", "") for line in file.readlines() if line.replace("\n", "") != ""]
	grid = []
	for line in lines:
		grid.append([int(num) for num in line])

# get scenic score
def getscenicscore(y, x):
	tree = grid[y][x]
	# left
	s1 = 0
	left = []
	for i in range(0, x)[::-1]: # reverse
		s1 += 1
		left.append(grid[y][i])
		if grid[y][i] >= tree:
			break

	# right
	s2 = 0
	right = []
	for i in range(x + 1, len(grid[y])): # reverse
		s2 += 1
		right.append(grid[y][i])
		if grid[y][i] >= tree:
			break

	# top
	s3 = 0
	top = []
	for i in range(0, y)[::-1]: # reverse
		s3 += 1
		top.append(grid[i][x])
		if grid[i][x] >= tree:
			break

	# bottom
	s4 = 0
	bottom = []
	for i in range(y + 1, len(grid)):
		s4 += 1
		bottom.append(grid[i][x])
		if grid[i][x] >= tree:
			break
	
	return s1 * s2 * s3 * s4, tree, [s1, s2, s3, s4], [left, right, top, bottom]

maxscenic = 0
# check for all trees
for y in range(0, len(grid)):
	for x in range(0, len(grid[y])):
		scenic, num, nums, ways = getscenicscore(y, x)
		if scenic > maxscenic:
			maxscenic = scenic

print(maxscenic)