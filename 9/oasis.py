from collections import OrderedDict

FILENAME = 'input.txt'

f = open(FILENAME, 'r')
line_list = [[int(e) for e in line.split()] for line in f.read().splitlines()]

print(line_list)


sum = 0
for line in line_list:
    #print(line)
    n = len(line)
    not_zeros = False
    levels = OrderedDict()
    levels.update({0: line})
    next_line = line
    level = 0
    all_zeros = False
    while(not all_zeros):
        level += 1
        next_level = []
        levels.update({level: next_level})
        for i, x in enumerate(next_line[:-1]):
            diff = next_line[i+1] - x
            next_level.append(diff)
        if set(next_level) == {0}:
            all_zeros = True
        #print(next_level)
        next_line = next_level
    #print(levels)
    for level in reversed(list(levels.keys())[1:]):
        #print(level)
        this_seq = levels[level]
        prev_seq = levels[level-1]
        prev_seq.append(prev_seq[-1] + this_seq[-1])
    sum += prev_seq[-1]
    #print(prev_seq[-1])


print(sum)


