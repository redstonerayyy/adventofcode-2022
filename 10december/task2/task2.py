with open("input.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines() if line.replace("\n", "") != ""]
    lines = [[line] if line == "noop" else line.split(" ") for line in lines]

X = 1
cycle = 1
cmdindex = 0
carry = False # carry for 2 cycle instructions
crt = [0 for i in range(40 * 6)]

while cycle < 241:
    # draw pixel
    print(cycle - 1, X)
    if cycle == 1:
        print([X - 1 + j + i * 40 for j in range(3) for i in range(6)])
    if (cycle - 1) in [X - 1 + j + i * 40 for j in range(3) for i in range(6)]:
        crt[cycle - 1] = "#"
    else:
        crt[cycle - 1] = "."
    
    # execute command
    cmd = lines[cmdindex]
    if cmd[0] == "noop":
        cmdindex += 1
    else: # addx
        if carry:
            carry = False
            X += int(cmd[1])
            cmdindex += 1
        else:
            carry = True

    cycle += 1

for i in range(6):
    for j in range(40):
        print(crt[i * 40 + j], end="")
    print("")