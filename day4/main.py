from time import perf_counter
timer_script_start=perf_counter()

timer_parse_start=perf_counter()
file = open("day4/input.txt", "r")
lines = list(file.read().splitlines())

timer_parse_end=timer_part1_start=perf_counter()
mLetters = ["X", "M", "A", "S"]
mLettersLen = len(mLetters)

linesLen = len(lines)
lettersLen = len(lines[0])

def searcher(vIncrement, hIncrement) -> int:
    def searchFn(rowIndex, colIndex, lines, matchIdx = 0):
        if matchIdx == mLettersLen:
            return 1
        if rowIndex < 0 or colIndex < 0 or rowIndex >= linesLen or colIndex >= lettersLen:
            return 0
        
        matchLetter = mLetters[matchIdx]
        if lines[rowIndex][colIndex] == matchLetter:
            nextRow = rowIndex+vIncrement
            nextCol = colIndex+hIncrement
            nextLetter = matchIdx+1
            return searchFn(nextRow, nextCol, lines, nextLetter)
        
        return 0

    return searchFn

searchN = searcher(-1,0)
searchS = searcher(1, 0)
searchE = searcher(0, 1)
searchW = searcher(0, -1)

searchNE = searcher(-1,1)
searchSE = searcher(1,1)
searchSW = searcher(1,-1)
searchNW = searcher(-1,-1)

def search(rowIndex: int, colIndex: int, lines) -> int:
    subTotal = 0;
    subTotal += searchN(rowIndex, colIndex, lines)
    subTotal += searchE(rowIndex, colIndex, lines)
    subTotal += searchS(rowIndex, colIndex, lines)
    subTotal += searchW(rowIndex, colIndex, lines)
    subTotal += searchNE(rowIndex, colIndex, lines)
    subTotal += searchSE(rowIndex, colIndex, lines)
    subTotal += searchSW(rowIndex, colIndex, lines)
    subTotal += searchNW(rowIndex, colIndex, lines)

    return subTotal

total = 0
for rowIndex,line in enumerate(lines):
    for colIndex,letter in enumerate(line):
        if letter == mLetters[0]:
            total += search(rowIndex, colIndex, lines)
# part 1
print(total)
timer_part1_end=timer_part2_start=perf_counter()

mLetters2 = ["M", "A", "S"]
mLettersLen2 = len(mLetters2)


def searcher2(vIncrement, hIncrement):
    def searchFn2(rowIndex, colIndex, lines, matchIdx = 0):
        def searchCrossCheck(crossCheck = True):
            if matchIdx == mLettersLen2:
                
                if not crossCheck:
                    return 1
                
                # calculate starting location
                sRowIndex = rowIndex - (mLettersLen2*vIncrement)
                sColIndex = colIndex - (mLettersLen2*hIncrement)

                validOffsetDirection = validOffsetDirections[(vIncrement, hIncrement)]

                if (validOffsetDirection[0][0]((sRowIndex+validOffsetDirection[0][1]), (sColIndex+validOffsetDirection[0][2]), lines, matchIdx = 0)(False) == 1 or  
                    validOffsetDirection[1][0]((sRowIndex+validOffsetDirection[1][1]), (sColIndex+validOffsetDirection[1][2]), lines, matchIdx = 0)(False) == 1):
                    return 1
                
                return 0

            if rowIndex < 0 or colIndex < 0 or rowIndex >= linesLen or colIndex >= lettersLen:
                return 0
            
            matchLetter = mLetters2[matchIdx]
            if lines[rowIndex][colIndex] == matchLetter:
                nextRow = rowIndex+vIncrement
                nextCol = colIndex+hIncrement
                nextLetter = matchIdx+1
                return searchFn2(nextRow, nextCol, lines, nextLetter)(crossCheck)
            
            return 0
        return searchCrossCheck
    return searchFn2



searchN2 = searcher2(-1,0)
searchS2 = searcher2(1, 0)
searchE2 = searcher2(0, 1)
searchW2 = searcher2(0, -1)

searchNE2 = searcher2(-1,1)
searchSE2 = searcher2(1,1)
searchSW2 = searcher2(1,-1)
searchNW2 = searcher2(-1,-1)

# valid offsets always start at M and must cross A, we can work out the coord offset
# there might be a generalized solution to this, but I can't think it up right now

# the dictionary is indexed by the coordinates representing the incrementing direction for
# search. in a language with better types I'd probably make this a named type and make it a bit
# more readable

# values are the search function to run, with the offset from our original search 
# location. one of them must be valid for this to be a cross
# ↖↗↘↙ ←↑→↓
validOffsetDirections = {
    # . M .
    # → A ← searchN
    # . S .
    (-1,0): [(searchE2, -1,-1), (searchW2,-1,1)],

    # . S .
    # → A ← searchS
    # . M .
    (1,0): [(searchE2, 1,-1), (searchW2,1,1)],

    # . ↓ .
    # M A S searchE
    # . ↑ .
    (0,1): [(searchS2, -1,1), (searchN2,1,1)], 

    # . ↓ .
    # S A M searchW
    # . ↑ . 
    (0,-1): [(searchS2,-1,-1), (searchN2,1,-1)],

    # ↘ . S
    # . A . searchNE
    # M . ↖
    (-1,1): [(searchSE2,-2,0),(searchNW2,0,2)],

    # ↘ . M
    # . A . searchSW
    # S . ↖
    (1,-1): [(searchSE2, 0,-2),(searchNW2, 2,0)], 

    # M . ↙
    # . A . searchSE
    # ↗ . S
    (1,1): [(searchNE2,2,0),(searchSW2,0,2)],

    # S . ↙
    # . A . searchNW
    # ↗ . M
    (-1,-1): [(searchSW2,-2,0),(searchNE2,0,-2)],
}



def search2(rowIndex: int, colIndex: int, lines) -> int:
    subTotal = 0;
    # its only X mas, not cross mas.
    # subTotal += searchN2(rowIndex, colIndex, lines)()
    # subTotal += searchE2(rowIndex, colIndex, lines)()
    # subTotal += searchS2(rowIndex, colIndex, lines)()
    # subTotal += searchW2(rowIndex, colIndex, lines)()
    subTotal += searchNE2(rowIndex, colIndex, lines)()
    subTotal += searchSE2(rowIndex, colIndex, lines)()
    subTotal += searchSW2(rowIndex, colIndex, lines)()
    subTotal += searchNW2(rowIndex, colIndex, lines)()

    return subTotal

total2 = 0
for rowIndex,line in enumerate(lines):
    for colIndex,letter in enumerate(line):
        if letter == mLetters2[0]:
            total2 += search2(rowIndex, colIndex, lines)

# answer will be doubled because we're detecting each M in the cross, just halve it
# part 2
print(total2/2)
timer_part2_end=timer_script_end=perf_counter()

print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.5f}
Part1: {timer_part1_end-timer_part1_start:3.5f}
Part2: {timer_part2_end-timer_part2_start:3.5f}
Total: {timer_script_end-timer_script_start:3.5f}""")