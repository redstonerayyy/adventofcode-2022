# read matches from file as arrays of the to letters
matches = []

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		line = line.replace("\n", "")
		if line != "":
			matches.append(line.split(" "))


# conversion
conv = {"Y": [2, "B"], "X": [1, "A"], "Z": [3, "C"]}
score = 0

for match in matches:
	score += conv[match[1]][0] # 1 rock, 2 paper, 3 scissors
	# match outcome
	inp = conv[match[1]][1]
	if inp == match[0]: # draw
		score += 3

	elif match[0] == "A":
		if inp == "B": # win
			score += 6
		if inp == "C": # loss
			pass

	elif match[0] == "B":
		if inp == "C": # win
			score += 6
		if inp == "A": # loss
			pass

	elif match[0] == "C":
		if inp == "A": # win
			score += 6
		if inp == "B": # loss
			pass
	
	print(score)
	