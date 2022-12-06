

def get_start_of_unique_seq(input_filename, char_n=4):
    # Return position where the four previous characters
    # were all different.
    
    # Lowest possible starting point
    # Assume there is always going to be a marker

    pos = -1

    with open(input_filename) as signal:
        buffer = signal.readline()

        for i in range(char_n, len(buffer)):
            marker = set(buffer[i-char_n:i])
            
            if len(marker) == char_n:
                print(buffer[i-char_n:i])
                print(marker)
                pos = i
                break
    
    return pos


def main():
    # Exercise 1
    pos_marker = get_start_of_unique_seq('day_6_data.txt')
    print('Packet marker\'s position: ', pos_marker)
    # Exercise 2
    pos_msg = get_start_of_unique_seq('day_6_data.txt', char_n=14)
    print('Msg starting position: ', pos_msg)


if __name__ == "__main__":
    main()