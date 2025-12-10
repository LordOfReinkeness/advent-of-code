import numpy as np

from challenges._2025._6.input_parse import parse_input

def main(data):
    # Your challenges for AOC 2025 day 6 part 2 goes here

    data = data.strip().split('\n')
    max_line_length = max([len(line) for line in data])\

    for idy in range(len(data)):
        while len(data[idy]) < max_line_length:
            data[idy] += ' '

    out = 0
    buff = []

    for idx in range(max_line_length - 1, -1, -1):
        math_slice = []

        for elem in range(len(data)):
            math_slice.append(data[elem][idx])

        if set(math_slice) != {' '}:
            buff.append(int(''.join(math_slice[:-1]).strip()))

            if math_slice[-1] != ' ':
                if math_slice[-1] == '+':
                    out += sum(buff)
                elif math_slice[-1] == '*':
                    n = 1
                    for elem in buff:
                        n *= elem

                    out += n

                buff = []

    return out
