from challenges._2024._11.input_parse import parse_input, expand

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 11 part 1 goes here

	out = 0
	for elem in data:
		out += expand(elem, 25)

	return out

