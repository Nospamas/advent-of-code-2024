from collections import Counter

file = open("day2/input.txt", "r")
lines = list(file.read().splitlines())

tuples = map(lambda x: [int(y) for y in x.split(" ")], lines)

def isSafe(tup):
    lastEntry = tup[0]
    increasing = tup[0] < tup[1]
    for entry in tup[1::]:
        if (entry == lastEntry):
            return False
        if abs(entry - lastEntry) > 3:
            return False
        if increasing and entry < lastEntry:
            return False
        if not increasing and entry > lastEntry:
            return False
        
        lastEntry = entry
    
    return True

areSafe = map(lambda x: isSafe(x), tuples)
safesCounted = Counter(areSafe)

# part 1
print(safesCounted[True])


# very brute force, but whatever
def dampenedSafe(tup):
    if isSafe(tup):
        return True
    
    for index,ent in enumerate(tup):
        tup2 = tup.copy()
        tup2.pop(index)
        if isSafe(tup2):
            return True

tuples2 = map(lambda x: [int(y) for y in x.split(" ")], lines)
areSafe2 = map(lambda x: dampenedSafe(x), tuples2)
safesCounted2 = Counter(areSafe2)

# part 2
print(safesCounted2[True])