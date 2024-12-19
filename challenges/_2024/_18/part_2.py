import os, time

import numpy as np

from challenges._2024._18.input_parse import parse_input
from colorama import Fore, Style
from copy import deepcopy

do_debug = False

max_id = 70
bytes_to_simulate = 1024
possible_directions = [np.array([0, -1]), np.array([1, 0]),  np.array([0, 1]), np.array([-1, 0])]
memory_map_master = []
memory_map = []

class Walker:

	def __init__(self, position: np.array, steps: int = 0, path = None):
		self.position: np.array = position
		self.steps: int = steps

		if path is None:
			self.path =[[1, 1]]
		else:
			self.path = path

	def __lt__(self, other):
		return self.steps < other.steps

	def __str__(self):
		return 'Walker with {} steps'.format(self.steps)

	def map_print(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Current path length: {}'.format(self.steps))
		for y in range(len(memory_map)):
			for x in range(len(memory_map[y])):
				if [x, y] in self.path:
					print(Fore.RED + 'O' + Style.RESET_ALL, end='')
				elif memory_map[y][x] in ['.', 'O']:
					print(Fore.LIGHTBLACK_EX + memory_map[y][x] + Style.RESET_ALL, end='')
				else:
					print(memory_map[y][x], end='')
			print()
		#time.sleep(0.1)

	def walk(self):

		if do_debug: self.map_print()

		if self.position.tolist() == [max_id+1, max_id+1]:
			self.map_print()
			return True, self.path

		new_walkers = []
		for direction in possible_directions:
			next_position: np.array = self.position + direction

			if memory_map[next_position[1]][next_position[0]] == '.':
				memory_map[next_position[1]][next_position[0]] = 'O'
				path = self.path.copy() + [next_position.tolist()]
				new_walkers.append(Walker(next_position, self.steps + 1, path))

		return False, new_walkers


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 18 part 1 goes here

	# settings
	global memory_map_master, memory_map, max_id, bytes_to_simulate

	if len(data) == 25:
		max_id = 6
		bytes_to_simulate = 12

	# build Map and itterate stepps from part 1
	memory_map_master = [['#'] * (max_id + 3)]
	memory_map_master += [['#'] + ['.' for i in range(max_id + 1)] + ['#'] for j in range(max_id + 1)]
	memory_map_master += [['#'] * (max_id + 3)]

	memory_map_master[1][1] = 'O'

	# for elem in data[:bytes_to_simulate]:
	# 	memory_map_master[elem[1] + 1][elem[0] + 1] = '#'
	#
	# # test for obstructions
	# shortest_path = []
	#
	# ## initiate new walker
	# walkers = [Walker(np.array([1, 1]))]
	# memory_map = deepcopy(memory_map_master)
	# finished = False
	# while not finished:
	# 	walker = walkers.pop(0)
	# 	finished, new_walkers = walker.walk()
	#
	# 	if finished:
	# 		shortest_path = deepcopy(new_walkers)
	# 		break
	#
	# 	for walker in new_walkers:
	# 		walkers.append(walker)

	# for elem in data[bytes_to_simulate:]:
	for elem in data:

		# place new obstruction
		memory_map_master[elem[1] + 1][elem[0] + 1] = '#'

		# check if obstruction is not on the fastest path
		# elem_list = [elem[0] + 1, elem[1] + 1]
		# if elem_list in shortest_path:

		# initiate new walker
		memory_map = deepcopy(memory_map_master)
		walkers = [Walker(np.array([1, 1]))]

		finished = False
		while not finished:
			walker = walkers.pop(0)
			finished, new_walkers = walker.walk()

			if finished:
				shortest_path = deepcopy(new_walkers)
				break

			for walker in new_walkers:
				walkers.append(walker)

			if len(walkers) == 0 and not finished:
				return '{},{}'.format(elem[0], elem[1])

			walkers.sort()

		bytes_to_simulate += 1