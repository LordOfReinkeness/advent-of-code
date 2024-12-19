import os, time

import numpy as np

from challenges._2024._18.input_parse import parse_input
from colorama import Fore, Style

do_debug = True

max_id = 70
bytes_to_simulate = 1024
possible_directions = [np.array([0, -1]), np.array([1, 0]),  np.array([0, 1]), np.array([-1, 0])]
memory_area = []

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
		for y in range(len(memory_area)):
			for x in range(len(memory_area[y])):
				if [x, y] in self.path:
					print(Fore.RED + 'O' + Style.RESET_ALL, end='')
				elif memory_area[y][x] in ['.', 'O']:
					print(Fore.LIGHTBLACK_EX + memory_area[y][x] + Style.RESET_ALL, end='')
				else:
					print(memory_area[y][x], end='')
			print()
		time.sleep(0.01)

	def walk(self):

		global memory_area

		if do_debug: self.map_print()

		if self.position.tolist() == [max_id+1, max_id+1]:
			return True, [self]

		new_walkers = []
		for direction in possible_directions:
			next_position: np.array = self.position + direction
			if memory_area[next_position[1]][next_position[0]] == '.':
				memory_area[next_position[1]][next_position[0]] = 'O'
				path = self.path.copy() + [next_position.tolist()]
				new_walkers.append(Walker(next_position, self.steps + 1, path))

		return False, new_walkers


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 18 part 1 goes here

	global memory_area, max_id, bytes_to_simulate
	if len(data) == 25:
		max_id = 6
		bytes_to_simulate = 12

	memory_area = [['.' for i in range(max_id + 1)] for j in range(max_id + 1)]

	for i in range(bytes_to_simulate):
		memory_area[data[i][1]][data[i][0]] = '#'

	for i in range(len(memory_area)):
		memory_area[i] = ['#'] + memory_area[i] + ['#']

	memory_area.insert(0, ['#'] * len(memory_area[0]))
	memory_area.append(['#'] * len(memory_area[0]))

	walkers = [Walker(np.array([1, 1]))]
	finished = False
	while not finished:
		walker = walkers.pop(0)
		finished, new_walkers = walker.walk()

		if finished:
			return new_walkers[0].steps

		for walker in new_walkers:
			walkers.append(walker)

		walkers.sort()
