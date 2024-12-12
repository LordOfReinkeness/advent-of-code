from challenges._2024._6.input_parse import parse_input


def main(data):
	guard_chars = ['^', '>', 'v', '<']
	guard_moves = {
		'^': [0, -1],
		'>': [1, 0],
		'v': [0, 1],
		'<': [-1, 0]
	}

	data = parse_input(data)
	guard = []
	# Your challenges for AOC 2024 day 6 part 1 goes here

	## get guard
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] not in ['.', '#']:
				guard = [data[y][x], [x, y]]
				break
		else:
			continue

		break


	# move guard
	while True:
		data[guard[1][1]][guard[1][0]] = 'X'
		guard_direction = guard_moves[guard[0]]
		guard_next = [guard[1][0] + guard_direction[0], guard[1][1] + guard_direction[1]]

		# check if guard walks out
		if -1 < guard_next[1] < len(data) and -1 < guard_next[0] < len(data[0]):

			# guard hits obstacle
			if data[guard_next[1]][guard_next[0]] == '#':
				guard[0] = guard_chars[ (guard_chars.index(guard[0]) + 1) % len(guard_chars) ]

			# guard can walk
			else:
				guard[1] = guard_next

		else:
			break

	out = 0
	for line in data:
		for c in line:
			if c == 'X':
				out += 1

	return out
