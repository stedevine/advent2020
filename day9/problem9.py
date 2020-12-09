import unittest

# For the window size n. The previous n numbers must contain 
# a pair of numbers that add up to the target.
def find_invalid_value(window_size, numbers):

    # Create the window starting at 0
    for i in range(0, len(numbers) - (window_size + 1)):
        
        # Check that the target number can be made by a pair of numbers in the window
        target = numbers[i + window_size + 1]
        window = numbers[i: i + window_size + 1]
        
        # For each value in the window check if any *other* value sums with it to produce the target
        valid = False
        for value in window:
            remaining = set(window)
            remaining.remove(value)
            if (target - value)  in remaining:
                # found it, stop searching
                valid = True
                break
        
        # Found the invalid value
        if not valid:
            return target


# Get all the contigious windows of at least size 2
def get_windows(numbers):
    for w in range(1, len(numbers)+1):
        for i in range(len(numbers)-w):
            yield numbers[i:i+w+1]

# There is a contigious set of numbers that add up to the target
# return the sum of the largest and smallest in this list
def get_encryption_weakness(target, numbers):    
    for window in get_windows(numbers):
        if sum(window) == target:
            window.sort()
            return (window[0] + window[-1])

tc = unittest.TestCase()
with open('./test_input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

    window_size = 5
    tc.assertEqual(127, find_invalid_value(window_size, numbers))
    tc.assertEqual(62, get_encryption_weakness(127, numbers))
    
with open('./problem9_input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

    window_size = 25
    invalid_value = find_invalid_value(window_size, numbers)
    print('Problem 1 : {}'.format(invalid_value))
    print('Problem 2 : {}'.format(get_encryption_weakness(invalid_value, numbers)))
