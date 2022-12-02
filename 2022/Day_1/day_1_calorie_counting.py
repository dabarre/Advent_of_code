

def count_max_calories(input_filename):
    max_calories = 0
    current_calories = 0

    with open(input_filename) as calories_file:
        for cal in calories_file.readlines():

            if cal.strip() == '':
                max_calories = max(max_calories, current_calories)
                current_calories = 0
                continue
            
            current_calories += int(cal)

    return max_calories

def sum_top_3_calories(input_filename, top_n=3):
    
    max_elves = [0] * (top_n+1)
    current_calories = 0

    with open(input_filename) as calories_file:
        for cal in calories_file.readlines():
            if cal.strip() == '':
                max_elves.sort()
                max_elves[0] = current_calories
                current_calories = 0
                continue
            
            current_calories += int(cal)

    
    return sum(max_elves[1:])


def main():
    filename = 'day_1_data.txt'

    # Exercise 1
    max_calories = count_max_calories(filename)
    print('Max calories carried by an elf: ', max_calories)

    # Exercise 2
    sum_top_3 = sum_top_3_calories(filename)
    print('Sum of the top 3 calories carried by the elves is:', sum_top_3)


if __name__ == "__main__":
    main()

