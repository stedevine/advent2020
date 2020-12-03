import unittest

def parse_line(policy):
    first_value = int(policy.split('-')[0])
    second_value = int(policy.split('-')[1].split(' ')[0])
    char = policy.split(' ')[1].split(':')[0]
    password = policy.split(' ')[-1]
    return(first_value, second_value, char, password)

def count_valid(problem_input):
    # Policy : Password must contain between max and min instances of specified character
    valid = 0
    for policy in problem_input:
        min, max, character, password = parse_line(policy)
        number_of_occurances = password.count(character)
        if (number_of_occurances >= min and number_of_occurances <= max):
            valid += 1
    
    return valid

def count_valid_new_policy(problem_input):
    # Policy : Password must have char at first or second index but not both       
    valid = 0
    for policy in problem_input:
        index1, index2, character, password = parse_line(policy)
        # policy is 1 based, rather than zero based
        index1 = index1 - 1
        index2 = index2 - 1
        character = policy.split(' ')[1].split(':')[0]
        password = policy.split(' ')[-1]
        
        # ^ is xor
        if (password[index1] == character) ^ (password[index2] == character):
                valid += 1
    
    return valid      

test_input = [
"1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"]
tc = unittest.TestCase()
tc.assertEqual(2, count_valid(test_input))
tc.assertEqual(1, count_valid_new_policy(test_input))

with open('./problem2_input.txt') as f:
    problem_input = f.readlines()
    print('part 1 {}'.format(count_valid(problem_input)))
    print('part 2 {}'.format(count_valid_new_policy(problem_input)))