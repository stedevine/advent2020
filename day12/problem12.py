def find_distance(instructions):
    x = 0
    y = 0 
    directions = ['E','S', 'W', 'N']
    direction_index = 0 # East

    for instruction in instructions:
        operation = instruction[0]
        number = int(instruction[1:])
        if operation == 'L' or operation == 'R':
            change = int(number / 90)
            if operation == 'L':
                change = change * -1
            direction_index = (direction_index + change) % 4
        
        if operation == 'F':
            if directions[direction_index] == 'E':
                y = y + number
            if directions[direction_index] == 'W':
                y = y - number
            if directions[direction_index] == 'N':
                x = x + number
            if directions[direction_index] == 'S':
                x = x - number
        
        if operation == 'E':
            y = y + number
        if operation == 'W':
            y = y - number
        if operation == 'N':
            x = x + number
        if operation == 'S':
            x = x - number

        #print('{} {}'.format(x,y))
    
    print(abs(x)+abs(y))


def find_new_distance(instructions):
    wx = 10
    wy = 1

    sx = 0
    sy = 0 

    for instruction in instructions:
        operation = instruction[0]
        number = int(instruction[1:])

        if operation == 'E':
            wx = wx + number
        if operation == 'W':
            wx = wx - number
        if operation == 'N':
            wy = wy + number
        if operation == 'S':
            wy = wy - number

        if operation == 'F':
            # move the ship in the direction of the waypoint
            ydelta = (wy - sy) * number
            xdelta = (wx - sx) * number
            
            sy = sy + ydelta
            sx = sx + xdelta
            
            # update the waypoint's position relative to the ship
            wy += ydelta
            wx += xdelta

        # Rotate the waypoint relative to the ship
        xdelta = (wx - sx)
        ydelta = (wy - sy)
        
        if instruction == 'R90' or instruction == 'L270':
            #print('{} {}'.format(xdelta, ydelta))
            wx = sx + ydelta         
            wy = sy - xdelta

        if instruction == 'R180' or instruction == 'L180':
            wx = sx - xdelta        
            wy = sy - ydelta

        if instruction == 'R270' or instruction == 'L90':
            #print('{} {}'.format(xdelta, ydelta))
            wx = sx - ydelta         
            wy = sy + xdelta

        #print('{} ship E {} N {} : wp E {} N {} ({} {})'.format(instruction, sx,sy, wx,wy,(wx-sx),(wy-sy)))
    
    print(abs(sx)+abs(sy))

with open('./problem12_input.txt') as f:
    instructions = [l.strip() for l in f.readlines()]
    find_distance(instructions)
    find_new_distance(instructions)
    