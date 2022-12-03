

def calc_prio(element):

    # prio value a..zA..Z = 1..26, 27..52
    # ord(prio) - ord('a') + 1

    prio = ord(element.lower()) - ord('a') + 1
    if element.isupper(): prio += 26

    return prio


def sum_priorities(input_filename):

    count_prio = 0

    with open(input_filename) as rucksacks:

        for rucksack in rucksacks:
            r = rucksack.strip()
            r1, r2 = r[:len(rucksack)//2], r[len(rucksack)//2:]

            prio_element = (set(r1).intersection(set(r2))).pop()

            count_prio += calc_prio(prio_element)

    return count_prio

def sum_prio_badges(input_filename):

    count_badge = 0

    with open(input_filename) as rucksacks:

        while True:
            r1 = set(rucksacks.readline().strip())
            r2 = set(rucksacks.readline().strip())
            r3 = set(rucksacks.readline().strip())

            #print(r1, r2, r3)

            if len(r1) + len(r2) + len(r3) == 0:
                break

            badge = r1.intersection(r2, r3).pop()
            count_badge += calc_prio(badge)

    return count_badge



def main():
    # Exercise 1
    sum_prio = sum_priorities('day_3_data.txt')
    print('Sum of priorities: ', sum_prio)
    #Exercise 2
    sum_badges = sum_prio_badges('day_3_data.txt')
    print('Sum priority of badges: ', sum_badges)

if __name__ == "__main__":
    main()