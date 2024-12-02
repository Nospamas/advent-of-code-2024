import os
from collections import Counter

print(os.getcwd())
file = open("day1/input.txt", "r")
lines = file.read().splitlines()
# coerce to list so that we can iterate over it multiple times
tuples = list(map(lambda x: x.split("   "), lines))
lefts = sorted(map(lambda x: int(x[0]), tuples))
rights = sorted(map(lambda x: int(x[1]), tuples))
pairs = zip(lefts, rights)
diffs = map(lambda x: abs(x[0]-x[1]), pairs)
sum1 = sum(diffs)

# part 1
print(sum1)

# part 2
counted = Counter(rights)
similarities = list(map(lambda y: counted[y] * y if y in counted else 0, lefts))
sum2 = sum(similarities)

print(sum2)


