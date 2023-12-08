import re
FILENAME = 'input.txt'

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


START = 'AAA'
END = 'ZZZ'
end_found = False
curr_node = START
steps =0

while (not end_found):
    for dir in directions:
        steps += 1
        if dir == 'R':
            curr_node = graph[curr_node].R
        else:
            curr_node = graph[curr_node].L
        
        if curr_node == END:
            end_found = True
            break

print(steps)

