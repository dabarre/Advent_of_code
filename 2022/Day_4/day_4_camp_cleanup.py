

def check_contains(a, b):
    return ((a[0] <= b[0] and a[1] >= b[1]) or 
                (b[0] <= a[0] and b[1] >= a[1]))

def check_overlap(a, b):
    return ((a[0] <= b[0] and a[1] >= b[0]) or 
                (b[0] <= a[0] and b[1] >= a[0]))



def count_fully_contained_assignments(input_filename):

    count_fca = 0
    count_oa = 0

    with open(input_filename) as assignments:

        for assignment in assignments:
            
            a, b = assignment.strip().split(',')
            a = [int(num) for num in a.split('-')]
            b = [int(num) for num in b.split('-')]

            if check_contains(a,b):
                count_fca += 1               

            if check_overlap(a,b):
                count_oa += 1

    return count_fca, count_oa

def main():

    count_fca, count_oa = count_fully_contained_assignments('day_4_data.txt')
    
    # Exercise 1
    print('Sum of fully contained assignments: ', count_fca)
    #Exercise 2
    print('Sum overlapping assignments: ', count_oa)

if __name__ == "__main__":
    main()