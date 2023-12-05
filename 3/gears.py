import re
f = open("input.txt", 'r')
lineList = f.read().splitlines()


nums = [list(re.finditer('\d+', line)) for line in lineList]
gears = [list(re.finditer('\*', line)) for line in lineList]

def printMatches(matchList):
    for l in matchList:
        pLine = []
        for mo in l:
            pLine.append(mo)
        print(pLine)
        
#printMatches(nums)
#print()
#printMatches(symbols)

rows = len(lineList)
cols = len(lineList[0])

print (str(rows) + ' rows * ' + str(cols) + ' cols')

grid =[['.']*cols for _ in range(rows)]

def printGrid(g):
    for r in g:
        print(r)

#printGrid(grid)

def getRatio(loc, g):
    adjNums = set()
    row = loc[0]
    col = loc[1]
    for r in range(row-1, row+2):
        for c in range(col -1, col+2):
            if r >=0 and c>=0 and r<rows and c<cols:
                if g[r][c] != '.':
                    adjNums.add(g[r][c])
    if len(adjNums) == 2 :
        return numDict[adjNums.pop()][0] * numDict[adjNums.pop()][0]
    else:
        return 0


numDict ={}
numid ='a'

for row, line in enumerate(nums):
    for mob in line:
        span = mob.span()
        numDict.update({numid: [int(mob.group()), (row, span)]})
        grid[row][span[0]:span[1]] = numid * (span[1] - span[0])
        numid = chr(ord(numid) + 1)

#printGrid(grid)
#print(numDict)

sum = 0
for i, line in enumerate(gears):
    for mob in line:
        loc = (i, mob.span()[0])
        sum += getRatio(loc, grid)
        #grid[i][mob.span()[0]] = 1

print(sum)