class RulesGraph:

	def __init__(self, name):
		self.name = name
		self.neighbours = []

	def __str__(self):
		return str(self.name)

	def get_name(self):
		return self.name

	def add_neighbours(self, neighbour):
		self.neighbours.append(neighbour)

	def has_next(self, next):
		for neighbour in self.neighbours:
			if next == neighbour.get_name():
				return True

		return False

def parse_input(data):

	# Your challenges for AOC 2024 day 5 input parsing goes here
	parts = data.strip().split('\n\n')
	rules = [[int(line.split('|')[0]),int(line.split('|')[1])] for line in parts[0].split('\n')]

	numbers = []
	for line in rules:
		numbers += line

	knots = {}
	for elem in set(numbers):
		knots[elem] = RulesGraph(elem)

	for rule in rules:
		knots[rule[0]].add_neighbours(knots[rule[1]])

	sequences = [[int(sequence) for sequence in line.split(',')] for line in parts[1].split('\n')]

	return knots, sequences
