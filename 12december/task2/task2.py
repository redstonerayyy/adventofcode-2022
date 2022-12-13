import string
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
    lines = [line.replace("\n", "") for line in file.readlines() if line.replace("\n", "") != ""]
    grid = [list(line) for line in lines]

# string to calculate heigh difference
letters = string.ascii_lowercase

# find start
spositions = []
for row in range(len(grid)):
    for block in range(len(grid[row])):
        if grid[row][block] == "a" or grid[row][block] == "S" :
            spositions.append([block, row])
            grid[row][block] = "a" # set to a so no error later
            break


paths = []
c = 1
for spos in spositions:
    print(c, "/", len(spositions))
    # mark place, which got already visited
    maxvisits = len(grid) * len(grid[0])
    visited = []
    pathqueque = [[spos]]
    finished = []
    while pathqueque:
        # print(len(visited), "/", maxvisits)
        el = pathqueque.pop(0)
        # if el[-1] not in visited:
        last = el[-1]
        if grid[last[1]][last[0]] == "E":
            finished.append(el)
        else:
            # left
            if last[0] > 0 and [ last[0] - 1 , last[1] ] not in visited:
                if grid[last[1]][last[0] - 1] != "E":
                    if letters.index(grid[last[1]][last[0]]) + 1 >= letters.index(grid[last[1]][last[0] - 1]):
                        visited.append([ last[0] - 1, last[1] ])
                        pathqueque.append([*el, [ last[0] - 1, last[1] ]])
                else:
                    if letters.index(grid[last[1]][last[0]]) + 1 >= 25: # z = 25
                        visited.append([ last[0] - 1, last[1] ])
                        pathqueque.append([*el, [ last[0] - 1, last[1] ]])
            # right
            if last[0] < len(grid[0]) - 1 and [ last[0] + 1 , last[1] ] not in visited:
                if grid[last[1]][last[0] + 1] != "E":
                    if letters.index(grid[last[1]][last[0]]) + 1 >= letters.index(grid[last[1]][last[0] + 1]):
                        visited.append([ last[0] + 1, last[1] ])
                        pathqueque.append([*el, [ last[0] + 1, last[1] ]])
                else:
                    if letters.index(grid[last[1]][last[0]]) + 1 >= 25: # z = 25
                        visited.append([ last[0] + 1, last[1] ])
                        pathqueque.append([*el, [ last[0] + 1, last[1] ]])
            # up
            if last[1] > 0 and [ last[0], last[1] - 1 ] not in visited:
                if grid[last[1] - 1][last[0]] != "E":
                    if letters.index(grid[last[1]][last[0]]) + 1 >= letters.index(grid[last[1] - 1][last[0]]):
                        visited.append([ last[0], last[1] - 1 ])
                        pathqueque.append([*el, [ last[0], last[1] - 1]])
                else:
                    if letters.index(grid[last[1]][last[0]]) + 1 >= 25: # z = 25
                        visited.append([ last[0], last[1] - 1 ])
                        pathqueque.append([*el, [ last[0], last[1] - 1]])
            # down
            if last[1] < len(grid) - 1 and [ last[0], last[1] + 1 ] not in visited:
                if grid[last[1] + 1][last[0]] != "E":
                    if letters.index(grid[last[1]][last[0]]) + 1 >= letters.index(grid[last[1] + 1][last[0]]):
                        visited.append([ last[0], last[1] + 1 ])
                        pathqueque.append([*el, [ last[0], last[1] + 1 ]])
                else:
                    if letters.index(grid[last[1]][last[0]]) + 1 >= 25: # z = 25
                        visited.append([ last[0], last[1] + 1 ])
                        pathqueque.append([*el, [ last[0], last[1] + 1 ]])

    shortestlength = maxvisits
    shortest = 0
    for i in range(len(finished)):
        if len(finished[i]) < shortestlength:
            shortest = i
            shortestlength = len(finished[i])

    paths.append(shortestlength)
    c += 1

print(paths)
print(min(paths) - 1)