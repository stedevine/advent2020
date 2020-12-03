import unittest

# Dots are free spaces, hashes are trees
# count all the trees that are encountered on the path
# the columns in the input field are repeated.
def count_trees_path(field, col_slope, row_slope):
    trees = 0
    col = 0 
    row = 0
    max_col = len(field[0])
    while row < len(field):
        if field[row][col] == '#':
            trees = trees + 1
        col = (col + col_slope) % max_col
        row = row + row_slope
    
    return trees

def count_product_of_trees_on_paths(field, paths):
    # Using the same logic, count the trees encountered
    # on different paths
    # return the product of these paths
    result = 1
    for (col_slope, row_slope) in paths:
        result *= count_trees_path(field, col_slope, row_slope)

    return result

test_input = [
'..##.......',
'#...#...#..',
'.#....#..#.',
'..#.#...#.#',
'.#...##..#.',
'..#.##.....',
'.#.#.#....#',
'.#........#',
'#.##...#...',
'#...##....#',
'.#..#...#.#',
]
path = [(3,1)]

tc = unittest.TestCase()

# Problem 1 - single path
tc.assertEqual(7, count_product_of_trees_on_paths(test_input, path))

problem_input = []
with open('./problem3_input.txt') as f:
    problem_input = [l.strip() for l in f.readlines()]

print('Problem 1 : {}'.format(count_product_of_trees_on_paths(problem_input, path)))

# Problem 2 - multiple paths
paths = [(1,1),(3,1),(5,1),(7,1),(1,2)]
tc.assertEqual(336, count_product_of_trees_on_paths(test_input, paths))
print('Problem 2 : {}'.format(count_product_of_trees_on_paths(problem_input, paths)))