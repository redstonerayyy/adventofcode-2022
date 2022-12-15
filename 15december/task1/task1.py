import os

with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
	lines = [line.replace("\n", "") for line in file if line.replace("\n", "") != ""]
	sensorpairs = []
	for sensor in lines:
		parts = sensor.split(" ")
		xsensor = int(parts[2].split("=")[1].replace(",", ""))
		ysensor = int(parts[3].split("=")[1].replace(":", ""))
		xbeacon = int(parts[8].split("=")[1].replace(",", ""))
		ybeacon = int(parts[9].split("=")[1])
		xdistance = abs(xsensor - xbeacon)
		ydistance = abs(ysensor - ybeacon)
		sensorpairs.append([xsensor, ysensor, xbeacon, ybeacon, xdistance, ydistance])

# left most object
xcords = [pair[0] for pair in sensorpairs] + [pair[2] for pair in sensorpairs]
ycords = [pair[1] for pair in sensorpairs] + [pair[3] for pair in sensorpairs]
xmin = min(xcords)
xmax = max(xcords)

# get blocked parts at y height
yheight = 10
ycordsfilled = []
for pair in sensorpairs:
	# if pair[0] == 8:
	# 	breakpoint()
	if pair[1] <= yheight:
		shift = 0
		width = pair[4] * 2
		while pair[1] + shift <= pair[1] + pair[5]:
			if pair[1] + shift == yheight:
				ycordsfilled.append([width, pair[0], pair[1]])
				break		
			width -= 2
			shift += 1
		
	elif pair[1] > yheight:
		shift = 0
		width = 1
		while pair[1] - shift >= pair[1] - pair[5]:
			if pair[1] - shift == yheight:
				ycordsfilled.append([width, pair[0], pair[1]])
				break		
			width += 2
			shift += 1
# calculate width

print(ycordsfilled)

