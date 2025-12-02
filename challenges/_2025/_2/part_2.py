from challenges._2025._2.input_parse import parse_input

def main(data):
    data = parse_input(data)
    out = 0

    ids = [str(id) for id_range in data for id in range(id_range[0], id_range[1] + 1)]

    divisors = {}

    for product_id in ids:
        length = len(product_id)

        if length not in divisors:
            divisors[length] = [n for n in range(2, length+1) if length % n == 0]

        for sections in divisors[length]:

            division_length = int(len(product_id) / sections)
            subsections = [product_id[n: n + division_length] for n in range(0, len(product_id), division_length)]

            if len(set(subsections)) == 1:
                out += int(product_id)
                break

    return out
