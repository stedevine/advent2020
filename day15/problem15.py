def init(input):
    history = {}
    turn = 1
    for i in input:
        history[i] = [turn]
        turn += 1
    
    return history, turn, input[-1]

def get_next(history, turn, number):
    if turn % 10000000 == 0 :
        print(turn)

    result = 0

    if number in history and len(history[number]) > 1:
        #print('seen number more than once')
        result = history[number][0] - history[number][1]

    if result in history:
        if len(history[result]) == 1:
            history[result].insert(0,turn)
        else:
            history[result][1] = history[result][0]
            history[result][0] = turn
        #history[result].insert(0, turn)
    else:
        history[result] = [turn]

    #print('turn {} input {} output {} history {}'.format(turn, number, result, history))
    return history, result

    
def get_nth(n):
    input = [13,0,10,12,1,5,8]

    history, turn, number = init(input)
    #print(history)
    result = input[-1]

    for turn in range(len(input) + 1,n+1):
        (history, result) = get_next(history, turn, result)

        #print('{}:{} ({})'.format(turn,number,history)

    print(result)

get_nth(2020)
get_nth(30000000)