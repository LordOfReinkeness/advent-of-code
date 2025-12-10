def parse_input(data: str):
    ranges, ingredients = data.strip().split('\n\n')

    ranges = [[int(n) for n in r.split('-')] for r in ranges.split('\n')]
    ingredients = [int(n) for n in ingredients.split('\n')]

    return ranges, ingredients