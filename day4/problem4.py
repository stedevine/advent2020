def count_valid(problem_data):
    passport = {}
    valid = 0 

    for line in problem_data:
        if line is not '':
            populate_passport(passport, line)
        else: 
            if is_valid(passport):
                valid += 1
            passport = {}

    if is_valid(passport):
        valid += 1
    
    print(valid)

def populate_passport(passport,line):
    fields = line.split(' ')
    for field in fields:
        passport[field.split(':')[0]] = field.split(':')[1]

def is_valid(passport):
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
        #print(check_integer(passport, 'byr', 1920, 2002))
        return check_integer(passport, 'byr', 1920, 2002) \
            and check_integer(passport, 'iyr', 2010, 2020) \
            and check_integer(passport, 'eyr', 2020, 2030) \
            and check_height(passport) \
            and check_hair(passport) \
            and check_eye(passport) \
            and check_number(passport)

def check_integer(passport, key, min, max):
    try:
        v = int(passport[key])
        return v >= min and v <= max
    
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
    count_valid(problem_input)