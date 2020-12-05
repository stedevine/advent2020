def get_number(code):
    row = int(code.replace('F','0').replace('B','1')[:7],2)
    col = int(code.replace('R','1').replace('L','0')[-3:],2)
    #print('row {} col {}'.format(row,col))
    
    return (row * 8 + col, code)

print(get_number('FFFBBBFRRR'))

with open('./problem5_input.txt') as f:
    results = [get_number(l.strip()) for l in f.readlines()]
    results.sort()
    print(results)
    l = 69
    for r in results:
        if (r[0] - 1 != l):
            print('seat {}'.format(r[0] - 1))
        l = r[0]
 