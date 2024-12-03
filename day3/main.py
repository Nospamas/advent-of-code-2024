import re
from time import perf_counter
timer_script_start=perf_counter()

timer_parse_start=perf_counter()
file = open("day3/input.txt", "r")
text = file.read()

timer_parse_end=timer_part1_start=perf_counter()
test = re.compile(r"mul\((\d+),(\d+)\)")

allMatch = test.findall(text)

multiples = map(lambda x: int(x[0]) * int(x[1]), allMatch)
total = sum(multiples)

print(total)
timer_part1_end=timer_part2_start=perf_counter()

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
timer_part2_end=timer_script_end=perf_counter()

print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.5f}
Part1: {timer_part1_end-timer_part1_start:3.5f}
Part2: {timer_part2_end-timer_part2_start:3.5f}
Total: {timer_script_end-timer_script_start:3.5f}""")