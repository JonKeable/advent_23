from collections import OrderedDict
from collections import deque
import timeit

FILENAME = 'input.txt'

f = open(FILENAME, 'r')
line_list = [[int(e) for e in line.split()] for line in f.read().splitlines()]

print(line_list)


def slow_sol(line_list):
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
            #print(f'lev: {level -1}')
            this_seq = levels[level]
            prev_seq = levels[level-1]
            #print(this_seq)
            #print(prev_seq)
            prev_seq = list(reversed(prev_seq))
            prev_seq.append(prev_seq[-1] - this_seq[0])
            prev_seq = list(reversed(prev_seq))
            #print(f'new: {prev_seq}')
            levels[level-1] = prev_seq
        sum += prev_seq[0]
        #print(prev_seq[-1])
    return sum
#988

#print(slow_sol(line_list))

def deq_sol(line_list):
    sum = 0
    for line in line_list:
        n = len(line)
        not_zeros = False
        levels = OrderedDict()
        levels.update({0: deque(line)})
        next_line = levels[0]
        level = 0
        all_zeros = False
        while(not all_zeros):
            level += 1
            next_level = deque()
            levels.update({level: next_level})
            for i in range(len(next_line)-1):
                diff = next_line[i+1] - next_line[i]
                next_level.append(diff)
            if set(next_level) == {0}:
                all_zeros = True
            next_line = next_level
        for level in reversed(list(levels.keys())[1:]):
            this_seq = levels[level]
            prev_seq = levels[level-1]
            prev_seq.appendleft(prev_seq[0] - this_seq[0])
        sum += prev_seq[0]
        #print(prev_seq[-1])
    return sum

s1,s2 = 0, 0

def s1():
    s1 = slow_sol(line_list)

def s2():
    s2 =deq_sol(line_list)

t1 = timeit.Timer(s1).repeat(3,100)
t2 = timeit.Timer(s2).repeat(3,100)

print(f'{t1}, {t2}')

# looks like slow_sol isnt so slow after all
# maybe my deque code is inneficient somewher?