import re
import math

f = open("input.txt", 'r')
lineList = f.read().splitlines()

cardList = [tuple([set([int(no) for no in e.split()]) for e in re.split(':|\|', line)[-2:]]) for line in lineList]

#print(cardList)

wins = [math.floor(len(card[0].intersection(card[1]))) for card in cardList]

print(wins)
noCards = [1]*len(wins)

#would recursion be better?

for i, card in enumerate(wins):
    for k in range(noCards[i]):
        for j in range(card):
            noCards[i+j+1] += 1

print(sum(noCards))