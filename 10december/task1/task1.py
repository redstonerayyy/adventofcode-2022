with open("input.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines() if line.replace("\n", "") != ""]
    lines = [[line] if line == "noop" else line.split(" ") for line in lines]

X = 1
cycle = 1
cmdindex = 0
carry = False # carry for 2 cycle instructions
sstrength = 0
crt = [0 for i in range(40 * 6)]


while cycle < 221:
    # check cycle
    if cycle == 20 or cycle % 40 == 20:
        print(cycle, X * cycle)
        sstrength += X * cycle

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

print(sstrength)