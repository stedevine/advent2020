#tc = unittest.TestCase()
def check_numbers(window_size, numbers):

    for i in range(0, len(numbers) - (window_size + 1)):
        # Check that the target number can be made by a pair of numbers in the window
        target = numbers[i+window_size+1]
        window = numbers[i:i+window_size+1]
        print("Checking {} in {}".format(target, window))
        valid = False
        for w in window:
            remaining = set(window)
            remaining.remove(w)
            if (target - w)  in remaining:
                valid = True
                break
        if not valid:
            print('invalid value {}'.format(target))
            return target


def get_windows(numbers):
    for w in range(1, len(numbers)+1):
        for i in range(len(numbers)-w+1):
            yield numbers[i:i+w]

def get_encryption_weakness(target,numbers):
    for window in get_windows(numbers):
        if sum(window) == target:
            print(window)
            window.sort()
            print(window)



with open('./test_input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

    window_size = 5
    print(check_numbers(window_size, numbers))
    print(get_encryption_weakness(127, numbers))


with open('./problem9_input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

    window_size = 25
    print(check_numbers(window_size, numbers))
    print(get_encryption_weakness(15353384, numbers))
    