import unittest
def get_answers(problem_data):
    forms = []
    form = ''
    for line in problem_data:
        if line is not '':
            form += line
            form  = ''.join(set(form))
        else:
            # line break - add the form to the list
            forms.append(form)
            form = ''

    forms.append(form)
    return sum(([len(i) for i in forms]))

def get_all_yes(problem_data):
    
    forms = []
    form_lines = []
    
    for line in problem_data:
        if line is not '':
            form_lines.append(line)
        else:
            forms.append(form_lines)
            form_lines = []

    forms.append(form_lines)
    
    all_yes_count = 0 
    for form in forms:
        # get the unique set of letters in the form
        letters = set(''.join(form))
        
        # put all the letters in the form into a string and, for each unique letter 
        # count the numer of instances in the string,
        # if all the users answered 'yes' there will be a #ofusers(len of form) answers in each form
        for l in letters:
            if (''.join(form).count(l) == len(form)):
                all_yes_count += 1

    return all_yes_count

tc = unittest.TestCase()
with open('./test_input.txt') as f:
    test_input = [l.strip() for l in f.readlines()] 

    tc.assertEqual(11, get_answers(test_input))
    tc.assertEqual(6, get_all_yes(test_input))

with open('./problem6_input.txt') as f:
    problem_input = [l.strip() for l in f.readlines()]    
    print('Problem 1 : {}'.format(get_answers(problem_input)))
    print('Problem 2 : {}'.format(get_all_yes(problem_input)))