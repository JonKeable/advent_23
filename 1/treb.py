import re

f = open("input.txt", 'r')
lineList = f.read().splitlines()
pattern = '\d'
print(sum([int(re.search(pattern, l).group() + re.search(pattern, l[::-1]).group()) for l in lineList]))
