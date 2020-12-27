def get_limits(lines):
    ranges = []
    for line in lines:
        if line == '':
            return ranges
        
        line_limits = line.split(': ')[1]
        for r in line_limits.split('or'):
            ranges.append(r.strip())

def get_set(ranges):

    s = set()
    for r in ranges:
        i = int(r.split('-')[0])
        j = int(r.split('-')[1]) + 1
        s.update(*[range(i,j)])
    
    return s


def get_slots(lines):
    slots = {}
    for line in lines:
        if line == '':
            print(slots)
            return slots
        
        key = line.split(': ')[0]
        
        slots[key] = []
        line_limits = line.split(': ')[1]
        for r in line_limits.split('or'):
            slots[key].append(r.strip())
        slots[key] = get_set(slots[key])

def get_tickets(lines):
    tickets = []
    ignore = True
    for line in lines:
        if ignore == False:
            tickets.append(line)
        if line == 'nearby tickets:':
            ignore = False

    return tickets
        
        
def get_errors(tickets,s):
    error_rate = 0
    for ticket in tickets:
        for field in [int(f) for f in ticket.split(',')]:
            if field not in s:
                error_rate += field
    
    return error_rate



            


with open('./test_input.txt') as f:
    #with open('./problem16_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    
    get_slots(lines)
    #print(lines)
    #tickets = get_tickets(lines)
    #print(tickets)
    #s = get_set(get_limits(lines))
    #print(s)
    #print(process_tickets(tickets, s))
    #print(get_errors(tickets,s))
