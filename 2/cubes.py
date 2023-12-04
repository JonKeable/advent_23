f = open("input.txt", 'r')
lineList = f.read().splitlines()

TEST_GAME = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

gameList = [l.split(':') for l in lineList]
gameDict = {g[0].split()[-1] : g[1].split(';') for g in gameList}

#print(gameDict)

gameDict = { int(id): [{color.split()[-1]:int(color.split()[0]) for color in round.split(',')} for round in game] for id, game in gameDict.items()}

#print(gameDict)

def getGameSum(game):
    for round in game[-1]:
        for col, no in TEST_GAME.items():
            if col in round.keys():
                if round[col] > no:
                    return 0
    
    return game[0]

#for game in gameDict.items():
#    print(getGameSum(game))

print(sum([getGameSum(game) for game in gameDict.items()]))

