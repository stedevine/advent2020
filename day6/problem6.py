import string
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

    #print(sum([sum(len(l)) for l in forms]))

    return forms

def get_all_yes(problem_data):
    # count all the letters (az) that are present in every line

    forms = []
    form_lines = []
    for line in problem_data:
        if line is not '':
            form_lines.append(line)
        else:
            print('form {}'.format(form_lines))
            forms.append(form_lines)
            form_lines = []

    forms.append(form_lines)
    #print('form {}'.format(form_lines))
    form_count = 0 
    for f in forms:
        print('form {} #people {}'.format(f, len(f)))
        #print(''.join(f))
        letters = set(''.join(f))
        
        for l in letters:
            if (''.join(f).count(l) == len(f)):
                form_count += 1
    print('{}'.format(form_count)) 
        # for all yes to answer there should be len(f) instances of each answer
         




with open('./test_input.txt') as f:
    problem_input = [l.strip() for l in f.readlines()]    
    print(get_answers(problem_input))
    get_all_yes(problem_input)

with open('./problem6_input.txt') as f:
    problem_input = [l.strip() for l in f.readlines()]    
    print(get_answers(problem_input))
    get_all_yes(problem_input)