from challenges._2025._7.input_parse import parse_input

import time
from colorama import Fore, Style, init


def display_frame(frame, wait_seconds, overwrite=False):
    init()

    color_map = {
        '^': Fore.GREEN,
        'S': Fore.YELLOW
    }

    max_width = max(len(str(cell)) for row in frame for cell in row)
    height = len(frame)

    if overwrite:
        print(f"\033[{height}A", end="")

    for row in frame:
        line = ""
        for cell in row:
            cell_str = str(cell).rjust(max_width)

            if isinstance(cell, int):
                if cell > 0:
                    line += f"{Fore.RED}{cell_str}{Style.RESET_ALL}"
                else:
                    line += '.'.rjust(max_width)
            else:
                color = color_map.get(cell, "")
                reset = Style.RESET_ALL if color else ""
                line += f"{color}{cell_str}{reset}"

        print(line)

    time.sleep(wait_seconds)

def main(data):
    data = parse_input(data)
    t_stop = 0.2

    for idy in range(len(data)):
        for idx in range(len(data[idy])):
            if data[idy][idx] == '.':
                data[idy][idx] = 0

    for idx in range(len(data[0])):
        if data[0][idx] == 'S':
            data[0][idx] = 1
            break

    # display_frame(data, t_stop)

    for idy, line in enumerate(data[0:-1]):
        for idx, elem in enumerate(line):

            if isinstance(elem, int) and elem > 0:

                if data[idy + 1][idx] == '^':
                    data[idy + 1][idx - 1] += elem
                    data[idy + 1][idx + 1] += elem
                else :
                    data[idy + 1][idx] += elem


        # display_frame(data, t_stop, overwrite=True)

    out = 0
    for elem in data[-1]:
        if isinstance(elem, int):
            out += elem

    return out
