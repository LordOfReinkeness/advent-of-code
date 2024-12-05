def parse_input(data):
	out = []
	# Your challenges for AOC 2024 day 2 input parsing goes here
	for line in data.strip().split('\n'):
		out.append( [int(numeric_string) for numeric_string in line.split(' ')])

	return out
