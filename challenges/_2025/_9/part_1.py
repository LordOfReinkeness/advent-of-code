import math

import numpy as np

from challenges._2025._9.input_parse import parse_input

def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 9 part 1 goes here

    areas = []

    for idy, y_elem in enumerate(data):
        for idx, x_elem in enumerate(data):
            if idx > idy:
                sides_vector = (y_elem - x_elem) + np.array([1, 1])
                area = math.prod(sides_vector)
                areas.append(abs(area))

    return max(areas)
