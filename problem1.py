import unittest
import itertools

# Find the product of the two numbers in this list which sum to 2020
def get_product(entries):
    p1 = 0
    p2 = 0
    for entry in entries:
        #candidate = 2020 - entry
        if (2020 - entry) in entries:
            p1 = entry
            p2 = (2020 - entry)

    return(p1*p2)    

# Find the product of the 3 numbers in this list which sum to 2020
def get_triple_product(entries):
    for combination in itertools.combinations(entries,3):
        if sum(combination) == 2020:
            return combination[0] * combination[1] * combination[2]

test_input = [
1721,
979,
366,
299,
675,
1456
]
tc = unittest.TestCase()
tc.assertEqual(514579, get_product(test_input))
tc.assertEqual(241861950, get_triple_product(test_input))

with open('./problem1_input.txt') as f:
    problem_data = [int(item) for item in f.readlines()]
    print(get_product(problem_data))
    print(get_triple_product(problem_data))