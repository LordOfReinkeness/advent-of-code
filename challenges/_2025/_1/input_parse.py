def parse_input(data: str):
    out = []
    for line in  [line for line in data.strip().split('\n')]:
        out.append([line[:1], int(line[1:])])

    return out