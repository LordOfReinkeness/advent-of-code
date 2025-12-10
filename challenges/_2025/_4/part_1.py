from challenges._2025._4.input_parse import parse_input

def main(data):
    data = parse_input(data)
    # Your challenge for AOC 2025 day 4 part 1 goes here
    out = 0

    for idy, line in enumerate(data):
        for idx, elem in enumerate(line):

            # for every element in the input array
            if elem == '@':
                submatrix = data[max(0, idy-1):min(len(line),idy+2), max(0, idx-1):min(len(line),idx+2)]
                number_at = sum(list(x).count('@') for x in submatrix) - 1
                if number_at < 4:
                    out += 1


    return out
