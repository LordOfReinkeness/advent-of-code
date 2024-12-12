import numpy as np

from challenges._2024._10.input_parse import parse_input

data = []
# adjacency_map = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
adjacency_map = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def get_trailheads(x, y, trail_map):

	if not data[y][x] == 9:
		for adjacency_vector in adjacency_map:
			next_x = x + adjacency_vector[0]
			next_y = y + adjacency_vector[1]
			if 0 <= next_x < len(data[0]) and 0 <= next_y < len(data) and data[y][x] + 1 == data[next_y][next_x]:
				trail_map[next_y][next_x] = str(data[next_y][next_x])
				get_trailheads(next_x, next_y, trail_map)

def main(data_unparsed):
	global data
	data = parse_input(data_unparsed)
	# Your challenges for AOC 2024 day 10 part 1 goes here

	out = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == 0:
				# print('Starting trail at coordinates [{},{}]'.format(x, y))
				trail_map = [['.' for c in line] for line in data]
				trail_map[y][x] = '0'
				get_trailheads(x, y, trail_map)

				trail_level = 0

				for line in trail_map:
					for c in line:
						# print(c, end='')
						if c == '9':
							trail_level += 1
					# print()
				# print('Trail level is: ' + str(trail_level) + '\n')

				out += trail_level

	return out
