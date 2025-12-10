from challenges._2025._3.input_parse import parse_input

def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 3 part 2 goes here
    out = 0

    for line in data:

        number_length = 12
        last_index = -1
        number = ''

        for idx in range(
                len(line) - number_length + 1,
                len(line) + 1
        ):
            current_section = line[last_index + 1:idx]
            last_index = last_index + 1 + current_section.index(max(current_section))
            number += str(line[last_index])

        out += int(number)

    return out
