import re


f = open("test.txt", 'r')
lineList = f.read().splitlines()

#print(lineList)

mappingsDict ={}
mapOrder = []

seeds = [int(seed) for seed in lineList[0].split(' ')[1:]]

for line in lineList[1:]:

    if 'map' in line:
        mapping = tuple(re.split('\-|\s', line)[0::2])
        #print(mapping)
        source, dest = mapping[0], mapping[1]
        mappingName = source + '-' + dest
        mappingsDict.update({mappingName : {}})
        mapOrder.append(source)
    elif line != '':
        line = line.split()
        sourceStart = int(line[1])
        destStart = int(line[0])
        offset = destStart - sourceStart
        mapRange = int(line[2])
        mappingsDict[mappingName].update({(sourceStart,sourceStart+mapRange):offset})

#not very encapsulated...
mapOrder.append(dest)




        
#print(mappingsDict)
#print(mappingsDict['seed-soil'])

def getMapping(k, source, dest):
    mapName = source + '-' + dest
    map = mappingsDict[mapName]
    for mapRange, offset in map.items():
        if k in range(mapRange[0], mapRange[1]):
            return k + offset
    return k


locs = set()
#print(mapOrder)

seedRanges = []
seedIt = iter(seeds)
for seedStart in seedIt:
    seedRanges.append((seedStart, next(seedIt) + seedStart))

print(seedRanges)

for sr in seedRanges:
    for seed in range(sr[0], sr[1]):
        mapIt = iter(mapOrder)
        start = next(mapIt)
        res = seed
        for id in mapIt:
            end = id
            res = getMapping(res, start, end)
            start = end
        locs.add(res)

print(locs)
print(min(locs))



