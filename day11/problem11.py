def solve_problem(grid):

    while(True):
        #input()
        changes = []
        result = []
        for row in (range(0,len(grid))):
            result.append([])
            grid[row] = list(grid[row])
            for col in (range(0, len(grid[row]))):
                # Add the co ordinates of all the positions that should change
                changes.append(should_change(grid,row,col))
    
        changes = list(filter(lambda c:  c != None, changes))
        if len(changes) == 0:
            # no more changes - grid is stable.
            # Find the number of unoccupied elements.
            unoccupied = 0
            for row in grid:
                unoccupied += row.count('#')
            
            print(unoccupied)
            break
        print(len(changes))
        for change in changes:
            if grid[change[0]][change[1]] == 'L':
                grid[change[0]][change[1]] = '#'
            
            else:
                grid[change[0]][change[1]] = 'L'
        
        for line in grid:
            print(''.join(line))


# updated for problem 2
def should_change(grid, row, col):
    if grid[row][col] == '.':
        return None
    
    if grid[row][col] == 'L' and get_line_of_sight(grid, row, col) == 0:
        return (row,col)
    
    # 4 for problem 1
    if grid[row][col] == '#' and get_line_of_sight(grid, row, col) >= 5:
        return (row,col)

def get_number_occupied(grid, row, col):
    #print('{},{}'.format(row,col))
    number_occupied = 0
    # top row
    if row > 0:
        # top left
        if col > 0 and grid[row-1][col-1] == '#':
                number_occupied += 1
        # above
        if grid[row-1][col] == '#':
            number_occupied  +=1
        
        # top right
        if col < len(grid[row]) -1 and grid[row-1][col+1] == '#':
            number_occupied +=1 
    
    # left
    if col > 0 and grid[row][col-1] == '#':
        number_occupied += 1
    
    # right
    if col < len(grid[row]) - 1 and grid[row][col+1] == '#':
        number_occupied += 1
    
    # bottom left
    if row < len(grid) - 1:
        # bottom right
        if col > 0 and grid[row+1][col-1] == '#':
            number_occupied += 1
        
        # below
        if grid[row+1][col] == '#':
            number_occupied += 1
        
        # bottom right
        if col < len(grid[row]) - 1 and grid[row+1][col+1] == '#':
            number_occupied += 1

    return number_occupied


def get_line_of_sight(grid, row, col):
    number_occupied = 0
    
    for direction in [(-1,-1),(-1,0),(-1,1), (0,-1),(0,1), (1,-1),(1,0),(1,1)]:   
        position = (row + direction[0], col + direction[1])
        while(position[0] >= 0 and position[0] < len(grid)  and position[1] >= 0 and position[1] < len(grid[0])):
            #print(position)
            if '#' == grid[position[0]][position[1]]:
                number_occupied += 1
                break
            if 'L' == grid[position[0]][position[1]]:
                break
            position = (position[0] + direction[0], position[1] + direction[1])    
            

    return number_occupied
    



with open('./problem11_input.txt') as f:
#with open('./test_input.txt') as f:
    grid = [l.strip() for l in f.readlines()]
    solve_problem(grid)
    #get_line_of_sight(grid,2,2)