def parse_input(data):
	out = [[],[]]
	# Your challenges for AOC 2024 day 1 input parsing goes here

	for line in data.split('\n'):
		out[0].append(int(line.split('   ')[0]))
		out[1].append(int(line.split('   ')[1]))

	return out
