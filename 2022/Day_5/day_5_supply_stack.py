
import copy

'''
Starting stack configuration

    [H]         [H]         [V]    
    [V]         [V] [J]     [F] [F]
    [S] [L]     [M] [B]     [L] [J]
    [C] [N] [B] [W] [D]     [D] [M]
[G] [L] [M] [S] [S] [C]     [T] [V]
[P] [B] [B] [P] [Q] [S] [L] [H] [B]
[N] [J] [D] [V] [C] [Q] [Q] [M] [P]
[R] [T] [T] [R] [G] [W] [F] [W] [L]
 1   2   3   4   5   6   7   8   9 
'''

STACKS = {
    1: ['R','N','P','G'],
    2: ['T','J','B','L','C','S','V','H'],
    3: ['T','D','B','M','N','L'],
    4: ['R','V','P','S','B'],
    5: ['G','C','Q','S','W','M','V','H'],
    6: ['W','Q','S','C','D','B','J'],
    7: ['F','Q','L',],
    8: ['W','M','H','T','D','L','F','V'],
    9: ['L','P','B','V','M','J','F'],
}

def move_and_get_top_stacks(input_filename):

    stacks_1 = copy.deepcopy(STACKS)
    stacks_2 = copy.deepcopy(STACKS)

    with open(input_filename) as operations:
        
        for op in operations:
            amount, init, end = [int(s) for s in op.split() if s.isdigit()]

            # Pop and stack n elements
            for i in range(amount): 
                stacks_1[end].append(stacks_1[init].pop())
            
            # Move last n elements
            cargo = stacks_2[init][-amount:]
            stacks_2[init] = stacks_2[init][:-amount]
            stacks_2[end].extend(cargo)

    stacking = ''.join([stack[-1] for stack in stacks_1.values()])
    appending = ''.join([stack[-1] for stack in stacks_2.values()])
    
    return stacking, appending

def main():
    stack_top, append_top = move_and_get_top_stacks('day_5_data.txt')
    # Exercise 1
    print('Top of stacks ex1: ', stack_top) # HBTMTBSDC
    # Exercise 2
    print('Top of stacks ex2: ', append_top)


if __name__ == '__main__':
    main()