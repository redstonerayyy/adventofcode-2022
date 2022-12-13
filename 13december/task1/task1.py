# https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/
import ast
import os

# read pairs
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
    pairs = [ast.literal_eval(line.replace("\n", "")) for line in file.readlines() if line.replace("\n", "") != ""]
    print("Pairs", len(pairs)//2)

def checklists(leftlist, rightlist):
    # right list is larger or equal in length
    # if lists are in other list reapply checking, conversion and recursively call this function
    for i in range(max(len(rightlist), len(leftlist))):
        try:
            if type(leftlist[i]) == int and type(rightlist[i]) == int:
                if leftlist[i] > rightlist[i]:
                    return -1
                elif leftlist[i] < rightlist[i]:
                    return 1
            elif (type(leftlist[i]) == int and type(rightlist[i]) == list):
                res = checklists([leftlist[i]], rightlist[i])
                if res == -1:
                    return -1
                elif res == 1:
                    return 1

            elif (type(leftlist[i]) == list and type(rightlist[i]) == int):
                res = checklists(leftlist[i], [rightlist[i]])
                if res == -1:
                    return -1
                elif res == 1:
                    return 1

                # both list
            elif (type(leftlist[i]) == list and type(rightlist[i]) == list):
                res = checklists(leftlist[i], rightlist[i])
                if res == -1:
                    return -1
                elif res == 1:
                    return 1

        except IndexError: # smaller list ended
            if len(rightlist) < len(leftlist):
                return -1
            else:
                return 1

    # right list is larger or equal in length and no element is smaller than it's left counterpart
    return 0

def comparepairs(pairone, pairtwo):
    j = 0
    while True:
        try:
            # both ints
            if type(pairone[j]) == int and type(pairtwo[j]) == int:        
                # check if left sjde js larger
                if pairone[j] > pairtwo[j]:
                    return False
                elif pairone[j] < pairtwo[j]:
                    return True

            # one int, one list
            elif (type(pairone[j]) == int and type(pairtwo[j]) == list):
                res = checklists([pairone[j]], pairtwo[j])
                if -1 == res:
                    return False
                elif 1 == res:
                    return True
            elif (type(pairone[j]) == list and type(pairtwo[j]) == int):
                res = checklists(pairone[j], [pairtwo[j]])
                if -1 == res:
                    return False
                elif 1 == res:
                    return True
    
            # both list
            elif (type(pairone[j]) == list and type(pairtwo[j]) == list):
                res = checklists(pairone[j], pairtwo[j])
                if -1 == res:
                    return False
                elif 1 == res:
                    return True
            
        except IndexError: # one pair reached it's end
            if len(pairone) > len(pairtwo):
                return False
            else:
                return True

        j += 1


rightorderindices = []
# 2 pairs follow one on another
for i in range(0, len(pairs), 2):
    if i == (10 - 1) * 2:
        pass #breakpoint()

    if comparepairs(pairs[i], pairs[i + 1]):
        rightorderindices.append(i//2 + 1)

print("Indices", rightorderindices)
print("Sum", sum(rightorderindices))
# for i in rightorderindices:
#     print(i)
