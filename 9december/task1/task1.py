# read file
with open("input.txt") as file:
	lines = [line.replace("\n", "").split(" ") for line in file.readlines() if line.replace("\n", "") != ""]

def updatetail():
	if not isheadneartail():
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
		
		if tail[:] not in tailvisited:
			tailvisited.append(tail[:])
			

def isheadneartail():
	near = False
	for x in range(tail[0] - 1, tail[0] + 2):
		for y in range(tail[1] - 1, tail[1] + 2):
			if head == [x, y]:
				near = True

	return near

head = [0, 0]
tail = [0, 0]
tailvisited = [[0, 0]]

for move in lines:
	for i in range(int(move[1])):
		if move[0] == "U": # up
			head[1] += 1
			updatetail()
		elif move[0] == "D": # down
			head[1] -= 1
			updatetail()
		elif move[0] == "L": # left
			head[0] -= 1
			updatetail()
		elif move[0] == "R": # right
			head[0] += 1
			updatetail()
	

print(len(tailvisited))