
from math import inf
import collections


def calculate_min_dist(input_filename, start='S', end='E'):

    # Get letter map
    with open(input_filename) as hill_file:        
        hill = [[*line.strip()] for line in hill_file.readlines()]

    # Create distance map
    hill_dist = [[inf for j in range(len(hill[0]))] for i in range(len(hill))]

    # Outside of bounds
    j_max, i_max = len(hill), len(hill[0])

    # Define
    min_dist_end = inf

    end_pos = None

    # State queue
    queue = collections.deque()
    
    # Search initial state
    for j in range(len(hill)):
        if queue and end_pos is not None: 
            break
        for i in range(len(hill[0])):
            if hill[j][i] == start:
                hill[j][i] = 'a'
                hill_dist[j][i] = 0.0
                queue.extend([(j,i)])
            elif hill[j][i] == end:
                hill[j][i] = 'z'
                end_pos = (j, i)
    
    # Go through all possible states
    while queue:

        (j, i) = queue.popleft()

        curr_dist = hill_dist[j][i]
        curr_char = hill[j][i]


        if (j, i) == end_pos:
            min_dist_end = min(curr_dist, min_dist_end)
            # Dont add new states
            continue

        # Add if
        #   - feasible direction
        #   - dist_diff >= -1
        #   - new dist < curr dist

        if (j-1 >= 0 and 
                ord(curr_char)-ord(hill[j-1][i]) >= -1 and 
                curr_dist+1 < hill_dist[j-1][i]):
            hill_dist[j-1][i] = curr_dist+1
            queue.extend([(j-1,i)])
        if (j+1 < j_max and 
                ord(curr_char)-ord(hill[j+1][i]) >= -1 and  
                curr_dist+1 < hill_dist[j+1][i]):
            hill_dist[j+1][i] = curr_dist+1
            queue.extend([(j+1,i)])
        if (i-1 >= 0 and 
                ord(curr_char)-ord(hill[j][i-1]) >= -1 and  
                curr_dist+1 < hill_dist[j][i-1]):
            hill_dist[j][i-1] = curr_dist+1
            queue.extend([(j,i-1)])
        if (i+1 < i_max and 
                ord(curr_char)-ord(hill[j][i+1]) >= -1 and  
                curr_dist+1 < hill_dist[j][i+1]):
            hill_dist[j][i+1] = curr_dist+1
            queue.extend([(j,i+1)])

    return min_dist_end


def calculate_min_dist_from_any(input_filename, start='S', end='E'):

    # Get letter map
    with open(input_filename) as hill_file:        
        hill = [[*line.strip()] for line in hill_file.readlines()]

    # Create distance map
    hill_dist = [[inf for j in range(len(hill[0]))] for i in range(len(hill))]

    # Define
    j_max, i_max = len(hill), len(hill[0])
    min_dist_end = inf

    # end_pos = None

    # State queue
    queue = collections.deque()
    
    # Search initial state
    for j in range(len(hill)):
        if queue: # and end_pos is not None: 
            break
        for i in range(len(hill[0])):
            if hill[j][i] == start:
                hill[j][i] = 'a'
                #hill_dist[j][i] = 0.0
                #queue.extend([(j,i)])
            elif hill[j][i] == end:
                hill[j][i] = 'z'
                #end_pos = (j, i)
                hill_dist[j][i] = 0.0
                queue.extend([(j,i)])
    
    # Go through all possible states
    while queue:

        (j, i) = queue.popleft()

        curr_dist = hill_dist[j][i]
        curr_char = hill[j][i]


        if curr_char == 'a':
            min_dist_end = min(curr_dist, min_dist_end)
            # Dont add new states
            continue

        # Add if
        #   - feasible direction
        #   - dist_diff <= 1
        #   - new dist < curr dist

        if (j-1 >= 0 and 
                ord(curr_char)-ord(hill[j-1][i]) <= 1 and 
                curr_dist+1 < hill_dist[j-1][i]):
            hill_dist[j-1][i] = curr_dist+1
            queue.extend([(j-1,i)])
        if (j+1 < j_max and 
                ord(curr_char)-ord(hill[j+1][i]) <= 1 and  
                curr_dist+1 < hill_dist[j+1][i]):
            hill_dist[j+1][i] = curr_dist+1
            queue.extend([(j+1,i)])
        if (i-1 >= 0 and 
                ord(curr_char)-ord(hill[j][i-1]) <= 1 and  
                curr_dist+1 < hill_dist[j][i-1]):
            hill_dist[j][i-1] = curr_dist+1
            queue.extend([(j,i-1)])
        if (i+1 < i_max and 
                ord(curr_char)-ord(hill[j][i+1]) <= 1 and  
                curr_dist+1 < hill_dist[j][i+1]):
            hill_dist[j][i+1] = curr_dist+1
            queue.extend([(j,i+1)])

    return min_dist_end
        

def main():
    day = 12
    input_filename = 'day_{}_data.txt'.format(day)

    min_dist_end = calculate_min_dist(input_filename)
    print('Min distance:', min_dist_end)

    mind_dist_from_a = calculate_min_dist_from_any(input_filename)
    print('Min distance from any "a":', mind_dist_from_a)


if __name__ == "__main__":
    main()