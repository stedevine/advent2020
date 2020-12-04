# conditions is a list of functions that take a 
# passport (dictionary) and returns a boolean
def count_valid(problem_data, conditions):
    number_valid = 0
    is_valid = True 
    for passport in get_passports(problem_data):
        for condition in conditions:
            if not condition(passport):
                is_valid = False
                break
        if is_valid:
            number_valid += 1
        is_valid = True

    return number_valid  

def get_passports(problem_data):
    passports = []
    passport = {}
    for line in problem_data:
        if line is not '':
            populate_passport(passport, line)
        else:
            # line break - add the passport to the list
            passports.append(passport)
            passport = {}

    # end of file, add the last passport to the list
    passports.append(passport)

    return passports

def populate_passport(passport,line):
    fields = line.split(' ')
    for field in fields:
        passport[field.split(':')[0]] = field.split(':')[1]

def has_fields(passport):
    for field in ['byr', 'iyr', 'eyr','hgt','hcl','ecl','pid']:
        if not field in passport:
            return False
    return True

def fields_are_valid(passport):
    return check_integer(passport, 'byr', 1920, 2002) \
        and check_integer(passport, 'iyr', 2010, 2020) \
        and check_integer(passport, 'eyr', 2020, 2030) \
        and check_height(passport) \
        and check_hair(passport) \
        and check_eye(passport) \
        and check_number(passport)

def check_integer(passport, key, min, max):
    try:
        val = int(passport[key])
        return val >= min and val <= max
    
    except ValueError:
        return False

def check_height(passport):
    try:
        metric = passport['hgt'][-2:]
        height = int(passport['hgt'][:-2])
        if metric == 'in':
            return  height >= 59 and height <= 76     
        if metric == 'cm' : 
            return  height >= 150 and height <= 193 

    except ValueError:
        return False

    return False

def check_hair(passport):
    hcl = passport['hcl']

    if len(hcl) != 7:
        return False

    if hcl[0] != '#':
        return False

    hex_string = '0x' + hcl[1:]
    try:
        int(hex_string,16)
        return True
    except ValueError:
        return False   

def check_eye(passport):
    return passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_number(passport):
    pid = passport['pid']
    if (len(pid) != 9):
        return False
    try:
        int(pid)
        return True
    except ValueError:
        return False 

problem_input = []
with open('./problem4_input.txt') as f:
    problem_input = [l.strip() for l in f.readlines()]
    print('Problem 1 : {}'.format(count_valid(problem_input,[has_fields])))
    print('Problem 2 : {}'.format(count_valid(problem_input,[has_fields,fields_are_valid])))
