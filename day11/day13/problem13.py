def get_earliest_time(data):
    min_time = int(data[0])

    buses = data[1].split(',')
    valid_buses = []
    for b in buses:
        if b != 'x':
            valid_buses.append(int(b))
    
    print(min_time)
    print(valid_buses)

    depart_time = min_time
    while(True):
        for valid in valid_buses:
            if depart_time % valid == 0:
                print('{} {} {}'.format(depart_time - min_time, valid, (depart_time - min_time) * valid))
                return
        depart_time += 1 

def get_crazy_time(data):
    
    leave_time = 0
    bus_data = zip(data.split(','), range(0,len(data)))
    bus_data = filter(lambda item: item[0] != 'x', bus_data)
    bus_data = [(int(x), y) for (x,y) in bus_data]
    print(bus_data)

    cadidate_time = 1
    while(True):
        is_match = True
        if cadidate_time % 1000000 == 0:
            print('testing {}'.format(cadidate_time))
        for  bus_datum in bus_data:
            result =  (cadidate_time + bus_datum[1]) % bus_datum[0]
            if result != 0:
                #print('not match {}'.format(cadidate_time))
                is_match = False
                break

        if is_match:
            print('Time {}'.format(cadidate_time))
            break
        
        cadidate_time += 1
    '''
    #cadidate_time = 1068779
        is_match = True
        for bus_datum in bus_data:     
            
            result = bus_datum[0] % (cadidate_time + bus_datum[1])
            print('time {} bus {} offset {} test_time {} result {}'.format(cadidate_time, bus_datum[0], bus_datum[1], cadidate_time+bus_datum[1], result))


            #print('time {} testing {} offset {} {} % {} = {}'.format(cadidate_time, bus_datum[0], bus_datum[1], bus_datum[0], cadidate_time + bus_datum[1], result))
            if result != 0:
                print('not match {}'.format(cadidate_time))
                is_match = False
                break
        
        if is_match:
            print('Time {}'.format(cadidate_time))
    '''

    '''
    test_leave_time = leave_time
    for bus in data.split(','):
        if (bus != 'x'):
            if (test_leave_time % bus == 0):
                test_leave_time += 1
            
       # print(bus)

    '''

test_input = [
'939',
'67','x','7','59','61']

#get_earliest_time(test_input)

problem_input = [
'1008169',
'29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,653,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19']

#get_earliest_time(problem_input)

get_crazy_time(test_input[1])
