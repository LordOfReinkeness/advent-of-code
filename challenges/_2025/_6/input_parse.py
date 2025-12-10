import re

def parse_input(data: str):
    pattern = '(\S*)\s*'

    out = []

    for line in [[number for number in re.findall(pattern, line.strip())] for line in data.strip().split('\n')[:-1]]:
        while '' in line:
            line.remove('')

        out.append([int(elem) for elem in line])

    last = re.findall(pattern, data.strip().split('\n')[-1].strip())
    while '' in last:
        last.remove('')

    return out + [last]
