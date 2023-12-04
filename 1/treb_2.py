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

R_DIGIT_NAMES = {k[::-1] : v for  (k,v) in DIGIT_NAMES.items()}
print(R_DIGIT_NAMES)

fPattern = rPattern = '\d'

for digName in DIGIT_NAMES.keys():
    fPattern+='|' + re.escape(digName)

for digName in R_DIGIT_NAMES.keys():
    rPattern+='|' + re.escape(digName)  

print (fPattern)
print (rPattern)

def digitise(digit):
    
    if digit in DIGIT_NAMES.keys():
        return DIGIT_NAMES.get(digit)
    else:
        return digit



print(sum([int(digitise(re.search(fPattern, l).group()) + digitise(re.search(rPattern, l[::-1]).group()[::-1])) for l in lineList]))
