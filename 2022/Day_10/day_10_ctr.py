import collections




def get_signal_strength(cycle, register_value):
    return cycle * register_value


def get_sum_signal_strength(input_filename, cycles):

    x = 1
    c = 0
    cycles = collections.deque(cycles)
    ss = 0

    with open(input_filename, 'r') as instructions:
        for instruction in instructions:
            instruction = instruction.strip()

            # Either instruction
            c+=1            

            # Check
            if len(cycles) == 0:
                break
            elif cycles[0] == c:
                ss += get_signal_strength(cycles.popleft(), x)

            # Add instruction
            if instruction.startswith('addx'):
                op, value = instruction.split()
                c += 1

                # Check mid-add op
                if len(cycles) == 0:
                    break
                elif cycles[0] == c:
                    ss += get_signal_strength(cycles.popleft(), x)

                x += int(value)

    return ss

def get_crt_image(input_filename):
    
    x = 1
    c = 0

    crt_image = ""
    
    with open(input_filename, 'r') as instructions:
        for instruction in instructions:
            instruction = instruction.strip()
                        
            if c % 40 == 0:
                crt_image += '\n'

            # Either instruction
            c+=1            

            # Check
            if c % 40 in [x, x+1, x+2]:
                crt_image += '#'
            else:
                crt_image += '.'

            # Add instruction
            if instruction.startswith('addx'):
                op, value = instruction.split()
                
                if c % 40 == 0: 
                    crt_image += '\n'
                c += 1

                # Check mid-add op
                if c % 40 in [x, x+1, x+2]:
                    crt_image += '#'
                else:
                    crt_image += '.'

                x += int(value)

    return crt_image

def main():
    cycles = [20, 60, 100, 140, 180, 220]
    signal_strength = get_sum_signal_strength('day_10_data.txt', cycles)
    print('Signal strength:', signal_strength)
    crt_image = get_crt_image('day_10_data.txt')
    print('CRT image:', crt_image)


if __name__ == "__main__":
    main()