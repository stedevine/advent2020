def count_outer(target, rule_dictionary, bags):
    print('Searching dictionary for {}'.format(target))

    for k,v in rule_dictionary.items():
        if target in v:
            bags.add(k)
            count_outer(k, rule_dictionary, bags)
            #print(v)
            '''
            for new_target in v:
                bags.add(new_target)
                print(bags)
                count_outer(new_target, rule_dictionary, bags)
            '''
    #print(bags)
    return bags


def build_dic(rules):
    d = {}
    for rule in rules:
        key = rule.split('bags')[0].strip()
        value = rule.split('contain')[1].strip()
        value = value.replace('bags','bag').replace(',','.').replace('bag.','token')
        value = [' '.join(x.strip().split(' ')[1:]) for x in value.split('token')][:-1]
        d[key] = value
    
    #print(d)

    # how many bags contain a shiny gold bag?
    result = count_outer('shiny gold', d, set())
    print(result,len(result))

with open('./problem7_input.txt') as f:
    rules = [line.strip() for line in f.readlines()]
    build_dic(rules)