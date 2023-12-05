import re
import math

f = open("input.txt", 'r')
lineList = f.read().splitlines()

cardList = [tuple([set([int(no) for no in e.split()]) for e in re.split(':|\|', line)[-2:]]) for line in lineList]

#print(cardList)

print(sum([math.floor(pow(2, len(card[0].intersection(card[1]))-1)) for card in cardList]))