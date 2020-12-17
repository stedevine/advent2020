def solve_problem(grid):
    get_next_state(grid)
    display(grid)
    c = 0
    for l in grid:
        c += l.count('#')
    
    print(c)

def count_occupied(grid):
    c = 0
    for l in grid:
        c += l.count('#')
    return c

def get_next_state(grid):
    changes = []
    while(True):
        for row in range(0,len(grid)):
            for col in range(0, len(grid[row])):
                change = get_change(grid,row,col)
                if change:
                    changes.append(change)
        #print(changes)
        if len(changes) == 0:
            break
        apply_changes(changes,grid)
        changes = []
        display(grid)
        print(count_occupied(grid))
        input()

    #if len(changes) == 0:
    #    break    
    #print(changes)
    #apply_changes(changes,grid)

def display(grid):
    for i in range(0,len(grid)):
        print(' {}'.format(grid[i]))

def apply_changes(changes, grid):
    for (row,col) in changes:
        new_row = list(grid[row])
        new_row[col] = 'L' if grid[row][col] == '#' else '#'
        grid[row] = ''.join(new_row)

def get_change(grid, row, col):
    if grid[row][col] == '.':
        # Nothing to do
        return None
    
    max_col = len(grid[row]) -1
    max_row = len(grid) -1

    num_occupied = 0
    # top left
    if (row > 0 and col > 1 and grid[row-1][col-1] == '#'):
        num_occupied += 1
    # top
    if (row > 0 and grid[row-1][col] == '#'):
        num_occupied += 1
    # top right
    if (row > 0 and col < max_col and grid[row-1][col+1] == '#'):
        num_occupied += 1

    # left
    if (col > 0 and grid[row][col-1] == '#'):
        num_occupied += 1
    # right
    if (col < max_col and grid[row][col+1] == '#'):
        num_occupied += 1
    
    # bottom left
    if (row < max_row and col > 1 and grid[row+1][col-1] == '#'):
        num_occupied += 1
    # bottom
    if (row < max_row and grid[row+1][col] == '#'):
        num_occupied += 1
    # bottom right
    if (row < max_row and col < max_col and grid[row+1][col+1] == '#'):
        num_occupied += 1
    
    #if (row,col) == (1,1):
    #    print('1,1 {} {}'.format(grid[row][col], num_occupied))
    
    if 'L' == grid[row][col] and num_occupied == 0:
        return (row,col)
        #new_row = list(grid[row])
        #new_row[col] = '#'
        #grid[row] = ''.join(new_row)
        #list(grid[row])[col] = '#'

    if '#' == grid[row][col] and num_occupied >= 4:
        #new_row = list(grid[row])
        #new_row[col] = 'L'
        #grid[row] = ''.join(new_row)
        return (row,col)

#with open('./test_input.txt') as f:
with open('./test1.txt') as f:
    grid = [l.strip() for l in f.readlines()]
    solve_problem(grid)