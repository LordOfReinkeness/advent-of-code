import numpy as np
from challenges._2024._14.input_parse import parse_input

room_size = np.array([101, 103])

class Robot:

	def __init__(self, position: np.array, velocity: np.array):
		self.position = position
		self.velocity = velocity

	def move(self):
		self.position = (self.position + self.velocity) % room_size

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 14 part 1 goes here
	robots = []
	for row in data:
		robots.append(Robot(row[0], row[1]))

	for i in range(1000):
		for robot in robots:
			robot.move()

		room = [[0 for p in range(room_size[0])] for line in range(room_size[1])]

		for robot in robots:
			room[robot.position[1]][robot.position[0]] += 1

		robots_in_all_quadrants = []
		for q_y in range(2):
			for q_x in range(2):

				quadrand_robots = 0
				offset = np.array([q_x * int((room_size[0] / 2) + 0.5), q_y * int((room_size[1] / 2) + 0.5)])
				for y in range(int(room_size[1] / 2)):
					for x in range(int(room_size[0] / 2)):
						pos = (offset + np.array([x, y])).tolist()
						quadrand_robots += room[pos[1]][pos[0]]

				robots_in_all_quadrants.append(quadrand_robots)

		robots_in_all_quadrants.sort()
		if robots_in_all_quadrants[:3] == [0, 0, 0]:
			print(i)