import unittest

# Returns the value of the accumulator and whether or not the program is valid
# (valid programs are not infinite loops)
def run_code(instructions):
    
    accumulator = 0 
    offset = 0
    # keep track of all the offsets we have visited
    visited = set()

    while(True):
        operation = instructions[offset].split(' ')[0]
        argument = int(instructions[offset].split(' ')[1])
        # Process operations
        if operation == 'nop':
            offset += 1
        
        if operation == 'acc':
            accumulator += argument
            offset += 1
        
        if operation == 'jmp':
            offset += argument
        
        if offset == len(instructions):
            #print('program completed {} {}'.format(offset, accumulator))
            return (True, accumulator)

        if offset in visited:
            #print('loop! {} {}'.format(offset, accumulator))
            return (False, accumulator)
        
        visited.add(offset)


def update_code(instructions):
    # Problem 2 - if we change one of the jmp instructions to a nop 
    # the program completes succesfully. We don't know which one, so
    # try each of them until the program completes.
   
    # get the index of each jmp operation
    operations = [ instruction.split(' ')[0] for instruction in instructions ]
    jmps = [i for i in range(len(operations)) if operations[i] == 'jmp']

    for jmp_index in jmps:
        code = instructions.copy()
        # change the jmp to a nop
        code[jmp_index] = code[jmp_index].replace('jmp','nop')
        result = run_code(code)
        # If the code completed succesfully, return the result.
        if (result[0]):
            return result[1] 

tc = unittest.TestCase()
with open('./test_input.txt') as f:
    instructions = [l.strip() for l in f.readlines()]
    tc.assertEqual(5, run_code(instructions)[1])
    tc.assertEqual(8, update_code(instructions))

with open('./problem8_input.txt') as f:
    instructions = [l.strip() for l in f.readlines()] 
    print('Problem 1 : {}'.format(run_code(instructions)[1]))
    print('Problem 2 : {}'.format(update_code(instructions)))
