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

# sort
# swap to  values of array at indices i1, i2
def swap(array_, i1, i2):
    temp = array_[i1]
    array_[i1] = array_[i2]
    array_[i2] = temp

def merge(arr1, arr2):
    # merge two sorted lists into one sorted list
    # and return this list
    i = 0
    j = 0
    result = []
    # compare and add elements
    while i < len(arr1) and j < len(arr2):
        if comparepairs(arr1[i], arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # add rest of the unfinished array
    if i < len(arr1):
        result += arr1[i:]
    else:
        result += arr2[j:]

    return result

def mergesort(_array):
    # for lists of length 2 or less return it
    # in sorted form
    if len(_array) == 1:
        return _array
    elif len(_array) == 2:
        if comparepairs(_array[0], _array[1]): # if in right order
            return _array
        return [_array[1], _array[0]]
    else:
        # recursively call the sort on two parts of the list
        middle = len(_array) // 2
        return merge(mergesort(_array[:middle]), mergesort(_array[middle:]))

# append divider packets
pairs.append([[2]])
pairs.append([[6]])

liste = mergesort(pairs)
print(liste.index([[2]]) + 1)
print(liste.index([[6]]) + 1)
print((liste.index([[6]]) + 1) * (liste.index([[2]]) + 1))