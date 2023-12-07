import re
from functools import total_ordering

f = open("input.txt", 'r')
lineList = f.read().splitlines()

#print(lineList)

mappingsDict ={}
mapOrder = []

@total_ordering
class RangeMap:
    '''
    represents the mapping of a source range to a destination range
    '''
    def __init__(self, start, range, offset) -> None:
        self.sourceStart = start
        self.sourceEnd = start+range
        self.offset = offset
        self.range = range
        self.destStart = self.sourceStart + self.offset
        self.destEnd = self.sourceEnd + self.offset
        
    def __lt__(self, other):
        return self.sourceStart < other.sourceStart
    def __repr__(self) -> str:
        return('{' + str(self.sourceStart) + '-' + str(self.sourceEnd) + ' : ' + str(self.offset) +'}')
    
    def getDestRange(self, inputRange):
        '''
        given and input range, return a tuple containing 
        -the ranges of destination values which are mapped from the given source input range
        -the range of the given source input range which cannot be mapped
        '''
        inputStart = inputRange[0]
        inputEnd = inputRange[1]
        #no values in range
        if inputStart > self.sourceEnd or  inputEnd <= self.sourceStart:
            return (None, (inputStart, inputEnd))
        #start within range
        if inputStart >= self.sourceStart:
            outputStart = inputStart+ self.offset
            #fully inside
            if inputEnd <= self.sourceEnd :
                return ([(outputStart, inputEnd+self.offset)], None)
            #overlap
            else:
                return([(outputStart, self.sourceEnd)],(self.sourceEnd, inputEnd))
        #el start below range
        #if end within range
        elif inputEnd >= self.sourceStart :
            outputStart = self.destStart
            #underlap
            if inputEnd <= self.sourceEnd :
                return ([(outputStart, inputEnd+self.offset)], (inputStart, self.sourceStart))
            #overlap and underlap, can map underlap naturally (k -> k)
            else:
                return ([(inputStart, self.sourceStart),(self.destStart, self.destEnd)], (self.sourceEnd, inputEnd))




seeds = [int(seed) for seed in lineList[0].split(' ')[1:]]

for line in lineList[1:]:

    if 'map' in line:
        mapping = tuple(re.split('\-|\s', line)[0::2])
        #print(mapping)
        source, dest = mapping[0], mapping[1]
        mappingName = source + '-' + dest
        mappingsDict.update({mappingName : []})
        mapOrder.append(source)
    elif line != '':
        line = line.split()
        sourceStart = int(line[1])
        destStart = int(line[0])
        offset = destStart - sourceStart
        mapRange = int(line[2])
        mappingsDict[mappingName].append(RangeMap(sourceStart,mapRange,offset))

#not very encapsulated...
mapOrder.append(dest)

for mapList in mappingsDict.values():
    mapList.sort()
        
print(mappingsDict)
#print(mappingsDict['seed-soil'])


def getMapping(kRange, source, dest):
    '''
    given a source range, get a list of all the mapped ranges
    from the source property to the destination property
    '''
    mapName = source + '-' + dest
    #get the relevent mapping of source-dest
    mapList = mappingsDict[mapName]
    #this will store all the possible dest ranges for the source range
    destRanges = []
    remainRange = kRange
    for rm in  mapList:
        mapping = rm.getDestRange(remainRange)
        mappedRanges = mapping[0]
        remainRange = mapping[1]
        if mappedRanges != None:
            for mr in mappedRanges:
                destRanges.append(mr)
        if remainRange == None:
            break

                

    if remainRange != None:
        destRanges.append(remainRange)
    #return the original range if no matching maps, 
    # otherwise a list of all destination ranges plus unmapped ranges
    #print(f'{kRange} {source} --> {destRanges} {dest}')
    return destRanges


locs = list()
#print(mapOrder)

seedRanges = []
seedIt = iter(seeds)
for seedStart in seedIt:
    seedRanges.append((seedStart, next(seedIt) + seedStart))

print(seedRanges)
print('|-|')
for sr in seedRanges:
    #iterate over all the different properties, e.g. soil, water
    orderIt = iter(mapOrder)
    #start by getting the first property (seed)
    start = next(orderIt)
    #the range list for this property, starting with the seed ranges
    rangeList = [sr]
    #for every property in the mapping  order list
    for id in orderIt:
        #the end is the next property in the mapping
        end = id
        #the list of destination mapping ranges
        nextList =[]
        #for every source range in the list of ranges
        for range in rangeList:
            #get a list of all the mapped ranges for this property map
            destRanges = getMapping(range, start, end)
            nextList = destRanges
        start = end
        rangeList = nextList
    locs.append(rangeList)



print('---')
print(locs)

minRange = locs[0][0][0]

for rangeList in locs:
    for range in rangeList:
        print(range)
        if range[0] < minRange:
            minRange = range[0]

print(minRange)




