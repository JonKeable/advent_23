import re

#too slow

f = open("input.txt", 'r')
lineList = f.read().splitlines()

print(lineList)

mappingsDict ={}
mapOrder = []

seeds = [int(seed) for seed in lineList[0].split(' ')[1:]]

for line in lineList[1:]:

    if 'map' in line:
        mapping = tuple(re.split('\-|\s', line)[0::2])
        print(mapping)
        source, dest = mapping[0], mapping[1]
        mappingName = source + '-' + dest
        mappingsDict.update({mappingName : {}})
        mapOrder.append(source)
    elif line != '':
        line = line.split()
        sourceStart = int(line[1])
        destStart = int(line[0])
        mapRange = int(line[2])
        for i in range(mapRange):
            mappingsDict[mappingName].update({sourceStart+i:destStart+i})

#not very encapsulated...
mapOrder.append(dest)




        
#print(mappingsDict)
print(mappingsDict['seed-soil'])

def getMapping(k, source, dest):
    mapName = source + '-' + dest
    map = mappingsDict[mapName]
    return ( map[k] if k in map else k)


locs = set()
print(mapOrder)


for seed in seeds:
    mapIt = iter(mapOrder)
    start = next(mapIt)
    res = seed
    for id in mapIt:
        end = id
        res = getMapping(res, start, end)
        start = end
    print(res)




