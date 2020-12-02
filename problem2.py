def count_valid(problem_input):
    valid = 0
    for policy in problem_input:
        min = int(policy.split('-')[0])
        max = int(policy.split('-')[1].split(' ')[0])
        char = policy.split(' ')[1].split(':')[0]
        password = policy.split(' ')[-1]
        print('{} {} {} {}'.format(min, max,char,password))
        number_of_occurances = password.count(char)
        if (number_of_occurances >= min and number_of_occurances <= max):
            valid += 1
    
    return valid

def count_valid_new_policy(problem_input):       
    valid = 0
    for policy in problem_input:
        index1 = int(policy.split('-')[0]) - 1
        index2 = int(policy.split('-')[1].split(' ')[0]) -1
        char = policy.split(' ')[1].split(':')[0]
        password = policy.split(' ')[-1]
        print('{} {} {} {}'.format(min, max,char,password))
        if (password[index1] == char) ^ (password[index2] == char):
                print(policy)
                valid += 1
    
    return valid      

problem_input = [
"1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"]

with open('./problem2_input.txt') as f:
    problem = f.readlines()
    #print('answer {}'.format(count_valid(problem)))
    print('answer {}'.format(count_valid_new_policy(problem)))

print('answer {}'.format(count_valid_new_policy(problem_input)))