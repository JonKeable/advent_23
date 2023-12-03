import re

f = open("test2.txt", 'r')
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

def digitise(line):
    
    for key, val in DIGIT_NAMES.items():
        line = line.replace(key, val)
    return line

digitsList = [digitise(l) for l in lineList]
print(digitsList)
pattern = '\d'
print(sum([int(re.search(pattern, l).group() + re.search(pattern, l[::-1]).group()) for l in digitsList]))
