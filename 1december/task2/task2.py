# get elves in an array where consisting of arrays which contain
# the calorie numbers for each elve
elves = []
with open("input.txt", encoding='utf-8') as file:
    lines = file.readlines()
    # add calories to an elve until a newline 
    # which is when the next elve starts
    elve = []
    while lines:
        el = lines.pop(0)
        if el == "\n":
            if len(elve) > 0:
                elves.append(elve[:])
                elve = []
        else:
            elve.append(int(el))

    # append last elve if no newline is encountred
    if len(elve) > 0:
        elves.append(elve[:])

# calculate maximum
# loop over all elves, calculate the sum of their calories
# and store it in an array
# sort the array an sum up the calories of the top 3 elves
calories = [sum(elve) for elve in elves]
calories.sort()

# calculate max numbers
print(calories[-1] + calories[-2] + calories[-3])
