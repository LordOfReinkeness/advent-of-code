from challenges._2025._6.input_parse import parse_input

def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 6 part 1 goes here

    intermediate = data[0].copy()

    for row in data[1:-1]:
        for idx, val in enumerate(row):

            if data[-1][idx] == '*': intermediate[idx] *= val
            elif data[-1][idx] == '+': intermediate[idx] += val
            else: print(f'Something is wrong in {idx}')

    return sum(intermediate)
