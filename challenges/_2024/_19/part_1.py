from challenges._2024._19.input_parse import parse_input

def main(data):
	towels, patters = parse_input(data)
	# Your challenges for AOC 2024 day 19 part 1 goes here

	towels.sort(key=lambda s: len(s))
	print(towels)

	return 'AOC 2024 day 19 part 1'
