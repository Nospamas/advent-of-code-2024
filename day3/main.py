import re
file = open("day3/input.txt", "r")
text = file.read()
test = re.compile(r"mul\((\d+),(\d+)\)")

allMatch = test.findall(text)

multiples = map(lambda x: int(x[0]) * int(x[1]), allMatch)
total = sum(multiples)

print(total)


# split into do segements, anything at the beginning of these should be run
doSegments = text.split("do()")
# split into don't segments, anything after a don't shouldn't be run, so we can throw it away
dontSegments = map(lambda x: x.split("don't()")[0], doSegments)

# join it all back up
newText = "".join(dontSegments)

# then do the same as part1
allMatch2 = test.findall(newText)
multiples2 = map(lambda x: int(x[0]) * int(x[1]), allMatch2)
total2 = sum(multiples2)

print(total2)