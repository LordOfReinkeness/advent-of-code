import os
import time

import numpy as np

from challenges._2024._15.input_parse import parse_input

movement_vectors = {
	'^': np.array([0, -1]),
	'>': np.array([1, 0]),
	'v': np.array([0, 1]),
	'<': np.array([-1, 0])
}

def map_print(warehouse_map, robot_position):
	#os.system('cls' if os.name == 'nt' else 'clear')

	out = ''
	for y in range(len(warehouse_map)):
		for x in range(len(warehouse_map[1])):

			if y == robot_position[1] and x == robot_position[0]:
				out += '@'
			else:
				out += warehouse_map[y][x]

		out += '\n'

	print(out)
	time.sleep(0.75)

def main(data):
	warehouse_map, robot_position, robot_movements = parse_input(data)
	# Your challenges for AOC 2024 day 15 part 1 goes here

	for movement in robot_movements:
		next_position = robot_position + movement_vectors[movement]

		if warehouse_map[next_position[1]][next_position[0]] == '.':
			robot_position = next_position
		elif warehouse_map[next_position[1]][next_position[0]] == 'O':
			# 1) move up the 'O's
			# 2) if no wall
			# 2.1) move back while moving 'O's

			next_position_tmp = next_position
			moves = 0

			while warehouse_map[next_position_tmp[1]][next_position_tmp[0]] == 'O':

				next_position_tmp += movement_vectors[movement]
				moves += 1

			if warehouse_map[next_position_tmp[1]][next_position_tmp[0]] == '.':
				for i in range(moves):
					warehouse_map[next_position_tmp[1]][next_position_tmp[0]] = 'O'
					next_position_tmp += (movement_vectors[movement] * -1)

				warehouse_map[next_position[1]][next_position[0]] = '.'
				robot_position = next_position

	out = 0
	for y in range(len(warehouse_map)):
		for x in range(len(warehouse_map[y])):
			if warehouse_map[y][x] == 'O':
				out += y*100 + x


	return out
