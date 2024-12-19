import numpy as np


def parse_input(data: str):

	warehouse_map = [list(line) for line in data.strip().split('\n\n')[0].split('\n')]

	for y in range(len(warehouse_map)):
		for x in range(len(warehouse_map[y])):
			if warehouse_map[y][x] == '@':
				warehouse_map[y][x] = '.'
				return warehouse_map, np.array([x, y]), data.strip().split('\n\n')[1].replace('\n', '')
