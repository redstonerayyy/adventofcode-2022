import os

# parse file
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
	lines = file.readlines()
	lines = [i.replace("\n", "") for i in lines if i.replace("\n", "") != ""]

# globals
lscommand = "$ ls"
cdcommand = "$ cd"

# parse directories
i = 0
folders = {}
path = ["/"]
currfolder = None
allfiles = []
while i < len(lines):
	l = lines[i]
	if l[:4] == lscommand:
		pass
	elif l[:4] == cdcommand:
		if currfolder != None:
			folders[currfolder["path"]] = currfolder
		# new folder
		if l[5:] == "/":
			path = ["/"]
		elif l[5:] == ".." and len(path) > 1: # remove last dir
			path.pop(-1)
		else:
			path.append(l[5:] + "/")
		
		currfolder = {"path": ''.join(path), "files": [], "directories": []}
		# skip if folder already scanned
		if ''.join(path) in folders:
			currfolder = None # prevent adding empty folder
			i += 1
			while lines[i][:4] != cdcommand:
				i += 1
			i -= 1

	else:
		if l[:3] == "dir": # dir
			currfolder["directories"].append(l[4:])
		else: # file
			currfolder["files"].append(l.split(" "))
			allfiles.append(int(l.split(" ")[0]))
	i += 1
	if i < len(lines): # add last
		if currfolder != None:
			folders[currfolder["path"]] = currfolder


# get size for each folder
def getdirsize(path):
	visited = []
	size = 0
	queque = [path]
	while queque:
		p = queque.pop(0)
		for file in folders[p]["files"]:
			size += int(file[0]) 

		for directory in folders[p]["directories"]:
			newp = p + directory + "/"
			if not newp in visited:
				visited.append(newp)
				queque.append(newp)

	return size

sizes = []
for f in folders:
	sizes.append([folders[f]["path"], getdirsize(folders[f]["path"])])

# t2
sizenums = [i[1] for i in sizes]
maximum = 70000000
unused = maximum - max(sizenums)
required = 30000000 - unused
smallest = max(sizenums) # big number
for s in sizes:
	if s[1] >= required:
		if s[1] < smallest:
			smallest = s[1]

print(smallest)