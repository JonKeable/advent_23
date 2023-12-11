from collections import OrderedDict

# try sol by starting from S and looking for chain, 
# rather than creating a graph of all elements, finding the loop, then half the length
# maybe not a very good idea in hindsight...

#FILENAME = 'test1.txt'
#FILENAME = 'test2.txt'
FILENAME = 'input.txt'
CARDINALS = {'N', 'S', 'E', 'W'}

class Pipe:

    SHAPE_LINKS = {'-': 'EW',
                '|': 'NS',
                'J': 'NW',
                'F': 'SE',
                '7': 'SW',
                'L': 'NE'
                }
    
    def __init__(self, row, col, shape, from_dir) -> None:
        self.row = row
        self.col = col
        self.shape = shape
        self.links = self.SHAPE_LINKS[shape]
        self.from_dir = from_dir
        self.next_dir = (set(self.links) - {from_dir}).pop()
    
    @classmethod
    def get_links(cls, shape):
        return cls.SHAPE_LINKS[shape]
    
    @classmethod
    def shape_has_link(cls, shape, direction):
        '''
        returns True if the given pipe shape links to the specified cardinal direction
        e.g. 'L' has a N link, but not a W link 
        '''
        return direction in cls.get_links(shape)
    
    def has_link(self, direction):
        '''
        returns True if the given pipe links to the specified cardinal direction
        e.g. 'L' has a N link, but not a W link 
        '''
        return direction in self.links
    
    def __eq__(self, other) -> bool:
        return (self.row, self.col) == (other.row, other.col)
    
    def __repr__(self) -> str:
        return f'{self.shape} @ {self.row},{self.col}'
    
    def __hash__(self) -> int:
        return hash(str(self))


class PipeGrid:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
    
    def __repr__(self) -> str:
        repr = ''
        repr += f'{self.h} x {self.w}'
        for line in self.grid:
            repr+=('\n' + line)
        return repr
    
    def check_dir(self, direction, row, col):
        assert direction in CARDINALS
        if direction == 'N':
            return self.check_north(row, col)
        if direction == 'S':
            return self.check_south(row, col)
        if direction == 'E':
            return self.check_east(row, col)
        if direction == 'W':
            return self.check_west(row, col)

    def check_north(self, row, col):
        row -= 1
        if row < 0:
            return False
        else:
            pipe_shape = self.grid[row][col]
            if pipe_shape == '.':
                return False
            if Pipe.shape_has_link(pipe_shape, 'S'):
                return Pipe(row, col, pipe_shape, 'S')
            else:
                return False
            
    def check_south(self, row, col):
        row += 1
        if row >= self.h:
            return False
        else:
            pipe_shape = self.grid[row][col]
            if pipe_shape == '.':
                return False
            if Pipe.shape_has_link(pipe_shape, 'N'):
                return Pipe(row, col, pipe_shape, 'N')
            else:
                return False
            
    def check_east(self, row, col):
        col += 1
        if col >= self.w:
            return False
        else:
            pipe_shape = self.grid[row][col]
            if pipe_shape == '.':
                return False
            if Pipe.shape_has_link(pipe_shape, 'W'):
                return Pipe(row, col, pipe_shape, 'W')
            else:
                return False
            
    def check_west(self, row, col):
        col -= 1
        if col < 0:
            return False
        else:
            pipe_shape = self.grid[row][col]
            if pipe_shape == '.':
                return False
            if Pipe.shape_has_link(pipe_shape, 'E'):
                return Pipe(row, col, pipe_shape, 'E')
            else:
                return False


def 

def find_chain(pipe_grid):

    for row, line in enumerate(pipe_grid.grid):
        if 'S' in line:
            start_loc = (row, line.index('S'))


    print(start_loc)

    join_found = False
    next_pipes =[]
    seen_pipes =set()

    for direction in CARDINALS:
        pipe = pipe_grid.check_dir(direction, start_loc[0], start_loc[1])
        if pipe :
            next_pipes.append(pipe)
            seen_pipes.add(pipe)

    i=1
    while not join_found:
        #print(next_pipes)
        i+=1
        linked_pipes = []
        for pipe in next_pipes:
            next_pipe = pipe_grid.check_dir(pipe.next_dir, pipe.row, pipe.col)
            if next_pipe:
                if next_pipe in seen_pipes:
                    result = i-1
                    print(next_pipe)
                    return result
                linked_pipes.append(next_pipe)
        if len(linked_pipes) != len(set(linked_pipes)):
            result = i
            print(linked_pipes)
            return result
        else:
            for pipe in linked_pipes:
                seen_pipes.add(pipe)
                next_pipes = linked_pipes
            
        


f = open(FILENAME, 'r')
line_list = [line for line in f.read().splitlines()]
pipe_grid = PipeGrid(line_list)
print(pipe_grid)

print(find_furthest(pipe_grid))


