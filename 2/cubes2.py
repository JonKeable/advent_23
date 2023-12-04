f = open("input.txt", 'r')
lineList = f.read().splitlines()

COLORS = [
    'red',
    'green',
    'blue'
]

gameList = [l.split(':') for l in lineList]
gameDict = {g[0].split()[-1] : g[1].split(';') for g in gameList}

#print(gameDict)

gameDict = { int(id): [{color.split()[-1]:int(color.split()[0]) for color in round.split(',')} for round in game] for id, game in gameDict.items()}

#print(gameDict)

COL_DICT = {col : 0 for col in COLORS}
#print(COL_DICT)

def getGamePower(game):

    minCubes = COL_DICT.copy()
    for round in game[-1]:
        for col in COLORS:
            if col in round.keys():
                if round[col] > minCubes[col]:
                    minCubes[col] = round[col]
    
    power = 1
    for count in minCubes.values():
        power*=count
    return power

#for game in gameDict.items():
#    print(getGameSum(game))

print(sum([getGamePower(game) for game in gameDict.items()]))

