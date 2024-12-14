from challenges._2024._12.input_parse import parse_input

adjacency_map = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class Plot:

	def __init__(self, plant_type):
		self.plant_type = plant_type
		self.visited = False
		self.neighbours = []

	def __str__(self):
		return self.plant_type

	def set_neighbours(self, neighbours):
		self.neighbours = neighbours

	def is_visited(self):
		return self.visited

	def get_fencing_const(self, plot_size = 0):
		self.visited = True
		out = 0
		plot_size += 1

		for neighbour in self.neighbours:
			if neighbour is None:
				out += 1
			elif not neighbour.is_visited():
				fences, plot_size = neighbour.get_coninous_plot(plot_size)
				out += fences

		return out, plot_size


def main(data):
	data = parse_input(data)
	garden = []

	# Your challenges for AOC 2024 day 12 part 1 goes here
	for y in range(len(data)):
		garden_row = []
		for x in range(len(data[y])):
			garden_row.append(Plot(data[y][x]))
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

	out = 0
	for row in garden:
		for plant in row:
			if not plant.is_visited():
				fences, plots = plant.get_fencing_const()
				out += fences * plots

	return out
