import re

f = open("input.txt", 'r')
lineList = f.read().splitlines()
DIGIT_NAMES = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

pattern = '\d'
for digName in DIGIT_NAMES.keys():
    pattern+='|' + re.escape(digName) 

#print (pattern)


def digitise(digit):
    
    if digit in DIGIT_NAMES.keys():
        return DIGIT_NAMES.get(digit)
    else:
        return digit


digLines = [re.findall(pattern, l) for l in lineList]

print(digLines)

print(sum([int(digitise(l[0]) + digitise(l[-1])) for l in digLines]))
