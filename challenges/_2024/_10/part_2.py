from challenges._2024._10.input_parse import parse_input

data = []
adjacency_map = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def get_trailheads(x, y):
	if data[y][x] == 9:
		return 1

	out = 0
	for adjacency_vector in adjacency_map:
		next_x = x + adjacency_vector[0]
		next_y = y + adjacency_vector[1]
		if 0 <= next_x < len(data[0]) and 0 <= next_y < len(data) and data[y][x] + 1 == data[next_y][next_x]:
			out += get_trailheads(next_x, next_y)

	return out

def main(data_unparsed):
	global data
	data = parse_input(data_unparsed)
	# Your challenges for AOC 2024 day 10 part 1 goes here

	out = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == 0:
				out += get_trailheads(x, y)

	return out
