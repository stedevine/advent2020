# Problem 1
def build_simple_dictionary(rules):
    d = {}
    for rule in rules:
        key = rule.split('bags')[0].strip()
        value = rule.split('contain')[1].strip()
        value = value.replace('bags','bag').replace(',','.').replace('bag.','token')
        value = [' '.join(x.strip().split(' ')[1:]) for x in value.split('token')][:-1]
        d[key] = value
    return d

# Create a set of the bags in which the target lives, return the count
def count_outer_bags(target, rule_dictionary, bags):
    for k,v in rule_dictionary.items():
        if target in v:
            bags.add(k)
            count_outer_bags(k, rule_dictionary, bags)
    
    return len(bags)

# Problem 2
def count_inner_bags(target, rule_dictionary, count):
    for k,v in rule_dictionary.items():
        if target == k:
            for inner_bag in v:
                # base case - the bag that contains no other bags
                if inner_bag == 'no other':
                    # just count this bag
                    return 1

                # this bag contains n bags, so recursively search for those bags and multuply the result by n
                multiplier = int(inner_bag.split(' ')[0])
                # remove the leading n so we have the key
                new_target = ' '.join(inner_bag.split(' ')[1:])

                count = count + multiplier * count_inner_bags(new_target, rule_dictionary, 1)

    return count 

def build_detailed_dictionary(rules):
    d = {}
    for rule in rules:
        # key is simple
        key = rule.split('bags')[0].strip()
        
        # turn rules into: n bag type
        value = rule.split('contain')[1].strip()
        value = value.replace('bags','bag').replace(',','.').replace('bag.','token')
        value = [' '.join(x.strip().split(' ')) for x in value.split('token')][:-1]
        
        d[key] = value
    
    return d

import unittest
tc = unittest.TestCase()

with open('./test_input.txt') as f:
    rules = [l.strip() for l in f.readlines()] 
    tc.assertEqual(4, count_outer_bags('shiny gold', build_simple_dictionary(rules), set()))
    tc.assertEqual(32, count_inner_bags('shiny gold', build_detailed_dictionary(rules), 0))

with open('./test_input2.txt') as f:
    rules = [l.strip() for l in f.readlines()] 
    tc.assertEqual(126, count_inner_bags('shiny gold', build_detailed_dictionary(rules), 0))


with open('./problem7_input.txt') as f:
    rules = [line.strip() for line in f.readlines()]
    print('problem 1 : {}'.format(count_outer_bags('shiny gold', build_simple_dictionary(rules), set())))
    print('problem 2 : {}'.format(count_inner_bags('shiny gold', build_detailed_dictionary(rules), 0)))

