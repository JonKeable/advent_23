import re
f = open("input.txt", 'r')
lineList = f.read().splitlines()


nums = [list(re.finditer('\d+', line)) for line in lineList]
symbols = [list(re.finditer('[^0123456789\.]', line)) for line in lineList]

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

grid =[[0]*cols for _ in range(rows)]

def printGrid(g):
    for r in g:
        print(r)

#printGrid(grid)

def setCollideBox(loc, g):
    row = loc[0]
    col = loc[1]
    for r in range(row-1, row+2):
        for c in range(col -1, col+2):
            if r >=0 and c>=0 and r<rows and c<cols:
                grid[r][c] = 1
    g[loc[0]][loc[1]] = 1

for i, line in enumerate(symbols):
    for mob in line:
        loc = (i, mob.span()[0])
        setCollideBox(loc,grid)

#print("-mat-")
#printGrid(grid)

sum = 0
for row, line in enumerate(nums):
    for mob in line:
        if 1 in grid[row][mob.span()[0]:mob.span()[1]]:
            sum += int(mob.group())

print(sum)