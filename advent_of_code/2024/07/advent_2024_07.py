from collections import deque

def solve_layer(target, values: deque, cur_number = 0):
    n1 = values.popleft()

    add = n1 + cur_number
    multi = n1 * cur_number

    if add == target:
        return True
    elif multi == target:
        return True
    else:
        if values:
            return any([solve_layer(target, values.copy(), cur_number=operation) for operation in [add, multi]])
    return False

def solve_puzzle(puzzle_input:str) -> int:
    total = 0

    lines = puzzle_input.splitlines()
    for line in lines:
        if line:
            target_number, values = line.strip().split(':')
            target_number = int(target_number)
            values = deque([int(value) for value in values.split()])
            if solve_layer(target=target_number, values=values):
                total += target_number
    
    return total