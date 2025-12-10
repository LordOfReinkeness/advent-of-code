from challenges._2025._5.input_parse import parse_input
from utils import IdRange, IdRangeJoinException

def main(data):
    ranges, ingredients = parse_input(data)
    # Your challenge for AOC 2025 day 5 part 1 goes here

    non_spoiled_ranges = [IdRange(id_range[0], id_range[1]) for id_range in ranges]
    non_spoiled_ranges.sort()

    joined_non_spoiled_ranges = []

    while len(non_spoiled_ranges) > 1:
        first_range = non_spoiled_ranges.pop(0)
        second_range = non_spoiled_ranges.pop(0)

        try:
            first_range.join(second_range)
        except IdRangeJoinException:
            joined_non_spoiled_ranges.append(first_range)
            non_spoiled_ranges.insert(0, second_range)
        else:
            non_spoiled_ranges.insert(0, first_range)

    joined_non_spoiled_ranges += non_spoiled_ranges

    out = 0
    for ingredient in ingredients:
        for joined_non_spoiled_range in joined_non_spoiled_ranges:
            if joined_non_spoiled_range.contains(ingredient):
                out += 1
                break

    return out