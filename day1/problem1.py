import unittest
import itertools

# For a list of numbers find the combination (of size number_of_values_to_combine) 
# that sums to the target value.
# return the product of the values in this combination.
def get_product(entries, number_of_values_to_combine, target_value):
    for combination in itertools.combinations(entries, number_of_values_to_combine):
        if sum(combination) == target_value:
            result = 1
            for c in combination:
                result *= c
            return result


test_input = [
1721,
979,
366,
299,
675,
1456
]
tc = unittest.TestCase()
tc.assertEqual(514579, get_product(test_input,2,2020))
tc.assertEqual(241861950, get_product(test_input,3,2020))

with open('./problem1_input.txt') as f:
    problem_data = [int(item) for item in f.readlines()]
    print('Problem 1 : {}'.format(get_product(problem_data, 2, 2020)))
    print('Problem 2 : {}'.format(get_product(problem_data, 3, 2020)))
