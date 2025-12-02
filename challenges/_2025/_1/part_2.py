from challenges._2025._1.input_parse import parse_input

def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 1 part 1 goes here

    indicator = 50
    password = 0

    for elem in data:
        for i in range(elem[1]):
            if elem[0] == "R":
                indicator += 1
            elif elem[0] == "L":
                indicator -= 1

            indicator %= 100

            if indicator == 0:
                password += 1

    return password