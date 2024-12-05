from challenges._2024._1.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 1 part 1 goes here
	data[0].sort()
	data[1].sort()

	out = 0

	for i in range(len(data[0])):
		out += abs(data[0][i] - data[1][i])

	return out
