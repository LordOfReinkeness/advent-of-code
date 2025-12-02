from challenges._2025._2.input_parse import parse_input

def main(data):
    data = parse_input(data)
    out = 0

    ids = [str(id) for id_range in data for id in range(id_range[0], id_range[1]+1)]

    for product_id in ids:
        if len(product_id) % 2 == 0:
            split = int(len(product_id) / 2)
            if len({product_id[:split], product_id[split:]}) == 1:
                out += int(product_id)

    return out
