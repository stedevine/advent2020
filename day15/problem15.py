def init(input):
    history = {}
    turn = 1
    for i in input:
        history[i] = [turn]
        turn += 1
    
    return history, turn, input[-1]

def get_next(history, turn, number):
    if turn % 100000 == 0 :
        print(turn)

    result = 0

    if number in history and len(history[number]) > 1:
        #print('seen number more than once')
        result = history[number][0] - history[number][1]

    if result in history:
        history[result].insert(0, turn)
    else:
        history[result] = [turn]

    #print('turn {} input {} output {} history {}'.format(turn, number, result, history))
    return history, result


'''    
    result = 0
    if turn == 5:
        print('turn 5 history {}'.format(history))
    if number in history:
        if turn == 5:
            print('{} is in history'.format(number))
        history[number].insert(0,turn)
        if len(history[number]) > 2:
            result = history[number][1] - history[number][2]
            #return (history, history[number][1] - history[number][2])
    
    else:
        # First time
        history[number] = [turn]
    
    print('turn {} input {} output {}'.format(turn, number, result))
    return (history, result)
 '''   
    

#input = [13,0,10,12,1,5,8]
input = [0,3,6]
history, turn, number = init(input)
print(history)
result = input[-1]

for turn in range(len(input) + 1,30000001):
    (history, result) = get_next(history, turn, result)

    #print('{}:{} ({})'.format(turn,number,history)

print(result)