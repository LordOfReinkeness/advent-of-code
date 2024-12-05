import numpy as np

from challenges._2024._4.input_parse import parse_input

def find_x_mas(position, data):

	first_diagonal_coordinates = [position[1] - 1, position[0] - 1, position[1] + 1, position[0] + 1]
	second_diagonal_coordinates = [position[1] + 1, position[0] - 1, position[1] - 1, position[0] + 1]

	if -1 in first_diagonal_coordinates or -1 in second_diagonal_coordinates:
		return 0

	try:
		first_diagonal = [
			data[position[1] - 1][position[0] - 1],
			data[position[1] + 1][position[0] + 1]
		]
		second_diagonal = [
			data[position[1] + 1][position[0] - 1],
			data[position[1] - 1][position[0] + 1]
		]
	except IndexError:
		return 0

	if 'M' in first_diagonal and 'S' in first_diagonal and 'M' in second_diagonal and 'S' in second_diagonal:
		return 1

	return 0


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 4 part 2 goes here
	matches = 0

	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] == 'A':
				matches += find_x_mas([x, y], data)


	return matches
