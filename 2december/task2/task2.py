# read matches from file as arrays of the to letters
matches = []

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		line = line.replace("\n", "")
		if line != "":
			matches.append(line.split(" "))


score = 0
# use if statements to check what the enemy has
# determine the score you need to add if u want to
# win, lose or draw
for match in matches:
	# match outcome
	inp = match[1]
	if match[0] == "A":
		if inp == "Z": # win
			score += 6 + 2
		elif inp == "Y": # draw
			score += 3 + 1
		elif inp == "X": # lose
			score += 3

	elif match[0] == "B":
		if inp == "Z": # win
			score += 6 + 3
		elif inp == "Y": # draw
			score += 3 + 2
		elif inp == "X": # lose
			score += 1

	elif match[0] == "C":
		if inp == "Z": # win
			score += 6 + 1
		elif inp == "Y": # draw
			score += 3 + 3
		elif inp == "X": # lose
			score += 2

	print(score)
	