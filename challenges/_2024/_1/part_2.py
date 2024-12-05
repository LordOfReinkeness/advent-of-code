from challenges._2024._1.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 1 part 2 goes here

	number_values = {}

	for num in data[1]:
		if num not in number_values:
			number_values[num] = 0

		number_values[num] += 1

	out = 0

	for num in data[0]:
		if num in number_values:
			out += num * number_values[num]

	return out