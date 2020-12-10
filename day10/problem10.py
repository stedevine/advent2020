def get_distribution(numbers):
    numbers.insert(0,0)
    numbers.sort()
    numbers.append(numbers[-1]+3)
    d = {}
    for i in range(0, len(numbers)-1):
        print('{} {}'.format(numbers[i], numbers[i+1]))
        diff = numbers[i+1] - numbers[i]
        if diff not in d:
            d[diff] = 1
        else:
            d[diff] = d[diff] + 1
        
        #print('diff {}'.format(numbers[i+1] - numbers[i]))
    
    print(d[1])
    print(d[3])
    print(d[1] * d[3])

with open('./test_input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]
    get_distribution(numbers)
'''
with open('./problem10_input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]
    get_distribution(numbers)
'''