from challenges._2024._8.input_parse import parse_input

def main(data):
	data, interference_field = parse_input(data)
	# Your challenges for AOC 2024 day 8 part 1 goes here
	frequencies = {}
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] != '.':
				if data[y][x] not in frequencies:
					frequencies[data[y][x]] = []
				frequencies[data[y][x]].append([x, y])

	for frequency in frequencies:
		for freq1 in frequencies[frequency]:
			for freq2 in frequencies[frequency]:
				if freq1 != freq2:
					interference_vector = [freq2[0] - freq1[0], freq2[1] - freq1[1]]
					next_interference =  [freq2[0] + interference_vector[0], freq2[1] + interference_vector[1]]

					while -1 < next_interference[1] < len(interference_field) and -1 < next_interference[0] < len(interference_field[0]):

						interference_field[next_interference[1]][next_interference[0]] = '#'
						next_interference = [next_interference[0] + interference_vector[0], next_interference[1] + interference_vector[1]]

	out = 0
	for y in range(len(interference_field)):
		for x in range(len(interference_field[0])):
			if data[y][x] != '.':
				out += 1
			elif interference_field[y][x] != '.':
				out += 1

	return out
