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

START = 'A'
END = 'Z'

start_nodes = []
for node in graph.keys():
    if node[2] == START:
        start_nodes.append(node)

print(start_nodes)

end_found = False
curr_nodes = start_nodes
steps =0

def are_end_nodes(node_list):
    for node in node_list:
        if node[2] != 'Z':
            return False
    return True

while (not end_found):
    for dir in directions:
        steps += 1
        next_nodes = []
        for node in curr_nodes:
            if dir == 'R':
                next_nodes.append(graph[node].R)
            else:
                next_nodes.append(graph[node].L)
            
        if are_end_nodes(next_nodes):
            end_found = True
            break
        curr_nodes = next_nodes

print(steps)

