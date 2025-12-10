import copy
from utils import animate_frames

from challenges._2025._7.input_parse import parse_input

def main(data):
    data = parse_input(data)

    out = 0
    store = [copy.deepcopy(data)]

    for idy, line in enumerate(data[:-1]):

        for idx, elem in enumerate(line):
            if elem == 'S':
                data[idy+1][idx] = '|'
                break
            elif elem == '^' and data[idy-1][idx] == '|':
                data[idy + 1][idx - 1] = '|'
                data[idy + 1][idx + 1] = '|'

                out += 1
            elif elem == '|' and data[idy + 1][idx] != '^':
                data[idy + 1][idx] = '|'

        store.append(copy.deepcopy(data))

    animate = True
    if animate:
        animate_frames(store)

    return out
