from challenges._2025._4.input_parse import parse_input
from utils import print_2d_matrix

def remove_rolls(layout):
    removed = 0
    to_remove = []

    for idy, line in enumerate(layout):
        for idx, elem in enumerate(line):

            # for every element in the input array
            if elem == '@':
                submatrix = layout[max(0, idy - 1):min(len(line), idy + 2), max(0, idx - 1):min(len(line), idx + 2)]
                number_at = sum(list(x).count('@') for x in submatrix) - 1
                if number_at < 4:
                    removed += 1
                    to_remove.append([idy, idx])


    if removed > 0:
        for elem in to_remove:
            layout[elem[0]][elem[1]] = '.'

    return removed, layout

def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 4 part 2 goes here
    out = 0

    while True:
        print_2d_matrix(data)
        print('\n------------\n')
        removed, data = remove_rolls(data)

        if removed == 0:
            break

        out += removed

    return out
