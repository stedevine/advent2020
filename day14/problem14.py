import math
def apply_mask_to_value(value, mask):
    # mask is zeros, ones and Xs
    # zero sets the matching bit to 0 
    # one sets the matching bit to 1
    # X does nothing

    # extract the ones from the mask. OR this with the value to set all the masked values to 1
    mask_1 = int(mask.replace('X','0'),2)
    # extract the zeros (actually turn them to 1s ) AND this with the input value and substract it 
    # it from the OR'd value to get the total
    mask_0 = int(mask.replace('1','X').replace('0','1').replace('X','0'),2)
    return (value | mask_1) - (value & mask_0)

def run_program_problem_1(lines):
    mask = 0
    memory = {}
    for line in lines:
        #print('{} {} {}'.format(line,mask,memory))
        tokens = line.split(' = ')
        operator = tokens[0]
        value = tokens[1]
        if operator == 'mask':
            mask = value
        else:
            # is memory operation
            offset = operator[3:]
            memory[offset] = apply_mask_to_value(int(value),mask)
    
    print(sum(memory.values()))

def get_memory_addresses(mask, memory_address):
    # a 1 in the mask means the corresponding bit in the memory address is overwritten with a 1
    memory_address = memory_address | int(mask.replace('X','0'),2)
    mem_binary = format(memory_address,'036b')

    merged_mem = ''
    for i,j in zip(mem_binary,mask):
        merged_mem += (j if j == 'X' else i)

    # Xs in the mask are 'floating', each X can be 1 or 0
    # return all possible combinations
    
    # There are 2 ^ (number of xs) combinations 
    # For x = 4:  0000, 0001, 0010, 0011 etc.
    # for each value in 0 -> 2 ^ (number of xs) create a string and 
    # replace the Xs in the mask with the values in the string:
    # mask = 0X1X0, value = 01 -> 00110 
    
    addresses = []
    xs = merged_mem.count('X')
    address_template = merged_mem.replace('X','{}')
    for i in range(0, int(math.pow(2,xs))):
        # value in binary with leading zeros.
        value_string = format(i, '0{}b'.format(xs))
        addresses.append(address_template.format(*format(i,'0{}b'.format(xs))))

    dec_addresses = [int(i,2) for i in addresses]
    return dec_addresses




def run_program_problem_2(lines):
    mask = 0
    memory = {}
    for line in lines:
        #print('{} {} {}'.format(line,mask,memory))
        tokens = line.split(' = ')
        operator = tokens[0]
        value = tokens[1]
        if operator == 'mask':
            mask = value
        else:
            # is memory operation
            memory_address = int(operator[3:][1:-1])
            for address in get_memory_addresses(mask, memory_address):
                memory[address] = int(value)
            #memory[offset] = apply_mask_to_value(int(value),mask)
    
    #pass
    #print(memory)
    print(sum(memory.values()))

with open('./problem14_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    run_program_problem_1(lines)
    run_program_problem_2(lines)

    #print(lines)