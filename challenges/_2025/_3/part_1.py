from challenges._2025._3.input_parse import parse_input

def main(data):
    data = parse_input(data)

    # Your challenges for AOC 2025 day 3 part 1 goes here
    out = 0
    for line in data:
        first_index = line[:-1].index(max(line[:-1]))
        second_index = line[first_index + 1:].index(max(line[first_index + 1:]))
        number = int(f'{line[first_index]}{line[first_index + 1:][second_index]}')
        out += number

    return out
