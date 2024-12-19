import sys
import os
import time
from copy import deepcopy

import matplotlib
from colorama import Fore, Style

import numpy as np
from matplotlib import pyplot as plt

from challenges._2024._16.input_parse import parse_input

path_id = 0
best_path = 121488
do_debug = True
rotations = ['>', 'v', '<', '^']
valid_directions = {
	'>': [ np.array([1, 0]), np.array([0, 1]), np.array([0, -1]) ],
	'v': [ np.array([0, 1]), np.array([-1, 0]), np.array([1, 0]) ],
	'<': [ np.array([-1, 0]), np.array([0, -1]), np.array([0, 1]) ],
	'^': [ np.array([0, -1]), np.array([1, 0]), np.array([-1, 0]) ]
}
heat_map = []

def create_initial_plot(data):
	fig, ax = plt.subplots()

	# Identify the valid normal values (>=0 and < sys.maxsize)
	normal_values = data[(data >= 0) & (data < sys.maxsize)]
	if normal_values.size > 0:
		max_valid_val = normal_values.max()
	else:
		# If no normal values, set a default max_valid_val
		max_valid_val = 0

	# Create a custom colormap:
	# Normalization: -1 maps to 0.0, sys.maxsize maps to 1.0
	# so the range is [-1, max_valid_val+1] since sys.maxsize should map to that upper bound.
	norm = matplotlib.colors.Normalize(vmin=-1, vmax=max_valid_val + 1)

	# Calculate fractions for the key points
	# fraction = (value - (-1)) / ((max_valid_val+1) - (-1)) = (value + 1) / (max_valid_val + 2)
	frac_neg_1 = 0.0  # for value -1
	frac_0 = (0 + 1) / (max_valid_val + 2)  # for value 0
	frac_max = (max_valid_val + 1) / (max_valid_val + 2)  # for value max_valid_val
	frac_maxsize = 1.0  # for value max_valid_val+1 (sys.maxsize)

	# Define colors:
	# At -1 (frac_neg_1): black
	# At 0 (frac_0): dark red
	# At max_valid_val (frac_max): bright red
	# At sys.maxsize (frac_maxsize): white

	# We'll choose dark red as something like '#8B0000' (a deep red),
	# and bright red as '#FF0000'.
	cdict = [(frac_neg_1, 'black'),
			 (frac_0, '#8B0000'),  # dark red
			 (frac_max, '#FF0000'),  # bright red
			 (frac_maxsize, 'white')]

	cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom_red_map", cdict)

	# Plot the data
	img = ax.imshow(data, cmap=cmap, norm=norm, origin='lower')

	plt.colorbar(img, ax=ax)
	plt.show(block=False)
	plt.pause(0.1)

	return fig, ax, img


def update_plot(img, data):
	# Identify the valid normal values again
	normal_values = data[(data >= 0) & (data < sys.maxsize)]
	if normal_values.size > 0:
		max_valid_val = normal_values.max()
	else:
		max_valid_val = 0

	# Update normalization to cover new range if needed
	img.norm.vmax = max_valid_val + 1

	# Update the data
	img.set_data(data)

	# Since vmax may have changed, we can re-draw
	img.figure.canvas.draw()
	img.figure.canvas.flush_events()

class Maze:
	def __init__(self, arena_map, position, rotation = 0, cost = 0):
		self.arena_map = arena_map
		self.position = position
		self.rotation = rotation
		self.cost = cost

		global path_id
		self.id = path_id
		path_id += 1

	def __lt__(self, other):
		return self.cost < other.cost

	def __str__(self):
		return 'Path wit ID {} (has {} Points cost)'.format(self.id, self.cost)

	def map_print(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Current cost: {}'.format(self.cost))
		for line in self.arena_map:
			for c in line:
				if c in rotations:
					print(Fore.RED + c + Style.RESET_ALL, end='')
				elif c == '.':
					print(Fore.LIGHTBLACK_EX + c + Style.RESET_ALL, end='')
				else:
					print(c, end='')
			print()
		time.sleep(0.25)

	def move(self):
		if self.arena_map[self.position[1]][self.position[0]] == 'E':
			return True, self.cost

		if self.cost < heat_map[self.position[1]][self.position[0]]:
			heat_map[self.position[1]][self.position[0]] = self.cost
		else:
			return False, []

		# if do_debug:
		# 	self.arena_map[self.position[1]][self.position[0]] = rotations[self.rotation]
		# 	self.map_print()

		new_paths = []
		for x in range(-1, 2):

			next_pos = self.position + valid_directions[rotations[self.rotation]][x]
			if self.arena_map[next_pos[1]][next_pos[0]] != '#':

				if self.arena_map[next_pos[1]][next_pos[0]] in rotations:
					continue
				else:
					new_paths.append(Maze(
						deepcopy(self.arena_map),
						next_pos,
						(self.rotation + x) % 4,
						self.cost + (abs(1000 * x) + 1)
					))

		return False, new_paths

def main(data):
	arena_map = parse_input(data)
	# Your challenges for AOC 2024 day 16 part 1 goes here

	global heat_map
	# For interactive updates
	plt.ion()
	heat_map = [[(sys.maxsize if c != '#' else -1) for c in line] for line in arena_map]
	paths = [Maze(deepcopy(arena_map), np.array([1, len(arena_map) - 2]))]

	if do_debug:
		fig, ax, img = create_initial_plot(np.array(heat_map))

	i = 0
	while True:
		current_path = paths.pop(0)
		done, new_paths = current_path.move()
		if done:
			return new_paths

		for new_path in new_paths:
			paths.append(new_path)

		paths.sort()

		if do_debug and i%100 == 0:
			update_plot(img, np.array(heat_map))

		i += 1