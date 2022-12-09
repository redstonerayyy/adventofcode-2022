# read file
with open("input.txt") as file:
	lines = [line.replace("\n", "").split(" ") for line in file.readlines() if line.replace("\n", "") != ""]

def updatetail(head, tail):
	if not isheadneartail(head, tail):
		if head[0] == tail[0]: # x is same
			if head[1] > tail[1]:
				tail[1] += 1
			else:
				tail[1] -= 1
		elif head[1] == tail[1]: # y is same
			if head[0] > tail[0]:
				tail[0] += 1
			else:
				tail[0] -= 1
			
		else: # move both directions
			if head[1] > tail[1]:
				tail[1] += 1
			else:
				tail[1] -= 1
			if head[0] > tail[0]:
				tail[0] += 1
			else:
				tail[0] -= 1
	
	return tail[:]
			

def isheadneartail(head, tail):
	near = False
	for x in range(tail[0] - 1, tail[0] + 2):
		for y in range(tail[1] - 1, tail[1] + 2):
			if head == [x, y]:
				near = True

	return near

knots = [[0, 0] for _ in range(10)]
visited = [[0, 0]]

for move in lines:
	for i in range(int(move[1])):
		if move[0] == "U": # up
			knots[0][1] += 1
			for i in range(8):
				updatetail(knots[i], knots[i + 1])
			tail = updatetail(knots[8], knots[9])
			if tail not in visited:
				visited.append(tail)
		elif move[0] == "D": # down
			knots[0][1] -= 1
			for i in range(8):
				updatetail(knots[i], knots[i + 1])
			tail = updatetail(knots[8], knots[9])
			if tail not in visited:
				visited.append(tail)
		elif move[0] == "L": # left
			knots[0][0] -= 1
			for i in range(8):
				updatetail(knots[i], knots[i + 1])
			tail = updatetail(knots[8], knots[9])
			if tail not in visited:
				visited.append(tail)
		elif move[0] == "R": # right
			knots[0][0] += 1
			for i in range(8):
				updatetail(knots[i], knots[i + 1])
			tail = updatetail(knots[8], knots[9])
			if tail not in visited:
				visited.append(tail)
	

print(len(visited))
print(knots)
