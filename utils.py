import numpy as np
from colorama import Fore, Style, init
import time, sys

two_x_two_matrix = [
    [[-1, -1], [-1, 0], [-1, 1]],
    [[0, -1], [0, 0], [0, 1]],
    [[1, -1], [1, 0], [1, 1]]
]

np_two_x_two_matrix = np.array(two_x_two_matrix)

def print_2d_matrix(matrix):

    for line in matrix:
        print(''.join(line))


class IdRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __lt__(self, other: IdRange):
        return self.start < other.start

    def __str__(self):
        return f'Range from {self.start} to {self.end}'

    def join(self, other):
        assert self.start <= other.start

        if self.end >= other.start:
            self.end = max(self.end, other.end)
        else:
            raise IdRangeJoinException

    def contains(self, ingredient):
        return self.start <= ingredient <= self.end

    def get_range(self):
        return range(self.start, self.end + 1)

class IdRangeJoinException(Exception):
    pass


def animate_frames(frames):
    init()

    color_map = {
        '|': Fore.RED,
        '^': Fore.GREEN,
        'S': Fore.YELLOW,
        1: Fore.RED,
        2: Fore.RED,
        3: Fore.RED,
        4: Fore.RED,
        5: Fore.RED,
        6: Fore.RED,
        7: Fore.RED,
        8: Fore.RED,
        9: Fore.RED
    }

    height = len(frames[0])

    for i, frame in enumerate(frames):
        if i > 0:
            time.sleep(0.2)
            print(f"\033[{height}A", end="")

        for row in frame:
            line = ""
            for char in row:
                color = color_map.get(char, "")
                reset = Style.RESET_ALL if color else ""
                line += f"{color}{char}{reset}"
            print(line)

class FrameAnimator:
    def __init__(self, base_array):
        init()
        self.base_array = base_array
        self.height = len(base_array)
        self.first_frame = True
        self.color_map = {
            '|': Fore.RED,
            '^': Fore.GREEN,
            'S': Fore.YELLOW
        }

    def show_frame(self, pipe_positions):
        if not self.first_frame:
            sys.stdout.write(f"\033[{self.height + 1}F")
            sys.stdout.flush()

        pipe_set = {(y, x) for y, x in pipe_positions}

        for y, row in enumerate(self.base_array):
            line = ""
            for x, char in enumerate(row):
                if (y, x) in pipe_set:
                    char = '|'
                color = self.color_map.get(char, "")
                reset = Style.RESET_ALL if color else ""
                line += f"{color}{char}{reset}"
            sys.stdout.write(f"\033[2K{line}\n")

        sys.stdout.write("\033[2K")
        sys.stdout.flush()
        time.sleep(0.1)
        self.first_frame = False