import numpy as np

from challenges._2024._12.input_parse import parse_input

adjacency_map = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class Plot:

	def __init__(self, plant_type, pos):
		self.plant_type = plant_type
		self.pos = pos
		self.visited = False
		self.neighbours = []

	def __str__(self):
		return self.plant_type

	def set_neighbours(self, neighbours):
		self.neighbours = neighbours

	def is_visited(self):
		return self.visited

	def get_coninous_plot(self, empty_plot, plot_size = 0, firs_call=True):
		self.visited = True
		plot_size += 1
		empty_plot[self.pos[1]][self.pos[0]] = self.plant_type

		for neighbour in self.neighbours:
			if neighbour is not None and not neighbour.is_visited():
				empty_plot = neighbour.get_coninous_plot(empty_plot, plot_size, False)

		if firs_call:
			return [empty_plot, plot_size]
		return empty_plot

def main(data):
	data = parse_input(data)
	garden = []

	# Your challenges for AOC 2024 day 12 part 1 goes here
	for y in range(len(data)):
		garden_row = []
		for x in range(len(data[y])):
			garden_row.append(Plot(data[y][x], [x, y]))
		garden.append(garden_row)

	for y in range(len(data)):
		for x in range(len(data[y])):

			neighbours = []

			for adjacency_vector in adjacency_map:
				adjacent_plot = [x + adjacency_vector[0], y + adjacency_vector[1]]
				if (0 <= adjacent_plot[1] < len(garden) and 0 <= adjacent_plot[0] < len(garden[0])
						and data[y][x] == data[adjacent_plot[1]][adjacent_plot[0]]):
					neighbours.append(garden[adjacent_plot[1]][adjacent_plot[0]])
				else:
					neighbours.append(None)

			garden[y][x].set_neighbours(neighbours)

	plots = []
	for row in garden:
		for plant in row:
			if not plant.is_visited():
				plots.append([plant.plant_type] + plant.get_coninous_plot([['.' for elem in range(len(data[0]))] for line in range(len(data))]))

	adjusted_plots = []

	for plot in plots:

		i = 0
		while plot[0] not in plot[1][i]:
			i+=1
		y_range = [i]
		while i < len(plot[1]) and plot[0] in plot[1][i]:
			i+=1
		y_range.append(i)
		p_transpose = np.array(plot[1]).transpose().tolist()

		i = 0
		while plot[0] not in p_transpose[i]:
			i += 1
		x_range = [i]
		while i < len(p_transpose) and plot[0] in p_transpose[i]:
			i += 1
		x_range.append(i)

		plot_new = [['.'] * (len(plot[1][0][x_range[0]:x_range[1]]) + 2)]
		for y in range(y_range[0], y_range[1]):
			plot_new.append(['.'] + plot[1][y][x_range[0]:x_range[1]] + ['.'])
		plot_new.append(['.'] * (len(plot[1][0][x_range[0]:x_range[1]]) + 2))

		adjusted_plots.append([plot_new, plot[2]])

	for plot in adjusted_plots:

		start = []

		for c in range(len(plot[0][1])):
			if plot[0][1][c] != '.':
				start = [1, c]

		left_vector


	return 'AOC 2024 day 12 part 2'
