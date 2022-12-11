
import math

head_n_knot = []
tail_visited = set()


def init(n_knots):
    head_n_knot.clear()
    for i in range(n_knots):
        head_n_knot.append([0.0, 0.0])

    tail_visited.clear()

def move_head(direction):
    if direction == "U":
        head_n_knot[0][1] += 1
    elif direction == "D":
        head_n_knot[0][1] -= 1
    elif direction == "L":
        head_n_knot[0][0] -= 1
    elif direction == "R":
        head_n_knot[0][0] += 1

    tail_follow()


def tail_follow():
    for i in range(1, len(head_n_knot)):
        x_diff = head_n_knot[i-1][0] - head_n_knot[i][0]
        y_diff = head_n_knot[i-1][1] - head_n_knot[i][1]

        if abs(x_diff) > 1 or abs(y_diff) > 1:
            head_n_knot[i][0] += math.copysign(1, x_diff) if abs(x_diff) > 1 else x_diff
            head_n_knot[i][1] += math.copysign(1, y_diff) if abs(y_diff) > 1 else y_diff


def add_tail_pos():
    tail_visited.add(tuple(head_n_knot[-1]))


def execute_moves(input_filename, n_knots):

    init(n_knots)

    with open(input_filename, 'r') as movements:
        for move in movements:
            direction, m_moves  = move.strip().split()

            for i in range(int(m_moves)):
                move_head(direction)
                add_tail_pos()   

    return


def main():
    execute_moves('day_9_data.txt', 2)
    print('Num visited by tail (2 knots):', len(tail_visited))

    execute_moves('day_9_data.txt', 10)
    print('Num visited by tail (10 knots):', len(tail_visited))


if __name__ == "__main__":
    main()