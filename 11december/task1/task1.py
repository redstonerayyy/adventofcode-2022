# read monkeys

def parsemonkeyraw(rawmonkey):
    mnumber = int(rawmonkey[0].split(" ")[1].replace(":", ""))
    mitems = [int(item.replace(",", "")) for item in rawmonkey[1].split(" ")[2:]]
    moperation = rawmonkey[2].split(" ")[4:]
    mdivtest = int(rawmonkey[3].split(" ")[-1])
    mtrue = int(rawmonkey[4].split(" ")[-1])
    mfalse = int(rawmonkey[5].split(" ")[-1])
    return [
        mnumber,
        mitems,
        moperation,
        mdivtest,
        mtrue,
        mfalse,
    ]

class Monkey:
    def __init__(self, monkeyinfo) -> None:
        self.monkeyinfo = monkeyinfo
        self.id = monkeyinfo[0]
        self.items = monkeyinfo[1]
        self.operation = monkeyinfo[2]
        self.divnum = monkeyinfo[3]
        self.truetransfermonkey = monkeyinfo[4]
        self.falsetransfermonkey = monkeyinfo[5]
        self.inspectioncount = 0

    def inspectitem(self):
        # calculate worry level
        try:
            item = self.items.pop(0)
            worry = item
        except:
            return False # return false if no item left

        # operation
        sign = self.operation[0]
        if self.operation[1] == "old":
            onum = worry
        else:
            onum = int(self.operation[1])
        
        if sign == "+":
            worry += onum
        elif sign == "*":
            worry *= onum
        
        # relief
        worry = int(worry / 3)

        # check
        # for some reason transfer the item with changed worry ??
        if worry % self.divnum == 0:
            self.transfer(worry, self.truetransfermonkey, monkeys)
        else:
            self.transfer(worry, self.falsetransfermonkey, monkeys)

        # add to counter
        self.inspectioncount += 1
        return True # true if item

    def transfer(self, item, monkeyid, monkeylist):
        for m in monkeylist:
            if m.id == monkeyid:
                m.items.append(item) 

with open("input.txt") as file:
    lines = [line.replace("\n", "").strip() for line in file.readlines() if line.replace("\n", "").strip() != ""]
    monkeys = []
    for i in range(0, len(lines), 6):
        monkeys.append(Monkey(parsemonkeyraw(lines[i: i + 6])))

    for m in monkeys:
        print(m.id, m.items)
    
    for i in range(20): # 20 rounds
        for j in range(len(monkeys)):
            while monkeys[j].inspectitem():
                pass

    counts = [m.inspectioncount for m in monkeys]
    counts.sort()
    print(counts[-1],counts[-2])
    print(counts[-1] * counts[-2])

    for m in monkeys:
        print(m.id, m.items, m.inspectioncount)