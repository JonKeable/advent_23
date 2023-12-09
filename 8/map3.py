import re
from math import lcm
FILENAME = 'input.txt'
#FILENAME = 'test3.txt'

class MapNode:
    def __init__(self, label, L, R) -> None:
        self.label = label
        self.L = L
        self.R = R

    def __repr__(self) -> str:
        return f'{self.label} = ({self.L},{self.R})'

f = open(FILENAME, 'r')
line_list = [line.split("=") for line in f.read().splitlines()]

#print(line_list)

directions = line_list.pop(0)[0]
line_list.pop(0)

#print(line_list)

graph = {}
for line in line_list:
    label = line[0].strip()
    #print(label)
    children = re.sub('\(|\)','',line[1].strip()).split(', ')
    #print(children)
    graph.update({label: MapNode(label, children[0], children[1])})

START = 'A'
END = 'Z'

start_nodes = []
for node in graph.keys():
    if node[2] == START:
        start_nodes.append(node)

print(start_nodes)

end_found = False


def is_end_node(node):
    return node[2] == 'Z'



steps_list =[]
for node in start_nodes:
    steps =0
    end_found = False
    curr_node = node
    while (not end_found):
        for dir in directions:
            steps += 1
            if dir == 'R':
                curr_node = graph[curr_node].R
            else:
                curr_node = graph[curr_node].L
            
            if curr_node[2] == 'Z':
                end_found = True
                break
    steps_list.append(steps)
    

print(steps_list)


print(prod)

# basically find the steps to each first end point pf each path from each start point
# then the lowest common multiple of all these path-steps is the first time that we
# will reach the end point of all paths at the same time
step_lcm=1
for steps in steps_list:
    step_lcm = lcm(step_lcm, steps)

print(step_lcm)