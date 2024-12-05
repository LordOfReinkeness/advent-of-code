import re

import numpy as np
from challenges._2024._4.input_parse import parse_input

def rotate_45(data):
	out = []
	for i in range(len(data)*2):
		start = [max(0, i-9), min(i, 9)]
		line = ''
		y = start[1]

		for x in range(start[0], len(data[0])):
			line += data[y][x]
			y -= 1
			x += 1

			if x >= len(data[0]) or y < 0:
				break

		out.append(line)
	return out

def rotate_320(data):
	out = []
	for i in range(len(data) - 1, -1 * (len(data)), -1):
		start = [max(0, i), max(-1*i, 0)]
		line = ''
		y = start[1]

		for x in range(start[0], len(data[start[0]])):
			line += data[y][x]
			y += 1
			x += 1

			if x >= len(data[0]) or y >= len(data):
				break

		out.append(line)
	return out

def get_mas_from_direction(direction, position, data):
	match = 'MAS'
	for c in match:
		position[0] += direction[0]
		position[1] += direction[1]

		if position[0] < 0 or position[1] < 0:
			return 0

		try:
			current_char = data[position[1]][position[0]]
		except:
			return 0

		if current_char != c:
			return 0

	return 1

def main(data):

	data = parse_input(data)
	# Your challenges for AOC 2024 day 4 part 1 goes here
	matches = 0
	directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

	# rotations = [''.join(line) for line in data] + [''.join(line) for line in np.array(data).transpose().tolist()] + rotate_45(data) + rotate_320(data)
	# reg_forward = 'XMAS'
	# reg_backwards = 'SAMX'
	# for l in rotations:
	# 	matches += len(re.findall(reg_forward, l))
	# 	matches += len(re.findall(reg_backwards, l))

	#print(np.array(data))

	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == 'X':
				for direction in directions:
					matches += get_mas_from_direction(direction, [x, y], data)


	return matches
