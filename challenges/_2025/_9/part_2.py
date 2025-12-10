import numpy as np
from functools import reduce

from challenges._2025._9.input_parse import parse_input

def print_map(floor_map):
    for line in floor_map:
        print(''.join(line))
    print()

def fill(point, floor_map):
    neighbours = np.array([
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1]
    ])

    to_fill = [point]

    while len(to_fill) > 0:
        point = to_fill.pop(0)

        if floor_map[point[1]][point[0]] == 'x':
            continue

        floor_map[point[1]][point[0]] = 'x'

        for neighbour in neighbours:
            next_pos = point + neighbour
            if floor_map[next_pos[1]][next_pos[0]] != 'x':
                to_fill.append(next_pos)


def main(data):
    data = parse_input(data)
    # Your challenge for AOC 2025 day 9 part 2 goes here


    print('Initiating floor map')
    dimensions = [max(line) + 2 for line in np.transpose(data)]
    print(f'\tdimensions are {dimensions[0]}:{dimensions[1]}')
    floor_map = np.full((dimensions[1], dimensions[0]), '.')

    print('Writing outline')
    position = data[0].copy()
    for idx in range(len(data)):
        idx = (idx + 1) % len(data)
        step_vector = ((data[idx] - position) / np.linalg.norm(data[idx] - position)).astype(int)

        while not np.array_equal(position, data[idx]):
            floor_map[position[1]][position[0]] = 'x'
            position += step_vector

    print('Filling shape')
    start = []
    for idy, line in enumerate(floor_map):
        for idx, elem in enumerate(line):
            if elem == 'x':
                start = np.array([idx + 1, idy + 1])
                break
        else:
            continue
        break

    fill(start, floor_map)

    print('Finding Area')
    out = 0
    for idy, y_elem in enumerate(data):
        for idx, x_elem in enumerate(data):
            if idx > idy:
                upper_left = [int(min(y_elem[0], x_elem[0])), int(min(y_elem[1], x_elem[1]))]
                lower_right = [int(max(y_elem[0], x_elem[0])), int(max(y_elem[1], x_elem[1]))]
                snippet = floor_map[upper_left[1]:lower_right[1]+1, upper_left[0]:lower_right[0]+1].tolist()

                if len(list(set(reduce(lambda a, b: a + b, list([list(set(line)) for line in snippet]))))) == 1:
                    out = max(sum([len(line) for line in snippet]), out)

    return out
