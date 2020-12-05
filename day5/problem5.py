import unittest

def get_seat_number(code):
    row = int(code.replace('F','0').replace('B','1')[:7],2)
    col = int(code.replace('R','1').replace('L','0')[-3:],2)    
    return (row * 8 + col)


tc = unittest.TestCase()

tc.assertEqual(567, get_seat_number('BFFFBBFRRR'))
tc.assertEqual(119, get_seat_number('FFFBBBFRRR'))
tc.assertEqual(820, get_seat_number('BBFFBBFRLL'))

with open('./problem5_input.txt') as f:
    seat_numbers = [get_seat_number(l.strip()) for l in f.readlines()]
    seat_numbers.sort()
    # Problem 1 : highest seat number
    print('Problem 1 : {}'.format(seat_numbers[-1]))
    # Problem 2 : your seat is a missing number in this list, it is not at the start or the end.
    all_seats = (list(range(seat_numbers[0], seat_numbers[-1])))
    print('Problem 2 : {}'.format(list(set(all_seats) - set(seat_numbers))[0]))
